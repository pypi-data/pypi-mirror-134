# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.countries
-----------------

The module contains the classes and functions managing countries.
"""

from typing import Dict, List

from connord import sqlite
from connord.exceptions import CountryError
from connord.formatter import Formatter


class Country:
    name: str
    flag: str

    def __init__(self, name: str = "", flag: str = ""):
        if not name and not flag:
            raise ValueError("name and flag can't be both empty")

        if name and not flag:
            self.name = name
            with sqlite.create_connection() as connection:
                flag_: str = sqlite.query(
                    connection,
                    columns="country_code",
                    table="locations",
                    where=[("LOWER(country)", "=", f"{name.lower()}")],
                    fetch="one",
                )
            self.flag = flag_.lower()
        elif not name and flag:
            self.flag = flag.lower()
            with sqlite.create_connection() as connection:
                name_: str = sqlite.query(
                    connection,
                    columns="country",
                    table="locations",
                    where=[("country_code", "=", f"{self.flag}")],
                    fetch="one",
                )
                self.name = name_
        else:
            self.name = name
            self.flag = flag.lower()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Country):
            return self.flag == other.flag

        return False

    @classmethod
    def from_database(cls, record: Dict[str, str]):
        name = record["country"]
        flag = record["country_code"]

        return cls(name=name, flag=flag)


def verify_countries(countries: List[str]) -> bool:
    """Verify if a list of countries are valid

    :param countries: a list of country codes/flags to verify
    :returns: True if all countries are valid
    :raises CountryError: if one country in the list is invalid
    """

    with sqlite.create_connection() as connection:
        countries_ = [
            Country(name=r["country"], flag=r["country_code"])
            for r in sqlite.query(
                connection,
                columns="country, country_code",
                table="locations",
                distinct=True,
                fetch="all",
            )
        ]

    wrong_countries: List[str] = [
        country for country in countries if Country(flag=country) not in countries_
    ]

    if wrong_countries:
        if len(wrong_countries) == 1:
            error_message = f"Invalid country: {wrong_countries[0]!s}"
        else:
            countries_s = ""
            for country in wrong_countries:
                countries_s += f"{country!r},"

            error_message = f"Invalid countries: {countries_s.rstrip(',')}."

        raise CountryError(error_message)

    return True


class CountriesPrettyFormatter(Formatter):
    """Format countries in pretty format"""

    def format_headline(self, sep: str = "=") -> str:
        """Returns the centered headline filled with sep"""
        countries_header = "Countries"
        return self.center_string(countries_header, sep)

    @staticmethod
    def format_country(country_code: str, country: str) -> str:
        """Returns the formatted country string"""
        return f"{country_code:6}{country}"


def to_string(stream: bool = False) -> str:
    """Gather all countries  in a printable string

    :param stream: If True print to stdout else print to 'formatter.output' variable
    :returns: Formatted string if stream is False else an empty string
    """

    formatter = CountriesPrettyFormatter()
    file_ = formatter.get_stream_file(stream)

    headline = formatter.format_headline()
    print(headline, file=file_)

    with sqlite.create_connection() as connection:
        records = sqlite.query(
            connection,
            columns="country, country_code",
            table="locations",
            distinct=True,
            sortby=[("country", "asc")],
            fetch="all",
        )
        countries_ = [Country.from_database(r) for r in records]

    for country in countries_:
        formatted_country = formatter.format_country(country.flag, country.name)
        print(formatted_country, file=file_)

    print(formatter.format_ruler(sep="-"), file=file_)
    return formatter.get_output()


def print_countries():
    """Prints all possible countries"""
    to_string(stream=True)
