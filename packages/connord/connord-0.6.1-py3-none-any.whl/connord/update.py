# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.update
--------------

This module provides ways to update configuration files and the database.
"""

import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Set

from connord import resources, servers, sqlite
from connord.areas import Area
from connord.exceptions import ResourceNotFoundError
from connord.locations import query_location
from connord.printer import Printer
from connord.sqlite import init_database

__ARCHIVES = {"standard": "ovpn.zip", "obfuscated": "ovpn_xor.zip"}
TIMEOUT = timedelta(hours=1)


def download_archives() -> bool:
    """Download the zip files"""
    for _, archive in __ARCHIVES.items():
        zip_resource = resources.NordvpnConfigurationZipFile(archive)
        zip_resource.create_parent()
        try:
            zip_resource.path.rename(zip_resource.path.parent / (archive + ".orig"))
        except ResourceNotFoundError:
            pass

        zip_resource_url = resources.NordvpnConfigurationZipFileURL(archive)
        zip_resource_url.download_progress()

    return True


def unzip():
    """Unzip the configuration files"""

    printer = Printer()

    zip_root_resource = resources.NordvpnConfigurationZipFile()
    zip_root_resource.create_parent()

    with printer.Do("Deleting old configuration files"):
        for ovpn_dir in ("ovpn_udp", "ovpn_tcp"):
            ovpn_dir_path = zip_root_resource.path / ovpn_dir
            ovpn_dir_resource = resources.DirectoryResource(ovpn_dir_path)
            ovpn_dir_resource.remove(ignore_errors=True)

    for key, archive in __ARCHIVES.items():
        zip_resource = resources.NordvpnConfigurationZipFile(archive)
        zip_resource.unzip_progress(message=f"Unzipping {key} configurations")


def update():
    """Update connord openvpn configuration files and databases"""
    update_ovpn_files()
    update_database()


def update_ovpn_files():
    download_archives()
    unzip()


def update_needed(zip_path: Path) -> bool:
    """Check if an update is needed
    : returns: False if the zip file's creation time hasn't reached the timeout
               else True.
    """
    if not os.path.exists(zip_path):
        return True

    now = datetime.now()
    time_created = datetime.fromtimestamp(os.path.getctime(zip_path))
    return now - TIMEOUT > time_created


def update_database():
    """Updates the location database with least possible online queries."""

    with sqlite.create_connection() as connection:
        init_database(connection)

    printer = Printer()

    printer.info("Querying servers and area information")
    servers_ = servers.Servers()

    areas: Set[Area] = {s.area for s in servers_}
    printer.info(f"Found {len(areas)} different areas.")

    with printer.incremental_bar("Updating location database", max=len(areas)) as bar:
        # TODO remove redundant areas from location database
        for area in areas:
            with sqlite.create_connection() as connection:
                if not sqlite.location_exists(connection, area.coordinates):
                    location = query_location(area.coordinates)
                    sqlite.create_location(connection, location)

            bar.next()
