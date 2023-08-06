# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.locations
-----------------

This module mixes together the 'countries' and 'areas' module and the location database.
"""

from typing import Dict, List, Optional, Union

from cachetools import LRUCache, cached

from connord.resources import OpenstreetmapLocationURL


class Coordinates:
    def __init__(self, latitude: Union[float, str], longitude: Union[float, str]):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"Coordinates: latitude: {self.latitude}, longitude: {self.longitude}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return self.latitude == other.latitude and self.longitude == other.longitude

        return False

    def __hash__(self):
        return hash((self.longitude, self.latitude))


# noinspection PyShadowingBuiltins
# pylint: disable=redefined-builtin
class Location:
    def __init__(
        self,
        coordinates: Coordinates,
        display_name: str,
        city: str,
        country: str,
        country_code: str,
        map: Optional[str],
    ):
        # TODO make use of Area and Country. circular imports??
        self.coordinates = coordinates
        self.display_name = display_name
        self.city = city
        self.country = country
        self.country_code = country_code
        self.map = map

    def __str__(self):
        return (
            f"Location: ({self.coordinates}), {self.country}, {self.country},"
            f" {self.city}"
        )

    def __repr__(self):
        no_map = "No map available"
        return (
            f"Location: ({self.coordinates}), {self.display_name}\n"
            f"{self.map if self.map else no_map}"
        )

    @classmethod
    def from_url(
        cls, coordinates: Coordinates, location: dict, map: Optional[str] = None
    ) -> "Location":
        """
        Creates a location from the json data received from the openstreetmap api. It
        does not use the openstreetmap coordinates which may differ from the original
        nordvpn coordinates. Instead, it uses the original coordinates used to query the
        location from openstreetmap.

        :param coordinates: Coordinates
        :param location: dictionary as received from the openstreetmap api
        :param map: an optional ascii map
        :return: The location
        """
        display_name: str = location["display_name"]
        city_keys: List[str] = ["city", "town", "village", "residential", "state"]
        city: str
        for key in city_keys:
            try:
                city = location["address"][key]
                break
            except KeyError:
                continue
        else:
            city = "Unknown"

        country: str = location["address"]["country"]
        country_code: str = location["address"]["country_code"]
        return cls(
            coordinates=coordinates,
            display_name=display_name,
            city=city,
            country=country,
            country_code=country_code,
            map=map,
        )

    @classmethod
    def from_database(cls, record: Dict[str, str]):
        coordinates = Coordinates(
            latitude=record["latitude"], longitude=record["longitude"]
        )

        display_name: str = record["display_name"]
        city: str = record["city"]
        country: str = record["country"]
        country_code: str = record["country_code"]
        map_: Optional[str] = record["map"]
        return cls(
            coordinates=coordinates,
            display_name=display_name,
            city=city,
            country=country,
            country_code=country_code,
            map=map_,
        )


@cached(cache=LRUCache(maxsize=50))
def query_location(coordinates: Coordinates) -> Location:
    """Query location given with latitude and longitude coordinates
    from remote nominatim api. The values are cached to reduce queries.
    The nominatim api restricts queries to 1/sec.

    :param coordinates: a Coordinates class
    :returns: a Location
    """

    resource = OpenstreetmapLocationURL(
        latitude=coordinates.latitude, longitude=coordinates.longitude
    )
    location_d = resource.receive()

    # TODO create map with ascii map package
    return Location.from_url(
        coordinates,
        location_d,
        map=None,
    )
