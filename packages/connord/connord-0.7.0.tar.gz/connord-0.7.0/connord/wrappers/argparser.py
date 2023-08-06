# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.wrappers.argparser
--------------------------

This module is built around python's argparse module to parse command line arguments.
"""

import argparse
import re
from pathlib import Path
from typing import Any, List, Optional, Tuple

from connord import (
    areas,
    categories,
    countries,
    exceptions,
    features,
    iptables,
    sqlite,
)
from connord.areas import Area
from connord.categories import Category
from connord.config import Config
from connord.countries import Country
from connord.exceptions import ConnordError
from connord.features import Feature
from connord.locations import Coordinates


class DomainType:
    PATTERN = re.compile(r"(?P<country_code>[a-z]{2})(?P<number>[0-9]+)(.netflix.com)?")

    def __call__(self, value: str) -> str:
        match = self.PATTERN.match(value)
        if not match:
            raise argparse.ArgumentTypeError(
                f"'{value}' is not a valid domain. Expected format is"
                f" {{country_code}}{{number}}[.netflix.com]"
            )

        country_code = match.groupdict()["country_code"]
        CountryType().__call__(country_code)
        return value


class CountryType:
    def __call__(self, value: str) -> str:
        try:
            countries.verify_countries([value])
        except exceptions.CountryError:
            raise argparse.ArgumentTypeError(f"'{value}' is an unrecognized country.")
        return value


class AreaType:
    def __call__(self, value: str) -> str:
        try:
            areas.verify_areas([value])
        except exceptions.AreaError as error:
            raise argparse.ArgumentTypeError(str(error))

        # TODO return Area instead of str
        return value


class CategoryType:
    def __call__(self, value: str) -> str:
        try:
            categories.verify_categories([value])
        except exceptions.CategoriesError:
            raise argparse.ArgumentTypeError(
                f"'{value}' is an unrecognized categories."
            )

        return value


class FeatureType:
    def __call__(self, value: str) -> str:
        try:
            features.verify_features([value])
        except exceptions.FeatureError:
            raise argparse.ArgumentTypeError(f"'{value}' is an unrecognized feature.")

        return value


class LoadType:
    def __call__(self, value: str) -> int:
        try:
            int_value = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"'{value}' must be an integer between 0 and 100."
            )

        if int_value < 0 or int_value > 100:
            raise argparse.ArgumentTypeError(
                f"'{value}' must be a value between 0 and 100."
            )

        return int_value


class TopType:
    def __call__(self, value: str) -> int:
        try:
            int_value = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"'{value}' must be a positive integer greater than 0."
            )

        if int_value <= 0:
            raise argparse.ArgumentTypeError(
                f"'{value}' must be a positive integer greater than 0."
            )

        return int_value


class TableType:
    def __call__(self, value: str) -> str:
        if iptables.verify_table(value):
            return value

        raise argparse.ArgumentTypeError(
            f"'{value}' is not a valid table name. Consult man iptables for details."
        )


class FileType:
    def __call__(self, value: str) -> Path:
        return Path(value)


class ArgumentsError(ConnordError):
    pass


class Arguments:
    def __init__(self, args: argparse.Namespace):
        self.namespace = args

    def equals(self, argument: str, other: str) -> bool:
        return self.get(argument) == other

    def get(self, argument: str, default: Any = None) -> Any:
        return getattr(self.namespace, argument, default)

    def get_load_match(self) -> Tuple[int, str]:
        config = Config()
        if self.namespace.max_load:
            load_: int = self.namespace.max_load
            match: str = "max"
        elif self.namespace.min_load:
            load_ = self.namespace.min_load
            match = "min"
        elif self.namespace.load:
            load_ = self.namespace.load
            match = "equal"
        else:  # apply defaults
            load_ = config["connord"].get("load", 100)
            match = config["connord"].get("match", "max")

        return load_, match

    def get_ip_version(self) -> str:
        config = Config()
        if self.namespace.v4 and self.namespace.v6:
            version_ = "all"
        elif self.namespace.v4:
            version_ = "4"
        elif self.namespace.v6:
            version_ = "6"
        else:
            version_ = config["iptables"]["default_version"]

        return version_

    def get_iptables_tables(self) -> Optional[List[str]]:
        config = Config()
        if self.namespace.all:
            tables: Optional[List[str]] = None
        elif self.namespace.table:
            tables = self.namespace.table
        else:
            tables = config["iptables"]["default_tables"]

        return tables

    def get_countries(self) -> List[Country]:
        if not self.namespace.country:
            return []

        return [Country(flag=c) for c in self.namespace.country]

    def get_areas(self) -> List[Area]:
        if not self.namespace.area:
            return []

        areas_: List[Area] = []
        with sqlite.create_connection() as connection:
            for area in self.namespace.area:
                # areas_ should only contain unambiguous area prefixes here
                # so taking just the first result is fine
                result = sqlite.get_area_by_prefix(connection, area)[0]
                city: str = result["city"]
                latitude: str = result["latitude"]
                longitude: str = result["longitude"]
                areas_.append(
                    Area(
                        city,
                        Coordinates(latitude=latitude, longitude=longitude),
                    )
                )

        return areas_

    def get_categories(self) -> List[Category]:
        config = Config()
        categories_strings: List[str] = (
            self.namespace.category
            if self.namespace.category
            else config["connord"]["default_categories"]
        )

        return [Category(name=c) for c in categories_strings]

    def get_features(self) -> List[Feature]:
        if not self.namespace.feature:
            return []

        return [Feature(f) for f in self.namespace.feature]

    def get_server_option(self) -> str:
        config = Config()
        if self.namespace.server:
            server = self.namespace.server
        elif self.namespace.best:
            server = "best"
        else:  # apply default
            server = config["connord"]["default_server"]

        return server

    def get_protocol(self) -> str:
        config = Config()
        if self.namespace.udp:
            protocol: str = "udp"
        elif self.namespace.tcp:
            protocol = "tcp"
        else:  # apply default
            protocol = config["connord"]["protocol"]

        return protocol


class AParserError(Exception):
    pass


class AParser:
    parser: argparse.ArgumentParser
    subparsers: Any
    # Organized as Lifo
    mutually_exclusive_groups: List[Any]
    help: str

    def __init__(self, **kwargs):
        self.help = kwargs.pop("help", "")
        self.parser = argparse.ArgumentParser(**kwargs)
        self.subparsers = None
        self.mutually_exclusive_groups = []
        self.make()

    def make(self):
        # to be overwritten in subclasses if necessary
        pass

    def description(self):
        return self.parser.description

    def parse(self, argv: List[str]) -> Arguments:
        args = self.parser.parse_args(argv)
        return Arguments(args)

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def add_mutually_exclusive_group(self, **kwargs):
        group = self.parser.add_mutually_exclusive_group(**kwargs)
        self.mutually_exclusive_groups.append(group)

    def get_mutually_exclusive_group(self):
        try:
            return self.mutually_exclusive_groups[-1]
        except IndexError:
            raise AParserError("No mutually exclusive group found.") from IndexError

    def add_mutually_exclusive_argument(self, *args, **kwargs):
        self.get_mutually_exclusive_group().add_argument(*args, **kwargs)

    def add_subparsers(self, **kwargs):
        self.subparsers = self.parser.add_subparsers(**kwargs)

    def add_subparser(
        self,
        name,
        subparser: "AParser",
        parents: Optional[List["AParser"]] = None,
        **kwargs,
    ):
        description = kwargs.pop("description", subparser.description())
        parser_parents = (
            [subparser.parser]
            if not parents
            else [subparser.parser] + [s.parser for s in parents]
        )
        help_ = kwargs.pop("help", None)

        self.subparsers.add_parser(
            name,
            add_help=False,
            parents=parser_parents,
            description=description,
            help=help_,
            **kwargs,
        )


class Update(AParser):
    class UpdateDatabase(AParser):
        def __init__(self):
            description = (
                "Update the location database, needed to resolve store resolved"
                "coordinates of locations."
            )
            super().__init__(description=description)

    class UpdateOVPN(AParser):
        def __init__(self):
            description = (
                "Update the openvpn configuration files, needed to connect to a NordVPN"
                " server."
            )
            super().__init__(description=description)

    def __init__(self):
        description = (
            "Update NordVPN configuration files used by openvpn and the location"
            " database. The latter is"
            " used internally to store locations resolved from coordinates with names"
            " like cities, street names etc. This kind information can be seen for"
            " example with the"
            " 'connord list areas' command."
        )
        super().__init__(description=description)

    def make(self):
        self.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="Force an update if an update was refused by connord.",
        )
        self.add_subparsers(dest="update_sub")
        self.add_subparser(
            "database", self.UpdateDatabase(), help="Update the database."
        )
        self.add_subparser(
            "ovpn", self.UpdateDatabase(), help="Update openvpn configuration files."
        )


class ListIptables(AParser):
    def __init__(self):
        description = (
            "List iptables rules in a format close to the yaml format of"
            " iptables rules files what makes it easier to write rules in yaml format"
            " if you're doing it for the first time. Furthermore it is capable to list"
            " both (ipv4 and ipv6) rules types and all tables with one command, what"
            " the native iptables command can't do."
        )
        super().__init__(description=description)

    def make(self):
        self.add_argument(
            "-4",
            dest="v4",
            action="store_true",
            help="List ipv4 rules. This is the default behaviour, if no -4 or -6 option"
            " is given on the command line. It can be used"
            " together with the -6 option to list both iptables rules types.",
        )
        self.add_argument("-6", dest="v6", action="store_true", help="List ipv6 rules.")
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "-t",
            "--table",
            type=TableType(),
            action="append",
            help="List TABLE, where table is a valid iptables table name like 'filter'"
            " or 'raw' etc. May be specified multiple times. (default: filter)",
        )
        self.add_mutually_exclusive_argument(
            "-a", "--all", action="store_true", help="List all tables."
        )


class ListServers(AParser):
    def __init__(self):
        description = (
            "List servers. The output can be filtered with one or more of the specified"
            " arguments. This can be useful if you want to figure out to which server"
            " to connect to if not using connord's best-match-algorithm. Furthermore"
            " it provides a lot of useful information about NordVPN servers in general."
        )
        super().__init__(description=description)

    def make(self):
        self.add_argument(
            "-c",
            "--country",
            action="append",
            type=CountryType(),
            help="Select a specific country where the server is located. Default"
            " behaviour is to show all countries. For a list of all countries where "
            " NordVPN servers can be found consult the output of 'connord list"
            " countries'. This option may be specified multiple"
            " times.",
        )
        self.add_argument(
            "-a",
            "--area",
            action="append",
            type=AreaType(),
            help="Select a specific area. May be specified multiple times. For a list"
            " of all possible areas consult the output of the 'connord list areas'"
            " command.",
        )
        self.add_argument(
            "-f",
            "--feature",
            action="append",
            type=FeatureType(),
            help="Select servers with a specific feature."
            " For a list of all possible features consult the"
            " output of the 'connord list features' command. (May be specified multiple"
            " times)",
        )
        self.add_argument(
            "-t",
            "--category",
            action="append",
            type=CategoryType(),
            help="Select servers with a specific category. For a list of all possible"
            " categories consult the output of the 'connord list categories'"
            " command. (May be specified multiple"
            " times)",
        )
        self.add_argument(
            "--netflix",
            action="store_true",
            help="Filter out servers known to work best with Netflix. (default: false)",
        )
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "--max-load",
            dest="max_load",
            type=LoadType(),
            help="Filter servers by their current (work)load where the argument to this"
            " option"
            " specifies the maximum acceptable load. Usually a lower load is considered"
            " to be 'better'.",
        )
        self.add_mutually_exclusive_argument(
            "--min-load",
            dest="min_load",
            type=LoadType(),
            help="Like --max-load but specify the minimum acceptable load.",
        )
        self.add_mutually_exclusive_argument(
            "--load",
            type=LoadType(),
            help="Filter servers where the load given by"
            " this argument must match exactly the load of the server.",
        )
        self.add_argument(
            "--top",
            type=TopType(),
            help="Show only the top count resulting servers. Top"
            " doesn't mean top quality here but simply the amount of servers to show.",
        )
        self.add_argument(
            "--best",
            action="store_true",
            help="Filter best servers determined by a best-server-for-your-location "
            "algorithm.",
        )
        self.add_argument(
            "--ping",
            action="store_true",
            help="Pings every server found so far and show the ping of each"
            " server. Use this option with care since pinging 5000 servers may"
            " take a while. Therefore, the ping option is always applied last after"
            " all other filters.",
        )
        self.add_argument(
            "--filter",
            type=str,
            help="Describe a user defined filter. Currently it is only possible to"
            " filter"
            " servers by their domain (host) name. Maybe it's best to start with an"
            " example:\n--filter '<us1000' shows all servers which are smaller"
            " than 'us1000'. Smaller means the country code part is compared and then"
            " the"
            " number. This usually includes servers from other countries which have got"
            " a lexically smaller country code like 'us', for example ca (Canada)."
            " Usually the wanted effect is to show only servers from the country"
            " specified with the country code and the number is less (or greater ...)"
            " than the one specified in the filter. To get the wanted result"
            " specify"
            " the --country us option together with the --filter option"
            " . (You also could achieve something similar with"
            " --filter '>us0, <us1000'. For more information about logical"
            " operators see below.)"
            " Other possible"
            " comparison operators are: <= < == > >=. Comparisons can be logically"
            " combined with the logical operators for AND ',' and OR '|'. To stay"
            " to the practice showing examples: To filter servers which hostnames are"
            " greater or equal to us900 AND smaller than us1000 the filter option"
            " looks like"
            " this: --filter '>=us900, <us1000'. (Any whitespace between expressions"
            " is ignored). To show"
            " servers with hostnames smaller than us100 OR greater than us1000"
            " --filter '<us100 | >us1000'. It's also possible to group logical"
            " operations"
            " with parentheses to be able to construct even more complex filters:"
            " --filter '(<us100 | >us1000) , (>us500 , <us600)'."
            " Like shown above enclose the filter in"
            " apostrophes"
            " to avoid shell expansion.",
        )


class ListMain(AParser):
    class ListCountries(AParser):
        def __init__(self):
            description = "List all countries with NordVPN servers."
            super().__init__(description=description)

    class ListAreas(AParser):
        def __init__(self):
            description = "List all areas with NordVPN servers."
            super().__init__(description=description)

    class ListFeatures(AParser):
        def __init__(self):
            description = "List all features offered by NordVPN servers."
            super().__init__(description=description)

    class ListCategories(AParser):
        def __init__(self):
            description = "List all categories offered by NordVPN servers."
            super().__init__(description=description)

    def __init__(self):
        description = (
            "The 'list' command provides further commands to show useful information"
            " around NordVPN servers like country codes, server features,"
            " the full list of NordVPN servers etc. It is also possible to list"
            " iptables rules."
        )
        super().__init__(description=description)

    def make(self):
        self.add_subparsers(dest="list_sub")
        self.add_subparser(
            "iptables",
            ListIptables(),
            help=(
                "List iptables rules. This is the same command like"
                " 'connord iptables list'."
            ),
        )
        self.add_subparser(
            "countries",
            self.ListCountries(),
            help="List all countries with NordVPN servers.",
        )
        self.add_subparser(
            "areas",
            self.ListAreas(),
            help="List all areas/cities with NordVPN servers.",
        )
        self.add_subparser(
            "features",
            self.ListFeatures(),
            help="List all possible features of NordVPN servers.",
        )
        self.add_subparser(
            "categories",
            self.ListCategories(),
            help="List all possible categories of NordVPN servers.",
        )
        self.add_subparser(
            "servers",
            ListServers(),
            help="List servers filtered by specified arguments.",
        )


# TODO --filter should be available too
class Connect(AParser):
    def __init__(self):
        description = (
            "Connect to NordVPN servers. The servers used by the"
            " best-algorithm can be filtered beforehand with one or more of the options"
            " below."
            " These options offer, besides some additional ones, pretty much the same"
            " functionality found in"
            " the 'connord list servers' command."
        )
        super().__init__(description=description)

    def make(self):
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "-s",
            "--server",
            type=DomainType(),
            help="Connect to a specific server. Only the options -d, -o, --udp and"
            " --tcp have an effect and there won't happen any further filtering.",
        )
        self.add_argument(
            "--best",
            action="store_true",
            help="Filter best servers determined by a best-server-for-your-location"
            " algorithm. This is the default behaviour if this option is not given on"
            " the command line.",
        )
        self.add_argument(
            "-c",
            "--country",
            action="append",
            type=CountryType(),
            help="Limit servers to a specific country. May be specified multiple"
            " times. See 'connord list countries' for a list of possible countries.",
        )
        self.add_argument(
            "-a",
            "--area",
            action="append",
            type=AreaType(),
            help="Limit servers to a specific area. May be specified multiple times."
            "See 'connord list areas' for all possible areas.",
        )
        self.add_argument(
            "-f",
            "--feature",
            action="append",
            type=FeatureType(),
            help="Select servers with a specific feature. May be"
            " specified multiple times. See 'connord list features' for all supported"
            " features",
        )
        self.add_argument(
            "-t",
            "--category",
            action="append",
            type=CategoryType(),
            help="Select servers with a specific category. May be specified multiple"
            " times. See 'connord list categories' for a full list of categories.",
        )
        self.add_argument(
            "--netflix",
            action="store_true",
            help="Select servers known to work best with Netflix.",
        )
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "--max-load",
            dest="max_load",
            type=LoadType(),
            help="Filter servers by maximum load.",
        )
        self.add_mutually_exclusive_argument(
            "--min-load",
            dest="min_load",
            type=LoadType(),
            help="Filter servers by minimum load.",
        )
        self.add_mutually_exclusive_argument(
            "--load", type=LoadType(), help="Filter servers by exact load match."
        )
        self.add_argument(
            "-d", "--daemon", action="store_true", help="Start in daemon mode."
        )
        self.add_argument(
            "-o",
            "--openvpn",
            dest="openvpn_options",
            type=str,
            nargs=1,
            help="Options to pass to openvpn. Must be as single string.",
        )
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "--udp",
            action="store_true",
            help="Use UDP protocol what implies using"
            " port 1194. This is the default behaviour.",
        )
        self.add_mutually_exclusive_argument(
            "--tcp",
            action="store_true",
            help="Use the protocol what implies using port 443.",
        )


class Kill(AParser):
    def __init__(self):
        description = (
            "Kill the openvpn process spawned by connord or all openvpn "
            "processes with --all"
        )
        super().__init__(description=description)

    def make(self):
        self.add_argument(
            "-a", "--all", action="store_true", help="Kill all openvpn processes."
        )


class Iptables(AParser):
    class Reload(AParser):
        def __init__(self):
            description = (
                "Reload iptables 'rules' configuration when connected to "
                "NordVPN or else the 'fallback' configuration. Especially useful after "
                "editing a configuration file and you wish to apply it to your running "
                "iptables rules."
            )
            super().__init__(description=description)

    class Flush(AParser):
        def __init__(self):
            description = (
                "Flush iptables to fallback configuration or with --no-fallback to no "
                "rules at all and apply ACCEPT policy to builtin chains."
            )
            super().__init__(description=description)

        # TODO add -4 , -6 selecting iptables version, maybe an --all flag for both
        def make(self):
            self.add_argument(
                "--no-fallback",
                dest="no_fallback",
                action="store_true",
                help="Flush tables ignoring fallback files.",
            )

    class Apply(AParser):
        def __init__(self):
            description = (
                "Apply iptables rules defined in 'rules' or 'fallback' "
                "configuration files for a specific 'table'."
            )
            super().__init__(description=description)

        def make(self):
            self.add_argument(
                "table", type=TableType(), help="Apply iptables rules for 'table'."
            )
            self.add_argument(
                "-f",
                "--fallback",
                action="store_true",
                help="Apply fallback instead of the rules configuration.",
            )
            self.add_argument(
                "-6",
                dest="ipv6",
                action="store_true",
                help="Apply the ipv6 configuration.",
            )

    class ListTemplates(AParser):
        def __init__(self):
            description = "List iptables jinja templates."
            super().__init__(description=description)

    class Save(AParser):
        def __init__(self):
            description = (
                "Save iptables rules in yaml or native, iptables-restore"
                " compatible, format. This command produces files which are usable"
                " by the 'connord iptables restore' command."
            )
            super().__init__(description=description)

        def make(self):
            self.add_argument(
                "-f",
                "--file",
                type=FileType(),
                help="Specify a filename to write the output to. If not given, the save"
                " command will write to the iptables[6].save file within the target"
                " directory"
                " (if --format is iptables)."
                " If --format"
                " is yaml then the tables are saved to TABLE[6].save files where"
                " TABLE is an iptables table name.",
            )
            self.add_argument(
                "-t",
                "--table",
                type=TableType(),
                help="Restrict the output to only one table. If not specified, output"
                " includes all available tables.",
            )
            self.add_argument(
                "-o",
                "--format",
                type=str,
                choices=["iptables", "yaml"],
                help="Save the rules in 'yaml' or 'iptables' format."
                " (default: iptables)",
            )
            self.add_argument(
                "-c",
                "--counters",
                action="store_true",
                help="Save the rules with counters. (default: false)",
            )
            self.add_argument(
                "-d",
                "--directory",
                type=FileType(),
                help="Save the rules into this"
                " directory. (default [config.yml]: iptables.templates_dir)",
            )
            self.add_argument(
                "-6",
                "--ipv6",
                action="store_true",
                help="Save ipv6 tables. Default behaviour is to save ipv4 tables.",
            )

    class Restore(AParser):
        def __init__(self):
            description = (
                "Restore iptables rules. This command acts as counterpart to"
                " the connord iptables save command. Files saved with the iptables save"
                " can be restored with this command."
            )
            super().__init__(description=description)

        def make(self):
            self.add_argument(
                "-f",
                "--file",
                type=FileType(),
                help="Restore ipv4 and ipv6 tables from the specified file. The format"
                " (See --format) must match the file content or the command fails."
                " (default: if --format is iptables: ip[6]tables.save | --format"
                " is yaml: TABLE[6].save files where TABLE must be valid table"
                " names)",
            )
            self.add_argument(
                "-t",
                "--table",
                type=TableType(),
                help="Restore only the named table."
                " Default behaviour is to restore all tables found in"
                " ip[6]tables.save (if --format is iptables and --file is not"
                " specified), or"
                " (if --format is yaml) all tables found in .save files"
                " within the target directory (may be specified with --directory)",
            )
            self.add_argument(
                "-o",
                "--format",
                type=str,
                choices=["iptables", "yaml"],
                help="Restore the rules from files in 'yaml' or 'iptables' format."
                " (default: iptables)",
            )
            self.add_argument(
                "-c",
                "--counters",
                action="store_true",
                help="Restore with counters for packets and bytes. (default: false)",
            )
            self.add_argument(
                "-d",
                "--directory",
                type=FileType(),
                help="Restore the rules from within this"
                " directory. (default [config.yml]: iptables.templates_dir)",
            )
            self.add_argument(
                "-6",
                "--ipv6",
                action="store_true",
                help="Restore ipv6 tables. Default behaviour is to restore ipv4"
                " tables.",
            )
            self.add_argument(
                "-n",
                "--dry-run",
                action="store_true",
                help="Only parse and construct the ruleset, but do not commit it. Can"
                " only be used together with --format iptables.",
            )

    def __init__(self):
        description = (
            "Manage the connord iptables configuration in detail with this command."
            " See the "
            " descriptions and help of the sub commands for further information."
        )
        super().__init__(description=description)

    def make(self):
        self.add_subparsers(dest="iptables_sub")
        self.add_subparser("list", ListIptables(), help="List iptables rules.")
        self.add_subparser(
            "templates",
            self.ListTemplates(),
            help="List paths of iptables templates found by connord.",
        )
        self.add_subparser("reload", self.Reload(), help="Reload iptables rules.")
        self.add_subparser("flush", self.Flush(), help="Flush iptables rules.")
        self.add_subparser(
            "apply", self.Apply(), help="Apply iptables rules per 'table'."
        )
        self.add_subparser("save", self.Save(), help="Save iptables rules.")
        self.add_subparser(
            "restore",
            self.Restore(),
            help="Restore iptables rules saved with the save command.",
        )


class Version(AParser):
    pass


class Main(AParser):
    def __init__(self):
        description = (
            "Connord connects you to NordVPN servers using openvpn and iptables in the"
            " toolchain. Try a quickstart with 'connord update', what downloads and"
            " updates"
            " the openvpn configuration files. 'connord connect' connects you to the"
            " best server available from your location. Both commands need to be run as"
            " root user. Try the --help option with subcommands to find out more or"
            " read"
            " the official documentation at https://github.com/MaelStor/connord."
        )
        epilog = "Run a command with -h or --help for more information."
        super().__init__(description=description, epilog=epilog)

    def make(self):
        self.add_mutually_exclusive_group()
        self.add_mutually_exclusive_argument(
            "-q", "--quiet", action="store_true", help="Suppress error messages."
        )
        self.add_mutually_exclusive_argument(
            "-v", "--verbose", action="store_true", help="Show what's going."
        )
        self.add_subparsers(dest="command")
        self.add_subparser("update", Update(), help="Update everything")
        subparser = ListMain()
        self.add_subparser("list", ListMain(), help=subparser.help)
        self.add_subparser("connect", Connect(), help="Connect to a server.")
        self.add_subparser("kill", Kill(), help="Kill the openvpn process.")
        self.add_subparser("iptables", Iptables(), help="Manage Iptables")
        self.add_subparser("version", Version(), help="Show version")
