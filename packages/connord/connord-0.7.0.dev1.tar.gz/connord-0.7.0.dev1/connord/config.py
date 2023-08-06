# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.config
--------------

This module provides the configuration updated from a configuration file. Be aware that
the configuration class follows the Borg pattern. The first instantiation initializes
the configuration with no easy possibility to reread the configuration files afterwards.
See the Config class documentation for further details.
"""

import os
from collections import UserDict
from pathlib import Path
from typing import ClassVar, List

import yaml

from connord.exceptions import MalformedResourceError

MAIN_CONFIG_PATH = Path("/etc/connord/config.yml")


# pylint: disable=too-few-public-methods
class Borg:
    """Define a borg class"""

    _shared_state: ClassVar[dict] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


# pylint: disable=too-many-ancestors,import-outside-toplevel
class Config(UserDict, Borg):
    def __init__(self, *pyfiles: str, **kwargs):

        Borg.__init__(self)

        if "data" in self.__dict__ and self.data:
            return

        self.loaded_configuration_files: List[Path] = []

        # default values if no configuration file is present
        data = {
            "environment": {"XTABLES_LIBDIR": "/usr/lib/xtables"},
            "iptables": {
                "dns": ["103.86.99.100/32", "103.86.96.100/32"],
                "vpn_interface": "tun+",
                "default_tables": ["filter"],
                "default_version": "4",
                "templates_dir": "/etc/connord/iptables",
            },
            "connord": {
                "verbose": False,
                "run_dir": "/var/run/connord",
                "tmp_dir": "/tmp/connord",
                "config_dir": "/etc/connord",
                "config_file": "/etc/connord/config.yml",
                "openvpn_configurations_dir": "/etc/connord/openvpn",
                "openvpn_scripts_dir": "/etc/connord/openvpn/scripts",
                "openvpn_credentials_file": "/etc/connord/openvpn/credentials",
                "default_categories": ["standard"],
                "protocol": "udp",
                "default_server": "best",
                # TODO actually use this key. Should default to an empty list instead of
                #   None
                "default_countries": None,
                "nordvpn_api_url": "https://api.nordvpn.com/server",
                "nordvpn_configurations_url": (
                    "https://downloads.nordcdn.com/configs/archives/servers"
                ),
                "nordvpn_configurations_dir": "/etc/connord/openvpn/nordvpn",
                "nordvpn_credentials_file": "/etc/connord/openvpn/nordvpn/credentials",
                "maximum_connection_retries": 3,
                # From https://www.top10vpn.com/guides/nordvpn-netflix/
                "netflix_countries": [
                    "au",  # Australia
                    "br",  # Brazil
                    "fr",  # France
                    "de",  # Germany
                    "it",  # Italy
                    "jp",  # Japan
                    "nl",  # Netherlands
                    "kr",  # South Korea
                    "gb",  # United Kingdom
                    "us",  # United States
                ],
            },
            "openvpn": {
                "daemon": False,
                # the following three options are needed by the builtin up down scripts
                "down-pre": True,
                "up-restart": True,
                "setenv": ["PATH", "/usr/sbin:/usr/bin:/sbin:/bin"],
                "auth-user-pass": "built-in",
                "verb": 3,
                "script-security": 2,
                "scripts": [
                    {
                        "name": "up",
                        "path": "built-in",
                        "stage": "up",
                        "creates": "up.env",
                    },
                    {
                        "name": "down",
                        "path": "built-in",
                        "stage": "down",
                        "creates": "down.env",
                    },
                    {
                        "name": "ipchange",
                        "path": "built-in",
                        "stage": "always",
                        "creates": "ipchange.env",
                    },
                ],
            },
            "openstreetmap": {"api_url": "https://nominatim.openstreetmap.org"},
        }

        # keys without initial value and stripped from debug output
        self.security_keys = ()

        new_config = self._load_config(*pyfiles)
        self._update_config(data, new_config)

        # additionally, from commandline or passed in kwargs
        self._update_config(data, kwargs)

        UserDict.__init__(self, data)

    def __str__(self) -> str:
        return "".join(
            sorted(
                [
                    f"{k} = {v}\n"
                    for (k, v) in self.items()
                    if k not in self.security_keys
                ]
            )
        )

    @staticmethod
    def _update_config(original: dict, new: dict):
        for key in ["iptables", "connord", "openvpn", "openstreetmap"]:
            if key in new:
                if key not in original:
                    original[key] = {}
                # original[key].update({k: v for (k, v) in new[key].items()})
                original[key].update(new[key])

    def _load_config(self, *pyfiles: str) -> dict:
        config: dict = {}
        paths: List[Path] = []
        if MAIN_CONFIG_PATH.exists():
            paths.append(MAIN_CONFIG_PATH)

        test_settings = "CONNORD_TEST_SETTINGS"
        if test_settings in os.environ:
            paths.append(Path(os.environ[test_settings]))

        for pyfile in pyfiles:
            if pyfile:
                paths.append(Path(pyfile))

        for path in paths:
            new_config = self._load_config_from_yaml(path)
            self._update_config(config, new_config)

        return config

    def _load_config_from_yaml(self, path: Path) -> dict:
        try:
            with path.open("r") as conf_fd:
                conf_dict = yaml.safe_load(conf_fd)
                if not conf_dict:
                    conf_dict = {}

                self.loaded_configuration_files.append(path)
                return conf_dict
        except yaml.MarkedYAMLError as error:
            raise MalformedResourceError(
                path,
                str(error.problem),
                str(error.problem_mark),
            )
