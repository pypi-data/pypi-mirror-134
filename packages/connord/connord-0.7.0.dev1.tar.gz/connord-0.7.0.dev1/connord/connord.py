# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.connord
---------------

This module provides a command line interface for connord.
"""

import errno
import os
import sys
import time

# Keep it first
from connord.config import Config
from connord.printer import Printer

config = Config()
for k, v in config["environment"].items():
    if k not in os.environ:
        os.environ[k] = v

# pylint: disable=wrong-import-position
from connord.wrappers.argparser import Arguments, Main

# pylint: disable=wrong-import-position
from connord import (
    resources,
    connect,
    iptables,
    listings,
    openvpn,
    update,
    user,
    version,
)


@user.needs_root
def process_list_ipt_cmd(arguments: Arguments) -> bool:
    version_ = arguments.get_ip_version()
    tables = arguments.get_iptables_tables()

    return listings.list_iptables(tables, version_)


def process_list_servers_cmd(arguments: Arguments) -> bool:
    countries_ = arguments.get_countries()
    areas_ = arguments.get_areas()
    categories_ = arguments.get_categories()
    features_ = arguments.get_features()
    load_, match = arguments.get_load_match()
    netflix = arguments.get("netflix")
    top = arguments.get("top")
    best = arguments.get("best")
    ping = arguments.get("ping")
    filters = arguments.get("filter")

    return listings.list_servers(
        countries_=countries_,
        areas_=areas_,
        categories_=categories_,
        features_=features_,
        netflix=netflix,
        load_=load_,
        match=match,
        top=top,
        best=best,
        ping=ping,
        filters=filters,
    )


# pylint: disable=too-many-return-statements
def process_list_cmd(arguments: Arguments) -> bool:
    """
    Process arguments when command is 'list'

    :param arguments: Command-line arguments
    :returns: True if processing was successful
    """

    resources.TemporaryDirectory().create(mode=0o755)

    if arguments.equals("list_sub", "iptables"):
        return process_list_ipt_cmd(arguments)
    if arguments.equals("list_sub", "servers"):
        return process_list_servers_cmd(arguments)
    if arguments.equals("list_sub", "countries"):
        return listings.list_countries()
    if arguments.equals("list_sub", "areas"):
        return listings.list_areas()
    if arguments.equals("list_sub", "features"):
        return listings.list_features()
    if arguments.equals("list_sub", "categories"):
        return listings.list_categories()

    # default: list all servers
    return listings.list_servers(
        countries_=None,
        areas_=None,
        categories_=None,
        features_=None,
        netflix=False,
        load_=100,
        match="max",
        top=0,
        best=False,
    )


@user.needs_root
def process_connect_cmd(arguments: Arguments) -> bool:
    """
    Process arguments for connect command

    :param arguments:
    :returns: True if processing was successful
    """
    server_option = arguments.get_server_option()
    countries_ = arguments.get_countries()
    areas_ = arguments.get_areas()
    features_ = arguments.get_features()
    categories_ = arguments.get_categories()
    netflix = arguments.get("netflix")
    load_, match = arguments.get_load_match()
    daemon = arguments.get("daemon", config["openvpn"]["daemon"])

    openvpn_options = arguments.get("openvpn_options")
    openvpn_ = openvpn_options[0] if openvpn_options else ""

    protocol = arguments.get_protocol()

    return connect.connect(
        server_option,
        countries_,
        areas_,
        features_,
        categories_,
        netflix,
        load_,
        match,
        daemon,
        openvpn_,
        protocol,
    )


@user.needs_root
def process_iptables_cmd(arguments: Arguments) -> bool:
    """Process 'iptables' command

    :param arguments:
    :returns: True if processing was successful
    """

    if arguments.equals("iptables_sub", "flush"):
        no_fallback = arguments.get("no_fallback", False)
        iptables.reset(not no_fallback)
        return True
    if arguments.equals("iptables_sub", "apply"):
        table: str = arguments.get("table")
        fallback: bool = arguments.get("fallback")
        ipv6: bool = arguments.get("ipv6")
        return iptables.apply(table, fallback=fallback, ipv6=ipv6)
    if arguments.equals("iptables_sub", "reload"):
        return iptables.reload()
    if arguments.equals("iptables_sub", "list"):
        return process_list_ipt_cmd(arguments)
    if arguments.equals("iptables_sub", "templates"):
        return iptables.list_templates()
    if arguments.equals("iptables_sub", "save"):
        file_: str = arguments.get("file")
        table = arguments.get("table")
        format_: str = arguments.get("format", "iptables")
        counters: bool = arguments.get("counters", False)
        directory: str = arguments.get("directory", config["iptables"]["templates_dir"])
        ipv6 = arguments.get("ipv6", False)
        return iptables.save(
            table=table,
            file_path=file_,
            format_=format_,
            counters=counters,
            directory=directory,
            ipv6=ipv6,
        )
    if arguments.equals("iptables_sub", "restore"):
        file_ = arguments.get("file")
        table = arguments.get("table")
        format_ = arguments.get("format", "iptables")
        counters = arguments.get("counters", False)
        directory = arguments.get("directory", config["iptables"]["templates_dir"])
        ipv6 = arguments.get("ipv6", False)
        dry_run: bool = arguments.get("dry_run", False)
        return iptables.restore(
            table=table,
            file_path=file_,
            format_=format_,
            counters=counters,
            directory=directory,
            ipv6=ipv6,
            dry_run=dry_run,
        )

    raise NotImplementedError("Not implemented")


@user.needs_root
def process_update_command(arguments: Arguments):
    if arguments.equals("update_sub", "ovpn"):
        update.update_ovpn_files()
    elif arguments.equals("update_sub", "database"):
        update.update_database()
    else:
        update.update()


@user.needs_root
def process_kill_cmd(arguments: Arguments) -> bool:
    """Process 'kill' command

    :param arguments: an Argument object
    """

    if arguments.get("all"):
        openvpn.kill_openvpn()
    else:
        ovpn_pid = resources.PidFileResource(name="openvpn.pid")
        openvpn.kill_openvpn(ovpn_pid.read())

    return True


def process_arguments(arguments: Arguments):
    if arguments.equals("command", "update"):
        return process_update_command(arguments)
    if arguments.equals("command", "version"):
        return version.print_version()
    if arguments.equals("command", "list"):
        return process_list_cmd(arguments)
    if arguments.equals("command", "connect"):
        return process_connect_cmd(arguments)
    if arguments.equals("command", "kill"):
        return process_kill_cmd(arguments)
    if arguments.equals("command", "iptables"):
        return process_iptables_cmd(arguments)

    # This should only happen when someone tampers with sys.argv
    raise NotImplementedError("Could not process command-line arguments.")


# This function has a high complexity score, but it's kept simple though
# pylint: disable=too-many-branches
def main():  # noqa: C901
    """Entry Point for the program. A first level argument processing method.
    All Exceptions that lead to an exit of the program are caught here.

    :raises: SystemExit either 0 or 1
    """

    if not sys.argv[1:]:
        sys.argv.extend(["-h"])

    arguments = Main().parse(argv=sys.argv[1:])

    printer = Printer(
        verbose=arguments.get("verbose", config["connord"]["verbose"]),
        quiet=arguments.get("quiet"),
    )

    try:
        if process_arguments(arguments):
            sys.exit(0)
    except PermissionError as error:
        printer.error(
            f"{error!s}: Permission Denied: You may need to run "
            f"connord {arguments.get('command')} as root"
        )
        raise
    except IOError as error:
        # Don't handle broken pipe
        if error.errno != errno.EPIPE:
            raise
    except KeyboardInterrupt:
        time.sleep(0.5)
        sys.exit(0)

    sys.exit(1)
