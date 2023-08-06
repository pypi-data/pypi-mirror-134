# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.areas
-------------

This module contains the classes and functions managing server areas.
"""

from typing import Dict, List, Optional

from connord import sqlite
from connord.exceptions import AreaError
from connord.formatter import Formatter
from connord.locations import Coordinates, Location


class Area:
    TRANSLATION_TABLE = str.maketrans("áãčëéşșť", "aaceesst")

    name: Optional[str]
    id: Optional[str]
    coordinates: Coordinates

    def __init__(self, name: Optional[str], coordinates: Coordinates):
        self.name = name
        self.id = self.translate(name.casefold()) if name is not None else None
        self.coordinates = coordinates

    def translate(self, name: str) -> str:
        """Translate special characters to the english equivalent

        :returns: the translated area name
        """
        return name.translate(self.TRANSLATION_TABLE)

    @classmethod
    def from_database(cls, record: Dict[str, str]):
        name: str = record["city"]
        latitude: str = record["latitude"]
        longitude: str = record["longitude"]

        return cls(name, Coordinates(latitude, longitude))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Area):
            return self.coordinates == other.coordinates

        return False

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.coordinates)


def verify_areas(areas_: List[str]) -> bool:
    """Verify a list of areas if they can be resolved to valid areas saved in
    the location database. Ambiguous strings resolve to more than one location.

    :param areas_: list of area names (cities) as string which may be just prefixes
    :returns: list of found areas if prefixes could be resolved unambiguously
    :raises: AreaError if an area could not be found or if the area string is ambiguous
    """

    with sqlite.create_connection() as connection:
        areas_found: Dict[str, List[Area]] = {
            a: [Area.from_database(r) for r in sqlite.get_area_by_prefix(connection, a)]
            for a in areas_
        }

    for area, list_ in areas_found.items():
        if not list_:
            raise AreaError(f"Area not found: {area}")

    ambiguous_areas = {a: c for a, c in areas_found.items() if len(c) > 1}
    if ambiguous_areas:
        error_string = ""
        for area, cities in ambiguous_areas.items():
            error_string += f" {area!s}: [{', '.join([str(s) for s in cities])}],"

        error_string = error_string.rstrip(",")
        raise AreaError(f"Ambiguous Areas:{error_string}")

    return True


def get_min_id(city: str) -> str:
    """Calculate the minimum string in lower case which must be given to identify an
    area/city unambiguously

    :param city: the area/city as string
    :returns: the minimum string or an empty string if for the given city no area was
    found in the database
    """

    if not city:
        raise ValueError("city may not be empty")

    def min_id_rec(prefix: str, current_areas: List[str], result: str) -> str:
        if not current_areas:
            return str()

        if len(current_areas) == 1:
            return result

        first_char = prefix[0].lower()
        prefix = prefix[1:]
        result += first_char
        current_areas = [
            a[1:] for a in current_areas if a and a.lower().startswith(first_char)
        ]

        return min_id_rec(prefix, current_areas, result)

    with sqlite.create_connection() as connection:
        records = sqlite.get_area_by_prefix(connection, str())
        areas_ = [r["city"] for r in records]

    return min_id_rec(city, areas_, str())


class AreasPrettyFormatter(Formatter):
    """Format areas in pretty format"""

    def format_headline(self, sep: str = "=") -> str:
        """Format the headline

        :param sep: filling character and separator
        :returns: the headline
        """
        headline = self.format_ruler(sep) + "\n"
        headline += f"{'Mini ID':8}: {'Latitude':^15} {'Longitude':^15}  {'City':4}\n"
        headline += f"{'Address'}\n"
        headline += self.format_ruler(sep)
        return headline

    def format_area(self, location: Location) -> str:
        """Format the area

        :param location:
        :returns: the area as string
        """

        lat = location.coordinates.latitude
        lon = location.coordinates.longitude
        display_name = location.display_name
        city = location.city
        min_id = get_min_id(city)

        string = f"{min_id!r:8}: {lat: 14.9f}° {lon: 14.9f}°  {city:40}\n"
        string += f"{display_name}\n"
        string += self.format_ruler(sep="-")
        return string


def to_string(stream: bool = False) -> str:
    """High-level command to format areas and returns the resulting string if not
    streaming directly to screen.

    :param stream: True if the output shall be streamed to stdout
    :returns: When streaming an empty string or else the result of the formatter
    """
    formatter = AreasPrettyFormatter()
    file_ = formatter.get_stream_file(stream)

    with sqlite.create_connection() as connection:
        records = sqlite.query(
            connection,
            columns="*",
            table="locations",
            sortby=[("city", "asc")],
            fetch="all",
        )
        locations = [Location.from_database(r) for r in records]

    headline = formatter.format_headline()
    print(headline, file=file_)

    for location in locations:
        area = formatter.format_area(location)
        print(area, file=file_)

    return formatter.get_output()


def print_areas():
    """High-level command to print areas to stdout"""
    to_string(stream=True)
