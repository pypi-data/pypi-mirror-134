# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.servers
---------------

This module provides the functionality around servers.
"""

import abc
import re
from collections import UserList
from typing import List, Optional, Pattern

from connord import sqlite
from connord.areas import Area
from connord.categories import Category
from connord.config import Config
from connord.countries import Country
from connord.exceptions import LoadError, MalformedResourceError
from connord.features import Feature
from connord.formatter import Formatter
from connord.locations import Coordinates
from connord.parser.lexer import Lexer, Token
from connord.parser.parser import Environment, Expression, Parser
from connord.printer import Printer
from connord.resources import NordvpnServersURL, YamlFileResource
from connord.wrappers.nettools import ping_servers_parallel


# pylint: disable=too-many-instance-attributes
class Server:
    ip_address: str
    search_keywords: List[str]
    categories: List[Category]
    name: str
    fqdn: str
    country: Country
    load: int
    features: List[Feature]
    area: Area
    ping: float
    canonical_name: str
    number: int

    NUMBER_REGEX: Pattern = re.compile(r".*?([0-9]+)")

    def __init__(self, **kwargs):
        self.ip_address = kwargs["ip_address"]
        self.search_keywords = kwargs["search_keywords"]
        self.categories = [
            Category(description=c["name"]) for c in kwargs["categories"]
        ]
        self.name = kwargs["name"]
        self.fqdn = kwargs["domain"]
        self.country = Country(kwargs["country"], kwargs["flag"])
        self.load = kwargs["load"]
        self.features = [Feature(f) for f, bool_ in kwargs["features"].items() if bool_]

        coordinates: Coordinates = Coordinates(
            kwargs["location"]["lat"], kwargs["location"]["long"]
        )

        with sqlite.create_connection() as connection:
            area_name = sqlite.get_area(connection=connection, coordinates=coordinates)

        self.area = Area(name=area_name, coordinates=coordinates)
        self.ping = float("inf")

        canonical_name = self.fqdn.split(".", 1)[0]
        self.canonical_name = canonical_name
        self.number = self.number_from_canonical_name(canonical_name=canonical_name)

    def has_category(self, category: Category) -> bool:
        return category in self.categories

    def number_from_canonical_name(self, canonical_name: str):
        match = self.NUMBER_REGEX.search(canonical_name)
        if match:
            return int(match.group(1))

        raise ValueError(f"No number found in '{canonical_name}'")

    @staticmethod
    def from_resource(resource: YamlFileResource):
        return resource.read_unsafe()


class Servers(UserList):
    data: List[Server]

    def __init__(self, data: List[Server] = None, parent_domain: str = "nordvpn.com"):
        self.parent_domain = parent_domain

        if data is None:
            data = self.receive()

        super().__init__(data)

    @staticmethod
    def receive() -> List[Server]:
        resource = NordvpnServersURL()

        try:
            servers = resource.receive()
            try:
                resource.write(servers)
            except PermissionError:
                pass
        except MalformedResourceError:
            servers = resource.read()

        return [Server(**s) for s in servers]

    def get_server_by_domain(self, domain: str) -> Server:
        if domain.endswith(self.parent_domain):
            fqdn = domain
        else:
            fqdn = domain + "." + self.parent_domain

        for server in self:
            if server.fqdn == fqdn:
                return server

        raise ValueError(f"Domain not found: {domain!r}.")

    def filter_by_countries(self, countries_: Optional[List[Country]]):
        if not countries_:
            return

        self.data = [s for s in self if s.country in countries_]

    def filter_by_areas(self, areas_: Optional[List[Area]]):
        if not areas_:
            return

        self.data = [s for s in self if s.area in areas_]

    def filter_by_load(self, load: int, match: str):
        if not load:
            return

        if match == "equal":
            LoadFilter(self).apply(load)
        elif match == "min":
            MinLoadFilter(self).apply(load)
        elif match == "max":
            MaxLoadFilter(self).apply(load)
        else:
            raise ValueError("Illegal Value: " + match)

    def filter_netflix_servers(self):
        """Filter netflix servers"""

        config = Config()

        netflix_countries = config["connord"]["netflix_countries"]
        new_data: List[Server] = []
        for server in self:
            if server.country.flag in netflix_countries:
                new_data.append(server)

        self.data = sorted(new_data, key=lambda s: s.number, reverse=True)

    def filter_by_categories(self, categories_: Optional[List[Category]]):
        if not categories_:
            return

        new_data: List[Server] = []
        for server in self:
            for category in categories_:
                if category in server.categories:
                    new_data.append(server)
                    break

        self.data = new_data

    def filter_by_features(self, features_: Optional[List[Feature]]):
        if not features_:
            return

        new_data: List[Server] = []
        for server in self:
            for feature in features_:
                if feature in server.features:
                    new_data.append(server)
                    break

        self.data = new_data

    def filter_by_count(self, top: int):
        if not top:
            return

        self.data = self.data[:top]

    def filter_best(self):
        self.data = sorted(self, key=lambda s: s.load)[:10]
        self.ping()
        self.data = sorted(self, key=lambda s: s.ping)

    def filter_by_name(self, filters: str):
        if not filters:
            return

        tokens: List[Token] = Lexer(filters).lex()
        expression: Expression = Parser(tokens).parse()
        env: Environment = Environment()
        new_data: List[Server] = []
        for server in self:
            env.update_hostname(server.canonical_name)
            if expression.eval(env):
                new_data.append(server)

        self.data = new_data

    def filter(
        self,
        countries_: List[Country] = None,
        areas_: List[Area] = None,
        categories_: List[Category] = None,
        features_: List[Feature] = None,
        netflix: bool = False,
        # TODO recognize 0 load as valid value
        load_: int = 0,
        match: str = "max",
        top: int = 0,
        best: bool = False,
        filters: str = "",
    ):

        # keep the country filter first to sort out as many servers as possible at an
        # early stage.
        self.filter_by_countries(countries_)
        self.filter_by_areas(areas_)
        self.filter_by_categories(categories_)
        self.filter_by_features(features_)
        self.filter_by_load(load=load_, match=match)
        self.filter_by_count(top)
        self.filter_by_name(filters)

        if best:
            self.filter_best()

        if netflix:
            self.filter_netflix_servers()

    def ping(self):
        pinged = ping_servers_parallel([s.ip_address for s in self])
        for server in self:
            server.ping = pinged[server.ip_address]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        formatter = ServersPrettyFormatter()
        formatter.format_headline()

        count = 1
        for server in self:
            formatter.format_server(server, count)
            count += 1

        return formatter.get_output()

    def print(self):
        print(self.__repr__(), file=Printer())


class ServersPrettyFormatter(Formatter):
    """Class to format servers pretty."""

    def format_headline(self, sep: str = "="):
        """Return formatted headline"""

        ruler = self.format_ruler(sep)

        print(ruler, file=self)
        print(
            f"      {'Country':25}  {'Domain':6}  {'IP Address':15}  {'Load':>9}"
            f"  {'Ping':>6}",
            file=self,
        )

        print("      Type", file=self)
        print("      Features", file=self)
        print(ruler, file=self)

    def format_server(self, server: Server, count: int, sep: str = "-"):
        """Return pretty formatted server on two lines"""

        host = server.canonical_name
        country = server.country.name
        ip = server.ip_address
        load = server.load
        ping = server.ping

        categories_ = [category.name for category in server.categories]
        categories_string = ",".join(categories_)

        features_ = [feature.name for feature in server.features]
        features_string = ",".join(features_)

        print(
            f"{count:4d}: {country:25}  {host:6}  {ip:15}  {load:>9d}  {ping:6.2f}",
            file=self,
        )

        print(f"Type: {categories_string}", file=self)
        print(f"Feat: {features_string}", file=self)
        print(self.format_ruler(sep), file=self)


class Filter(metaclass=abc.ABCMeta):
    """
    Abstract class for different filters applied to servers.
    """

    __MAX = 100
    __MIN = 0

    def __init__(self, servers: Servers):
        """
        Initialise a Filter
        :param servers: A list of servers

        """
        if servers is None:
            raise ValueError("servers may not be None")

        self.servers = servers

    def verify_load(self, load: int) -> bool:
        """
        Verify if load is valid

        :load: Expects an integer between 0 and 100 inclusive
        :returns: True if load is valid
        :raises LoadError: If load is invalid
        """

        if load > self.__MAX or load < self.__MIN:
            raise LoadError("Load must be >= 0 and <= 100.")

        return True

    def apply(self, load: int):
        """
        Apply filters on servers

        :param load: Expects an integer between 0 and 100 inclusive
        :returns: Filtered list of servers
        """
        if not load:
            return

        if self.verify_load(load):
            self.servers.data = self.filter(load)

    @abc.abstractmethod
    def filter(self, load: int) -> List[Server]:
        """
        :param load: Expects an integer between 0 and 100 inclusive
        :returns: A list of filtered servers
        """
        raise NotImplementedError("To be implemented in subclasses")


class LoadFilter(Filter):
    """
    Filter to match load exactly
    """

    def filter(self, load: int) -> List[Server]:
        return [s for s in self.servers if s.load == load]


class MaxLoadFilter(Filter):
    """
    Filter to match maximum load
    """

    def filter(self, load: int) -> List[Server]:
        return [s for s in self.servers if s.load <= load]


class MinLoadFilter(Filter):
    """
    Filter to match minimum load
    """

    def filter(self, load: int) -> List[Server]:
        return [s for s in self.servers if s.load >= load]
