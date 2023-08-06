# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.categories
------------------

This module provides classes and functions managing server categories.
"""
from typing import List

from connord.exceptions import CategoriesError
from connord.formatter import Formatter

# TODO move into database
CATEGORIES = {
    "double": "Double VPN",
    "dedicated": "Dedicated IP",
    "standard": "Standard VPN servers",
    "p2p": "P2P",
    "obfuscated": "Obfuscated Servers",
    "onion": "Onion Over VPN",
}


class Category:
    def __init__(self, name: str = "", description: str = ""):
        if not name and not description:
            raise ValueError("name and description may not be empty.")

        if name and not description:
            self.name = name
            self.description: str = CATEGORIES[name]
        elif not name and description:
            self.description = description
            for n, d in CATEGORIES.items():
                if d == description:
                    self.name = n
                    break
        else:
            self.name = name
            self.description = description

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Category):
            return self.name == other.name

        return False

    def __str__(self):
        return f"Category: {self.name}"

    def __repr__(self):
        return f"Category: {self.name}, {self.description}"


def verify_categories(categories: List[str]) -> bool:
    """Verify if categories is are valid

    :categories: a list of category names
    :raises: CategoriesError if there are invalid categories in categories
    :returns: True if all categories are valid
    """

    wrong_categories = []
    for server_type in categories:
        if server_type not in CATEGORIES:
            wrong_categories.append(server_type)

    if wrong_categories:
        raise CategoriesError(f"Wrong server categories: {wrong_categories!s}")

    return True


def verify_categories_description(descriptions: List[str]) -> bool:
    """Verify if categories descriptions are valid

    :description: a list of descriptions
    :raises: CategoriesError if there are invalid categories in categories
    :returns: True if all type descriptions are valid
    """

    wrong_categories = [
        desc for desc in descriptions if desc not in CATEGORIES.values()
    ]

    if wrong_categories:
        raise CategoriesError(f"Wrong category descriptions: {wrong_categories!s}")

    return True


class CategoriesPrettyFormatter(Formatter):
    """Format type in pretty format"""

    def format_headline(self, sep: str = "=") -> str:
        """Format headline

        :param sep: the fill character
        :returns: centered string
        """

        categories_header = "Categories"
        return self.center_string(categories_header, sep)

    @staticmethod
    def format_category(category: str, description: str) -> str:
        """Format a category

        :param category: the category
        :param description: the description
        :returns: the formatted category as string
        """

        return f"  {category:26}{description}"


def to_string(stream: bool = False) -> str:
    """Gather all categories in a printable string

    :param stream: If True print to stdout else print to 'formatter.output' variable
    :returns: Formatted string if stream is False else an empty string
    """
    formatter = CategoriesPrettyFormatter()
    file_ = formatter.get_stream_file(stream)

    headline = formatter.format_headline()
    print(headline, file=file_)

    for category, description in CATEGORIES.items():
        formatted_category = formatter.format_category(category, description)
        print(formatted_category, file=file_)

    print(formatter.format_ruler(sep="-"), file=file_)
    return formatter.get_output()


def print_categories():
    """Prints all possible categories"""
    to_string(stream=True)
