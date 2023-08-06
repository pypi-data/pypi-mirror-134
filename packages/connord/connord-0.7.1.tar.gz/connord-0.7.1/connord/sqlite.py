# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.sqlite
--------------

This module wraps sqlite to provide high level functions accessing and manipulating the
location database.
"""

import sqlite3
from pathlib import Path
from sqlite3 import Error
from typing import Any, List, Tuple

from connord.exceptions import SqliteError
from connord.locations import Coordinates, Location
from connord.resources import DatabaseFile


def create_connection(db_file: str = None) -> sqlite3.Connection:
    """Create a database connection"""

    if not db_file:
        db_resource = DatabaseFile()
        db_resource.create()
        db_path = db_resource.path
    else:
        db_path = Path(db_file)

    try:
        connection = sqlite3.connect(str(db_path))
        return connection
    except Error as error:
        raise SqliteError(
            error, f"Could not create a connection to database '{db_path!s}'"
        )


def execute(connection: sqlite3.Connection, sql: str):
    """Create the table. Prints errors to stdout.

    :param connection: a database connection
    :param sql: the sql to execute.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except Error as error:
        raise SqliteError(error, "Could not create table")


def _process_where_to_sql(where: List[Tuple[str, str, str]] = None) -> str:
    sql = str()
    if where:
        counter = 0
        for condition, operator, value in where:
            if counter == 0:
                sql += f" WHERE {condition} {operator} '{value}'"
            else:
                sql += f" AND {condition} {operator} '{value}'"
            counter += 1

    return sql


def _process_sortby_to_sql(sortby: List[Tuple[str, str]] = None) -> str:
    sql = str()
    if sortby:
        counter = 0
        for orderby, order in sortby:
            if counter == 0:
                sql += f" ORDER BY {orderby} {order.upper()}"
            else:
                sql += f", {orderby} {order.upper()}"

            counter += 1

    return sql


def query(
    connection: sqlite3.Connection,
    columns: str = "*",
    table: str = "locations",
    where: List[Tuple[str, str, str]] = None,
    distinct: bool = False,
    sortby: List[Tuple[str, str]] = None,
    fetch: str = "all",
) -> Any:
    """
    Query columns from a given table by unique locations defined by latitude and
    longitude if not None else selects all rows

    param connection: A valid connection to the database
    param columns: A comma separated list of columns. Takes the special value '*'
    param table: query the given table
    param latitude: the latitude of the location
    param longitude: the longitude of the location
    param fetch: the query type 'all' or 'one'. 'many' is currently resolved to 'all'
    returns: the result of the query. It may be None if location does not exist
    """

    if distinct:
        sql = f"SELECT DISTINCT {columns} FROM {table}"
    else:
        sql = f"SELECT {columns} FROM {table}"

    sql += _process_where_to_sql(where)
    sql += _process_sortby_to_sql(sortby)

    try:
        if fetch == "one":
            cursor = connection.cursor()
            result = cursor.execute(sql).fetchone()
            if result:
                return result[0]

            return result

        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql).fetchall()
        return result

    except Error as error:
        raise SqliteError(error, f"Failed query: {sql}")


def create_location(connection: sqlite3.Connection, location: Location) -> Any:
    """Create a location in the location table. Prints errors to stdout.

    :param connection: a database connection
    :param location: tuple with (latitude, longitude, display_name, city, country,
                     country_code)
    """
    sql = """INSERT OR IGNORE INTO locations(
                latitude,
                longitude,
                display_name,
                city,
                country,
                country_code,
                map
              )
              VALUES(?,?,?,?,?,?,?)"""

    try:
        cursor = connection.cursor()
        cursor.execute(
            sql,
            (
                location.coordinates.latitude,
                location.coordinates.longitude,
                location.display_name,
                location.city,
                location.country,
                location.country_code,
                location.map,
            ),
        )
        connection.commit()
        return cursor.lastrowid
    except Error as error:
        raise SqliteError(error, f"Could not create location '{location}'")


def location_exists(connection: sqlite3.Connection, coordinates: Coordinates) -> bool:
    """Return true if a location give by latitude and longitude exists."""
    result = query(
        connection,
        table="locations",
        columns="latitude, longitude",
        where=[
            ("latitude", "=", f"{coordinates.latitude}"),
            ("longitude", "=", f"{coordinates.longitude}"),
        ],
        fetch="one",
    )
    return bool(result)


def get_area(connection: sqlite3.Connection, coordinates: Coordinates) -> str:
    return query(
        connection,
        table="locations",
        columns="city",
        where=[
            ("latitude", "=", f"{coordinates.latitude}"),
            ("longitude", "=", f"{coordinates.longitude}"),
        ],
        fetch="one",
    )


def get_area_by_prefix(connection: sqlite3.Connection, area_name: str) -> List[dict]:
    return query(
        connection,
        columns="city, latitude, longitude",
        table="locations",
        where=[("LOWER(city)", "LIKE", f"{area_name}%")],
        fetch="all",
    )


def get_map(connection: sqlite3.Connection, coordinates: Coordinates) -> str:
    return query(
        connection,
        columns="map",
        where=[
            ("latitude", "=", f"{coordinates.latitude}"),
            ("longitude", "=", f"{coordinates.longitude}"),
        ],
        fetch="one",
    )


def create_location_table(connection: sqlite3.Connection):
    """Creates the location table if it doesn't exist.

    :raises: SqliteError if connection is None
    """
    sql_create_location_table = """ CREATE TABLE IF NOT EXISTS locations(
                                        latitude text NOT NULL,
                                        longitude text NOT NULL,
                                        display_name text NOT NULL,
                                        city text NOT NULL,
                                        country NOT NULL,
                                        country_code NOT NULL,
                                        map NULL,
                                        UNIQUE(latitude, longitude)
                                    ); """

    execute(connection, sql_create_location_table)


def init_database(connection: sqlite3.Connection):
    """Initialize location database

    :param connection: a database connection
    """

    with connection:
        create_location_table(connection)
