# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.iptables
----------------

This module provides all high level to low level access to iptables.
"""
import os
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Union

import iptc  # type: ignore
import yaml
from iptc.ip4tc import Table as Table4  # type: ignore
from iptc.ip6tc import Table6  # type: ignore

from connord import exceptions, resources, user
from connord.config import Config
from connord.exceptions import IptablesError
from connord.formatter import Formatter
from connord.printer import Printer
from connord.resources import (
    FileResource,
    IptablesSaveDirectory,
    IptablesTemplate,
    YamlFileResource,
)
from connord.servers import Server
from connord.wrappers import nettools
from connord.wrappers.commands import Command


class IPTCTable:
    def __init__(self, table: Union[Table4, Table6]):
        self.table = table

    def print(self, stream: bool):
        formatter = IptablesPrettyFormatter()
        stream_file = formatter.get_stream_file(stream)

        self.table.refresh()
        table_header = formatter.format_table_header(self.table)
        print(table_header, file=stream_file)
        for chain in self.table.chains:
            chain_header = formatter.format_chain_header(chain)
            print(chain_header, file=stream_file)
            counter = 1
            for rule in chain.rules:
                rule_s = formatter.format_rule(rule, counter)
                print(rule_s, file=stream_file)
                counter += 1

        return formatter.get_output()


class IptablesBlueprint:
    table: str
    ipv6: bool
    counters: bool
    specification: dict

    def __init__(
        self, table: str, ipv6: bool, specification: dict = None, counters: bool = False
    ):
        self.table = table
        self.ipv6 = ipv6
        self.counters = counters
        self.specification = (
            specification if specification else self.make_specification()
        )

    def flush(self):
        printer = Printer()
        with printer.Do(f"Flushing table '{self.table}', ipv6={self.ipv6!r}"):
            iptc.easy.flush_table(self.table, ipv6=self.ipv6)

            chain: str
            for chain in iptc.easy.get_chains(self.table, ipv6=self.ipv6):
                iptc.easy.set_policy(self.table, chain, policy="ACCEPT", ipv6=self.ipv6)

    def set_counters(self, chain: str, values: Tuple[int, int] = (0, 0)):
        """
        IMPORTANT:
        Adding counters is currently not working although the code below should
        actually work. It's tested in the python console with some strange side
        effects, like counters manipulation in another rule than specified with far
        too high values. Use this function not with the current version of
        python-iptables==1.0.0

        :param chain: String: The chain for which to add counters
        :param values: Tuple: A tuple of two integers where the first is the counter
        for packets and the second is the counter for bytes. default: (0, 0)
        """
        table = Table4(self.table) if not self.ipv6 else Table6(self.table)
        iptc_chain = iptc.Chain(table, chain)
        if iptc_chain.is_builtin():
            policy = iptc_chain.get_policy()
            iptc_chain.set_policy(policy, counters=values)

    def add_chain(self, chain: str):
        if not iptc.easy.has_chain(self.table, chain, ipv6=self.ipv6):
            iptc.easy.add_chain(self.table, chain, ipv6=self.ipv6)

        policy = self.specification[chain].get("policy", "None")
        if policy != "None":
            iptc.easy.set_policy(self.table, chain, policy=policy, ipv6=self.ipv6)

        if self.counters:
            # Currently, setting counters for chains is not working. See comment for
            # self.set_counters method.
            pass

    def init_chains(self):
        for chain in self.specification:
            self.add_chain(chain)

    def add_rule(self, chain: str, rule: dict):
        if iptc.easy.test_rule(rule, ipv6=self.ipv6):
            try:
                if self.counters:
                    packets, bytes_ = (
                        rule["counters"]["packets"],
                        rule["counters"]["bytes"],
                    )
                    del rule["counters"]
                    rule["counters"] = (packets, bytes_)

                iptc.easy.add_rule(self.table, chain, rule, ipv6=self.ipv6)
                return
            except ValueError:
                pass

        raise IptablesError(f"Malformed rule: {rule}\n  in {self.table}.{chain}")

    def add_rules(self, chain: str):
        try:
            rule: dict
            for rule in self.specification[chain]["rules"]:
                self.add_rule(chain, rule)
        except KeyError:
            pass

    def apply_specification(self) -> bool:
        self.flush()
        self.init_chains()

        printer = Printer()
        with printer.Do(f"Applying table {self.table!r}, ipv6={self.ipv6}"):
            chain: str
            for chain in self.specification:
                self.add_rules(chain)

        return True

    def get_rules(self, chain: str):
        rules: List[Dict] = iptc.easy.get_rule(self.table, chain, ipv6=self.ipv6)
        rule: Dict
        for rule in rules:
            if not self.counters:
                del rule["counters"]
            else:
                packets, bytes_ = rule["counters"]
                del rule["counters"]
                rule["counters"] = {"packets": packets, "bytes": bytes_}
        return rules

    def get_chains(self):
        return iptc.easy.get_chains(self.table, ipv6=self.ipv6)

    def get_policy(self, chain: str):
        table = Table4(self.table) if not self.ipv6 else Table6(self.table)
        return (
            iptc.easy.get_policy(self.table, chain, ipv6=self.ipv6)
            if iptc.Chain(table, chain).is_builtin()
            else None
        )

    def make_specification(self):
        specification: Dict = {}
        for chain in self.get_chains():
            rules = self.get_rules(chain)
            policy = self.get_policy(chain)
            specification[chain] = {}
            specification[chain]["policy"] = str(policy)
            specification[chain]["action"] = "create"
            specification[chain]["rules"] = rules

        return specification


class YamlTemplate(IptablesTemplate):
    # TODO initialize with Server and protocol

    def apply(self, server: Server = None, protocol: str = None) -> bool:
        printer = Printer()
        printer.info(f"Applying template: {self.path.name!r}")

        specification: dict = self.read_with_server(server, protocol)
        blueprint = IptablesBlueprint(self.table, self.is_ipv6(), specification)
        blueprint.apply_specification()

        return True

    def render_with_server(self, server: Server = None, protocol: str = None) -> str:
        """Render a jinja2 template with data from config.yml per default. Adds some
        useful variables to the environment which can be used in rules and fallback
        files.

        :param server: a Server
        :param protocol: 'udp' or 'tcp'
        :returns: the rendered template as string
        """

        config = Config().copy()

        # TODO: add run configuration to subdict config['run']
        config["vpn_remote"] = server.ip_address if server else "0.0.0.0/0"
        config["vpn_protocol"] = protocol if protocol else "udp"
        config["vpn_port"] = "1194" if protocol == "udp" else "443"

        config["gateways"] = nettools.get_gateways()

        env = load_environment()
        config.update(env)
        return self.render(dict(config))

    def read_with_server(self, server: Server = None, protocol: str = None) -> dict:
        """High-level abstraction for the render_template method

        :param server: the server as dict or None
        :param protocol: the used protocol as string. may be one of 'udp' or 'tcp'
        :returns: the rendered template file as dictionary
        """

        rendered_template = self.render_with_server(server, protocol)
        return yaml.safe_load(rendered_template)


class YamlTemplates:
    resource: resources.IptablesTemplatesDirectory
    templates: List[YamlTemplate]

    def __init__(self):
        self.resource = resources.IptablesTemplatesDirectory()
        self.templates = [YamlTemplate(t.path) for t in self.resource.list_templates()]

    def apply(self, server: Server = None, protocol: str = None) -> bool:
        for template in self.templates:
            if not template.apply(server, protocol):
                return False

        return True

    def filter_by_predicate(self, pred: Callable[[YamlTemplate], bool]):
        self.templates = [t for t in self.templates if pred(t)]


def list_templates() -> bool:
    printer = Printer()
    yaml_templates = YamlTemplates()

    paths = "\n".join(str(t.path) for t in yaml_templates.templates)
    print(paths, file=printer)

    return True


@user.needs_root
def load_environment() -> dict:
    """Merge environment files with the configuration file

    Configuration file variables overwrite variables from environment
    """
    stats_resource = resources.StatsDirectory()
    if not stats_resource.exists():
        return {}

    env = {}
    # TODO What happens when openvpn is going down. Is the up.env variable deleted ??
    yaml_resources = [
        resources.YamlFileResource(f) for f in stats_resource.list_files(suffix="env")
    ]
    for resource in yaml_resources:
        env.update(resource.read())

    return env


def load_from_stats() -> Tuple[Server, str]:
    try:
        server = Server.from_resource(resources.YamlStatsFile(filename="server"))

        stats_resource = resources.YamlStatsFile(filename="stats")
        stats = stats_resource.read()
        protocol = stats["last_server"]["protocol"]
    except (exceptions.ResourceNotFoundError, KeyError):
        raise exceptions.IptablesError(
            "Cannot apply 'rules' files when not connected to a NordVPN server."
        )
    return server, protocol


def apply(table: str, fallback: bool = False, ipv6: bool = False) -> bool:
    templates: YamlTemplates = YamlTemplates()
    templates.filter_by_predicate(
        lambda t: t.table == table
        and t.is_fallback() == fallback
        and t.is_ipv6() == ipv6
    )

    server: Optional[Server] = None
    protocol: Optional[str] = None
    if not fallback:
        server, protocol = load_from_stats()

    return templates.apply(server, protocol)


def reload() -> bool:
    server: Server
    protocol: str

    server, protocol = load_from_stats()

    templates = YamlTemplates()
    templates.filter_by_predicate(lambda t: not t.is_fallback())
    return templates.apply(server, protocol)


def flush_tables(ipv6: bool = False):
    """Flush all tables and apply the default policy ACCEPT to standard tables"""
    printer = Printer()
    with printer.Do(f"Flushing all tables: ipv6={ipv6!r}"):
        iptc.easy.flush_all(ipv6=ipv6)

    with printer.Do("Setting ACCEPT policy in all chains"):
        tables: List[str] = iptc.easy.get_tables(ipv6=ipv6)
        for table in tables:
            chains: List[str] = iptc.easy.get_chains(table, ipv6=ipv6)
            for chain in chains:
                iptc.easy.set_policy(table, chain, policy="ACCEPT", ipv6=ipv6)


def reset(fallback: bool = True):
    """Reset all tables to fallback if True else just flush them"""
    if fallback:
        templates = YamlTemplates()
        templates.filter_by_predicate(lambda t: t.is_fallback())
        templates.apply()
    else:
        flush_tables(ipv6=False)
        flush_tables(ipv6=True)


def verify_table(table: str) -> bool:
    """Return true if the table is a valid table name

    :param table: table as string
    """
    return table in Table4.ALL or table in Table6.ALL


class IptablesSaveCommand(Command):
    def __init__(
        self,
        table: str = None,
        file: str = None,
        ipv6: bool = False,
        counters: bool = False,
    ):
        command: str = "ip6tables-save" if ipv6 else "iptables-save"
        super().__init__(command)

        self.file = file

        if table:
            self.add_option("table", table)
        if counters:
            self.add_option("counters")
        if file:
            self.add_option("file", file)

    def run(self, **kwargs):
        if self.file:
            with Path(self.file).open("w", encoding="utf8") as filed:
                return super().run(stdout=filed, encoding="utf8", text=True)
        else:
            return super().run(stdout=sys.stdout)


class IptablesRestoreCommand(Command):
    file: Optional[str]

    def __init__(
        self,
        table: str = None,
        file: str = None,
        ipv6: bool = False,
        dry_run: bool = False,
        counters: bool = False,
    ):
        command: str = "ip6tables-restore" if ipv6 else "iptables-restore"
        super().__init__(command)

        self.file = file

        if table:
            self.add_option("table", table)
        if dry_run:
            self.add_option("test")
        if counters:
            self.add_option("counters")
        if file:
            self.add_arguments(file)


class IptablesSaveFile(FileResource):
    def __init__(
        self, path: Union[str, os.PathLike], table: str = None, ipv6: bool = False
    ):
        parent = IptablesSaveDirectory()
        super().__init__(parent.path / path)
        self.table = table
        self.ipv6 = ipv6

    def save(self, counters: bool = False):
        raise NotImplementedError()

    def restore(self, dry_run: bool = False, counters: bool = False):
        raise NotImplementedError()

    def is_ipv6(self) -> bool:
        return self.ipv6


class IptablesSaveNativeFile(IptablesSaveFile):
    def __init__(
        self,
        table: str = None,
        ipv6: bool = False,
        file: Union[str, os.PathLike] = None,
    ):
        if file:
            file_name = str(file)
        else:
            if table:
                base = table
            else:
                base = "iptables"

            file_name = base + ("6" if ipv6 else "") + ".save"

        super().__init__(file_name, table=table, ipv6=ipv6)

    def save(self, counters: bool = False):
        command = IptablesSaveCommand(
            table=self.table,
            file=str(self.path_not_exist_ok()),
            ipv6=self.is_ipv6(),
            counters=counters,
        )
        command.run()

    def restore(self, dry_run: bool = False, counters: bool = False):
        command = IptablesRestoreCommand(
            table=self.table,
            file=str(self.path_not_exist_ok()),
            ipv6=self.is_ipv6(),
            dry_run=dry_run,
            counters=counters,
        )
        command.run()


class IptablesSaveYamlFile(IptablesSaveFile):
    table: str
    ipv6: bool

    def __init__(self, table: str, ipv6: bool = False):
        file_name = table + ("6" if ipv6 else "") + ".save"
        super().__init__(file_name)
        self.table = table
        self.ipv6 = ipv6

    def save(self, counters: bool = False):
        blueprint = IptablesBlueprint(self.table, self.ipv6, counters=counters)

        yaml_resource = YamlFileResource(self.path_not_exist_ok())
        yaml_resource.write_safe(blueprint.specification)

    # TODO what about restoring counters
    def restore(self, dry_run: bool = False, counters: bool = False):
        yaml_resource = YamlFileResource(self.path)
        specification: Dict = yaml_resource.read()

        blueprint = IptablesBlueprint(
            self.table, self.ipv6, specification=specification, counters=counters
        )
        blueprint.apply_specification()


class SaveIptablesStrategy:
    table: Optional[str]
    path: Optional[Path]
    directory: Optional[Path]
    counters: bool
    ipv6: bool

    def __init__(
        self,
        table: str = None,
        path: str = None,
        directory: str = None,
        counters: bool = False,
        ipv6: bool = False,
    ):
        self.table = table
        self.path = Path(path) if path else None
        self.directory = Path(directory) if directory else None
        self.counters = counters
        self.ipv6 = ipv6

    def execute(self):
        raise NotImplementedError()


class SaveIptablesNativeFormat(SaveIptablesStrategy):
    def execute(self):
        save_file: IptablesSaveFile = IptablesSaveNativeFile(
            table=self.table, ipv6=self.ipv6, file=self.path
        )
        save_file.save(counters=self.counters)


class SaveIptablesYamlFormat(SaveIptablesStrategy):
    def execute(self):
        if self.table:
            tables = [self.table]
        else:
            tables = Table4.ALL if not self.ipv6 else Table6.ALL

        for table_ in tables:
            save_file = IptablesSaveYamlFile(table=table_, ipv6=self.ipv6)
            if self.directory:
                save_file.path = self.directory / save_file.path_not_exist_ok().name
            save_file.save(counters=self.counters)


@user.needs_root
def save(
    table: str = None,
    file_path: str = None,
    directory: str = None,
    format_: str = "iptables",
    counters: bool = False,
    ipv6: bool = False,
):
    save_strategy: SaveIptablesStrategy
    if format_ == "iptables":
        save_strategy = SaveIptablesNativeFormat(
            table=table,
            path=file_path,
            directory=directory,
            counters=counters,
            ipv6=ipv6,
        )
    else:
        save_strategy = SaveIptablesYamlFormat(
            table=table,
            path=file_path,
            directory=directory,
            counters=counters,
            ipv6=ipv6,
        )

    save_strategy.execute()


class RestoreIptablesStrategy:
    table: Optional[str]
    path: Optional[Path]
    directory: Optional[Path]
    counters: bool
    ipv6: bool
    dry_run: bool

    def __init__(
        self,
        table: str = None,
        path: str = None,
        directory: str = None,
        counters: bool = False,
        ipv6: bool = False,
        dry_run: bool = False,
    ):
        self.table = table
        self.path = Path(path) if path else None
        self.directory = Path(directory) if directory else None
        self.counters = counters
        self.ipv6 = ipv6
        self.dry_run = dry_run

    def execute(self):
        raise NotImplementedError()


class RestoreIptablesNativeFormat(RestoreIptablesStrategy):
    def execute(self):
        save_file = IptablesSaveNativeFile(
            table=self.table, ipv6=self.ipv6, file=self.path
        )
        save_file.restore(dry_run=self.dry_run, counters=self.counters)


class RestoreIptablesYamlFormat(RestoreIptablesStrategy):
    def execute(self):
        if self.table:
            tables = [self.table]
        else:
            tables = Table4.ALL if not self.ipv6 else Table6.ALL

        for table in tables:
            save_file = IptablesSaveYamlFile(table=table, ipv6=self.ipv6)
            if self.directory:
                save_file.path = self.directory / save_file.path_not_exist_ok().name
            save_file.restore(dry_run=self.dry_run, counters=self.counters)


def restore(
    table: str = None,
    file_path: str = None,
    directory: str = None,
    format_: str = "iptables",
    counters: bool = False,
    ipv6: bool = False,
    dry_run: bool = False,
):
    strategy: RestoreIptablesStrategy
    if format_ == "iptables":
        strategy = RestoreIptablesNativeFormat(
            table=table,
            path=file_path,
            directory=directory,
            counters=counters,
            ipv6=ipv6,
            dry_run=dry_run,
        )
    else:
        strategy = RestoreIptablesYamlFormat(
            table=table,
            path=file_path,
            directory=directory,
            counters=counters,
            ipv6=ipv6,
            dry_run=dry_run,
        )

    strategy.execute()


class IptablesPrettyFormatter(Formatter):
    """Pretty format for iptables"""

    def format_table_header(self, table: Union[Table4, Table6], sep: str = "+") -> str:
        """Format the table header

        :param object table: An iptables table
        :param sep: Fill with separator
        :returns: the table surrounded by line filled with sep
        """

        version = "v6" if isinstance(table, Table6) else "v4"

        prefix = sep * 2
        string = table.name.upper()
        suffix = sep * (self.max_line_length - 5 - len(version) - len(string))

        table_header = f"{prefix} {string} {version} {suffix}"
        return table_header

    def format_chain_header(self, chain: iptc.Chain, sep: str = "=") -> str:
        """Format the chain header

        :param object chain: An iptables chain
        :param sep: Fill or separator
        :returns: the chain centered in a filled line with sep
        """
        policy: Optional[iptc.Policy] = chain.get_policy()
        policy_s = policy.name if policy else "None"

        if chain.is_builtin():
            packet_counter, byte_counter = chain.get_counters()
            packet_counter_s = self._format_counter(packet_counter, true_byte=False)
            byte_counter_s = self._format_counter(byte_counter)

            counter_output = (
                f"packets: {packet_counter_s:>4} bytes: {byte_counter_s:>4}"
            )

            string = f"{chain.name} ({policy_s:^6}) [{counter_output}]"
        else:
            string = f"{chain.name} ({policy_s:^6})"

        return self.center_string(string, sep)

    @staticmethod
    def _format_iprange(iprange: str) -> str:
        """Format an iprange to cidr notation

        :param iprange: An iprange as string
        :returns: iprange in cidr notation
        """

        cidr = nettools.iprange_to_cidr(iprange.lstrip("!"))
        return ("!" if iprange.startswith("!") else "") + cidr

    @staticmethod
    def _format_counter(counter: int, true_byte: bool = True) -> str:
        multi = 1024 if true_byte else 1000

        kilo = multi
        mega = multi * kilo
        giga = multi * mega

        if counter > giga:
            counter_s = str(int(counter / giga)) + "G"
        elif counter > mega:
            counter_s = str(int(counter / mega)) + "M"
        elif counter > kilo:
            counter_s = str(int(counter / kilo)) + "K"
        else:
            counter_s = str(counter)

        return counter_s

    def format_rule(
        self, rule: Union[iptc.Rule, iptc.Rule6], rule_number: int, sep: str = "-"
    ) -> str:
        """Format a rule

        :param object rule: An iptables rule
        :param rule_number: the number of the rule in the chain
        :param sep: Separator/Fill
        :returns: the formatted rule in 2 lines with a separating rule appended
        """

        # convert to short cidr notation
        src_net = IptablesPrettyFormatter._format_iprange(str(rule.src))
        dst_net = IptablesPrettyFormatter._format_iprange(str(rule.dst))

        parameters = rule.target.get_all_parameters()
        parameters_s = str(parameters) if parameters else ""

        output = (
            f"{rule_number:3}: {rule.in_interface!s:11} "
            f"{rule.out_interface!s:11} {rule.protocol:6} {src_net!s:18} "
            f"{dst_net!s:18} {rule.target.name:<6}{parameters_s!s}\n"
        )

        if rule.matches:
            matches = ""
            for match in rule.matches:
                matches += f"{match.name}{match.parameters!s},"

            output += f"     Matches: {matches.rstrip(',')}"

        output += "\n"

        packet_counter, byte_counter = rule.get_counters()
        packet_counter = self._format_counter(packet_counter, true_byte=False)
        byte_counter = self._format_counter(byte_counter)

        counter_output = f"packets: {packet_counter:>4} bytes: {byte_counter:>4}"
        output += (
            f"{sep * (self.max_line_length - 6 - len(counter_output))} "
            f"[{counter_output}] {sep * 2}"
        )
        return output


@user.needs_root
def to_string(
    tables: List[str] = None, version: str = "4", stream: bool = False
) -> str:
    """Formats tables, chains and rules. If stream is True print directly to
    stdout else collect all lines in 'formatter.output'

    :param tables: list of valid netfilter tables defaults to all netfilter tables
    :param version: either '6' for ip6tables, '4' for iptables or 'all' for both
    :param stream: If true stream to stdout instead of 'formatter.output'
    """

    output = []
    tables_to_print: List[IPTCTable] = []
    if version in ("4", "all"):
        if tables is None:
            tables = Table4.ALL
        for table_s in tables:
            tables_to_print.append(IPTCTable(Table4(table_s)))

    if version in ("6", "all"):
        if tables is None:
            tables = Table6.ALL
        for table_s in tables:
            tables_to_print.append(IPTCTable(Table6(table_s)))

    for table in tables_to_print:
        output.append(table.print(stream))

    return "".join(output)


def print_iptables(tables: List[str] = None, version: str = "4"):
    """Convenience function to print given tables in version to stdout"""
    to_string(tables, version, stream=True)
