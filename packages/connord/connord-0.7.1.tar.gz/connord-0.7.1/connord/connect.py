# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.connect
---------------

This module provides high level functions to connect to a server via openvpn.
"""

from math import inf
from typing import List, Optional

from connord import resources, servers, sqlite
from connord.areas import Area
from connord.categories import Category
from connord.config import Config
from connord.countries import Country
from connord.exceptions import ConnectError
from connord.features import Feature
from connord.openvpn import run_openvpn
from connord.printer import Printer
from connord.servers import Server
from connord.wrappers import nettools

WARNING_MESSAGE = """WARNING: Connection to an obfuscated server
This may fail if not configured properly.
Are you sure you want to continue?"""


def connect_to_specific_server(
    domain: str, openvpn: str, daemon: bool, protocol: str
) -> bool:
    """Connect to a specific server

    :param domain: list of domains which holds one value like gb111
    :param openvpn: string of options to pass through to openvpn
    :param daemon: True if the openvpn shall be run in daemon mode
    :param protocol: may be one of 'udp' or 'tcp'
    :returns: True if openvpn was run successfully
    """

    servers_ = servers.Servers()
    server = servers_.get_server_by_domain(domain)

    server.ping = nettools.ping(server.ip_address)[server.ip_address]

    return try_connect(server, 1, openvpn, daemon, protocol, 1)


def try_connect(
    server: Server,
    attempt: int,
    openvpn_cmdline: str,
    daemon: bool,
    protocol,
    max_retries: Optional[int] = None,
) -> bool:
    printer = Printer()

    if server.ping != inf:
        if max_retries is not None and attempt > max_retries:
            raise ConnectError("Maximum retries reached.")

        printer.info(
            f"({attempt}/{max_retries if max_retries else inf!s}) Trying to connect to"
            f" {server.fqdn}: Ping {server.ping} ms | Load {server.load} %"
        )

        if server.has_category(Category(name="obfuscated")) and not printer.yes_no(
            WARNING_MESSAGE
        ):
            return False

        with sqlite.create_connection() as connection:
            map_ = sqlite.get_map(connection, server.area.coordinates)
            if map_:
                printer.info(map_)

        return run_openvpn(server, openvpn_cmdline, daemon, protocol)

    raise ConnectError("No server left with a valid ping.")


# pylint: disable=too-many-locals
def connect(
    domain: str,
    countries_: List[Country],
    areas_: List[Area],
    features_: List[Feature],
    categories_: List[Category],
    netflix: bool,
    load_: int,
    match: str,
    daemon: bool,
    openvpn: str,
    protocol: str,
) -> bool:
    """High-level function to connect to an openvpn server. Filters servers and
    tries to connect to an openvpn server 'max_retries' times or else raise an
    exception.

    :param domain: Domain like de910 or best
    :param countries_: list of countries
    :param areas_: list of areas
    :param features_: list of features
    :param categories_: list of categories
    :param netflix: True to filter netflix optimized servers
    :param load_: depending on match, filter by max, min or equal load servers
    :param match: may be 'max', 'min' or 'equal'
    :param daemon: True if openvpn shall run in daemon mode
    :param openvpn: options to pass through to openvpn as string
    :param protocol: may be 'udp' or 'tcp'
    :returns: True if running openvpn was successful
    :raises: ConnectError
    """

    resources.NordvpnConfigurationRootDirectory().create(mode=0o755)
    resources.NordvpnCredentialsFile().create(mode=0o600)
    resources.TemporaryDirectory().create(mode=0o755)
    resources.StatsDirectory().create(mode=0o750)

    config = Config()

    if "best" != domain:
        return connect_to_specific_server(domain, openvpn, daemon, protocol)

    servers_ = servers.Servers()
    servers_.filter(
        countries_=countries_,
        areas_=areas_,
        features_=features_,
        categories_=categories_,
        netflix=netflix,
        load_=load_,
        match=match,
        best=True,
    )

    max_retries: Optional[int] = config["connord"]["maximum_connection_retries"]
    for attempt, server in enumerate(servers_, start=1):
        if try_connect(
            server, attempt, openvpn, daemon, protocol, max_retries=max_retries
        ):
            return True

    raise ConnectError("No server found to establish a connection.")
