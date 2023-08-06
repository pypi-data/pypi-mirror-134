# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.listings
----------------

This module is an interface to provide high level functions for all kind of lists
presented to the user.
"""

from typing import List, Optional

from connord import areas, categories, countries, features, iptables, servers
from connord.areas import Area
from connord.categories import Category
from connord.countries import Country
from connord.features import Feature


def list_iptables(tables: Optional[List[str]], version: str) -> bool:
    """Prints iptables to stdout

    :param tables: list of tables like ['filter']
    :param version: '6' or '4' or 'all'
    :returns: True
    """
    iptables.print_iptables(tables, version)
    return True


def list_countries() -> bool:
    countries.print_countries()
    return True


def list_areas() -> bool:
    areas.print_areas()
    return True


def list_features() -> bool:
    features.print_features()
    return True


def list_categories() -> bool:
    categories.print_categories()
    return True


def list_servers(
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
    ping: bool = False,
    filters: str = "",
) -> bool:
    servers_ = servers.Servers()
    servers_.filter(
        countries_=countries_,
        areas_=areas_,
        categories_=categories_,
        features_=features_,
        netflix=netflix,
        load_=load_,
        match=match,
        top=top,
        best=best,
        filters=filters,
    )

    if ping:
        servers_.ping()

    servers_.print()
    return True
