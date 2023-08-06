# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.resources
-----------------

This module provides classes managing url, file and directory resources on a high level
and consistently.
"""

import getpass
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any, List, Pattern, Union
from urllib.request import urlretrieve
from zipfile import ZipFile

import requests
import yaml
from jinja2 import Environment, FileSystemLoader
from pkg_resources import resource_filename

from connord.config import Config, MAIN_CONFIG_PATH
from connord.exceptions import (
    MalformedResourceError,
    ResourceNotFoundError,
)
from connord.printer import Printer


class Resource:
    _path: Path

    def __init__(self, path: Union[str, os.PathLike]):
        self.path = Path(path)

    def create(self, mode: int = 0o666):
        """Empty method to be overwritten by subclasses"""
        raise NotImplementedError("Implement in subclasses")

    def remove(self, ignore_errors: bool = False):
        """Empty method to be overwritten by subclasses"""
        raise NotImplementedError("Implement in subclasses")

    def check_exists(self) -> bool:
        if self.exists():
            return True

        raise ResourceNotFoundError(self._path)

    def exists(self) -> bool:
        return self._path.exists()

    @property
    def path(self) -> Path:
        if self.exists():
            return self._path

        raise ResourceNotFoundError(self._path)

    @path.setter
    def path(self, value: Path):
        self._path = value

    def path_not_exist_ok(self) -> Path:
        return self._path


class DirectoryResource(Resource):
    def create(self, mode: int = 0o755):
        if not self._path.exists():
            self._path.mkdir(mode=mode, parents=True, exist_ok=False)

    def list_files(self, suffix: str = "") -> List[Path]:
        """Return a file list of a directory with the directory prepended. May be
        filtered by a specific suffix (extension).
        """

        files = [
            self.path / _file
            for _file in self.path.iterdir()
            if suffix and _file.suffix.removeprefix(".") == suffix
        ]

        return files

    def remove(self, ignore_errors: bool = False):
        shutil.rmtree(self.path_not_exist_ok(), ignore_errors=ignore_errors)


class FileResource(Resource):
    def create(self, mode: int = 0o644):
        if not self._path.exists():
            self._path.touch(mode=mode, exist_ok=False)

    def create_parent(self, mode: int = 0o755) -> DirectoryResource:
        directory = DirectoryResource(self._path.parent)
        directory.create(mode)
        return directory

    def has_permissions(self, permissions: int = 0o644) -> bool:
        stats = self.path.stat()
        return stats.st_mode & 0o777 == permissions

    def verify_safe_file_permissions(self, permissions: int = 0o600) -> bool:
        if not self.has_permissions(permissions):
            raise PermissionError(
                f"Unsafe file permissions: {self.path!r} should have mode: "
                f"{oct(permissions)!r}."
            )
        return True

    def remove(self, ignore_errors: bool = False):
        if not ignore_errors:
            self.path_not_exist_ok().unlink()
        else:
            if self.exists():
                self.path.unlink()

    def read(self) -> Any:
        return self.path.read_text(encoding="utf8")

    def equals(self, other: "FileResource") -> bool:
        try:
            if self.check_exists() and other.check_exists():
                return os.path.getsize(self.path) == os.path.getsize(other.path)
        except ResourceNotFoundError:
            pass

        return False


class URLResource(FileResource):
    def __init__(self, url: str, path: Union[str, os.PathLike]):
        super().__init__(path)

        self.url = url

    def download_progress(self):
        printer = Printer()
        spinner = printer.spinner(f"Downloading {self.url}")
        with requests.get(
            self.url, stream=True, timeout=60
        ) as response, self.path_not_exist_ok().open("wb") as dest_fd:
            chunk_size = 512
            for chunk in response.iter_content(chunk_size=chunk_size):
                spinner.next()
                dest_fd.write(chunk)

        spinner.finish()

    def download(self):
        urlretrieve(self.url, self.path_not_exist_ok())


class JsonURLResource(URLResource):
    def download_progress(self):
        self.download()

    def download(self):
        downloaded = self.receive()
        self.write(downloaded)

    def read(self) -> Any:
        with self.path.open("r", encoding="utf8") as filed:
            return json.load(filed)

    def write(self, to_dump: Any):
        with self.path_not_exist_ok().open("w") as filed:
            json.dump(to_dump, filed)

    def receive(self) -> Any:
        header = {
            "User-Agent": " ".join(
                (
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0)",
                    "Gecko/20100101 Firefox/60.0",
                )
            )
        }
        try:
            with requests.get(self.url, headers=header, timeout=60) as response:
                return response.json()
        except ValueError as error:
            raise MalformedResourceError(
                self.path_not_exist_ok(), str(error), "Unknown problem mark"
            )


class YamlFileResource(FileResource):
    def _read(self, unsafe: bool = False) -> Any:
        try:
            with self.path.open("r", encoding="utf8") as filed:
                loaded = yaml.unsafe_load(filed) if unsafe else yaml.safe_load(filed)
                return loaded
        except yaml.MarkedYAMLError as error:
            raise MalformedResourceError(
                self.path, str(error.problem), str(error.problem_mark)
            )

    def read(self) -> Any:
        return self._read(unsafe=False)

    def read_unsafe(self) -> Any:
        return self._read(unsafe=True)

    def _write(self, to_dump: Any, unsafe: bool = False) -> None:
        with self.path_not_exist_ok().open("w") as filed:
            if unsafe:
                yaml.dump(to_dump, filed, default_flow_style=False)
            else:
                yaml.safe_dump(to_dump, filed, default_flow_style=False)

    def write(self, to_dump: Any) -> None:
        self._write(to_dump, unsafe=True)

    def write_safe(self, to_dump: Any) -> None:
        self._write(to_dump, unsafe=False)


class JinjaTemplateResource(FileResource):
    def __init__(self, path: Union[str, os.PathLike]):
        super().__init__(path)
        self.environment = Environment(
            loader=FileSystemLoader(self.path.parent),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, mapping: dict) -> str:
        template = self.environment.get_template(self.path.name)
        return template.render(mapping)


class PidFileResource(FileResource):
    def __init__(self, name: str = "openvpn.pid"):
        config = Config()
        path = Path(config["connord"]["run_dir"]) / name
        super().__init__(path)

    def read(self) -> int:
        return int(super().read())


class ZipResource(FileResource):
    def unzip_progress(self, destination: Path = None, message: str = "") -> None:
        printer = Printer()
        destination = destination if destination else self.path.parent

        with ZipFile(self.path, "r") as zip_stream:
            name_list = zip_stream.namelist()
            message = message if message else f"Unzipping {self.path!s}"
            with printer.incremental_bar(
                message, max=len(name_list)
            ) as incremental_bar:
                for file_name in name_list:
                    zip_stream.extract(file_name, destination)
                    incremental_bar.next()

    def unzip(self, destination: Path = None) -> None:
        destination = destination if destination else self.path.parent
        with ZipFile(self.path, "r") as zipfile:
            zipfile.extractall(path=destination)


class ConnordConfigurationDirectory(DirectoryResource):
    def __init__(self):
        config_path = Path(MAIN_CONFIG_PATH).parent
        super().__init__(config_path)


class IptablesTemplate(JinjaTemplateResource):
    PATTERN: Pattern = re.compile(
        r"[0-9]*[-]?(?P<table>[a-zA-Z]+)(?P<version>6)?\.(?P<type>rules|fallback)"
    )

    table: str
    version: str
    type: str

    def __init__(self, path: Union[str, os.PathLike]):
        super().__init__(path)
        match = self.PATTERN.search(self.path_not_exist_ok().name)
        if match:
            groupdict = match.groupdict()
            self.table = groupdict["table"]
            self.version = "ipv6" if groupdict["version"] else "ipv4"
            self.type = groupdict["type"]
        else:
            raise MalformedResourceError(
                self.path_not_exist_ok(),
                f"Error: {self.path_not_exist_ok().name} is not a valid filename"
                f" for an iptables rules file.",
                problem_mark="",
            )

    def is_ipv6(self) -> bool:
        return self.version == "ipv6"

    def is_ipv4(self) -> bool:
        return self.version == "ipv4"

    def is_fallback(self) -> bool:
        return self.type == "fallback"

    def is_rules(self) -> bool:
        return self.type == "rules"


class IptablesTemplatesDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        directory = Path(config["iptables"]["templates_dir"])
        super().__init__(
            directory if directory.exists() else resource_filename(__name__, "config")
        )

    def list_templates(self) -> List[IptablesTemplate]:
        files = self.list_files(suffix="rules")
        files.extend(self.list_files(suffix="fallback"))

        return [IptablesTemplate(f) for f in files]

    def get_templates(
        self, table: str, fallback: bool = False, ipv6: bool = False
    ) -> List[IptablesTemplate]:
        return [
            t
            for t in self.list_templates()
            if t.table == table and t.is_fallback() == fallback and t.is_ipv6() == ipv6
        ]


class IptablesSaveDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        super().__init__(config["iptables"]["templates_dir"])


class TemporaryDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        super().__init__(config["connord"]["tmp_dir"])


class TemporaryFile(FileResource):
    def __init__(self, name: str):
        root = TemporaryDirectory()
        super().__init__(root.path / name)


class TemporaryOpenvpnConfigurationFile(TemporaryFile):
    def __init__(self):
        super().__init__("ovpn.conf")


class DatabaseFile(FileResource):
    def __init__(self):
        super().__init__(resource_filename(__name__, "db/connord.sqlite3"))


class OpenvpnScriptsDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        path = Path(config["connord"]["openvpn_scripts_dir"])
        super().__init__(
            path if path.exists() else resource_filename(__name__, "scripts")
        )


class OpenvpnScript(FileResource):
    def __init__(self, name: str = "openvpn_up_down.bash"):
        directory = OpenvpnScriptsDirectory()
        super().__init__(directory.path / name)


class StatsDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        super().__init__(config["connord"]["run_dir"])


class StatsFile(FileResource):
    def __init__(self, filename: str):
        root = StatsDirectory()
        super().__init__(root.path / filename)


class YamlStatsFile(YamlFileResource):
    def __init__(self, filename: str = "stats"):
        root = StatsDirectory()
        super().__init__(root.path / filename)


class EnvironmentFile(FileResource):
    def __init__(self, filename: str):
        root = StatsDirectory()
        super().__init__(root.path / filename)


class OpenstreetmapLocationURL(JsonURLResource):
    def __init__(self, latitude: float, longitude: float):
        config = Config()
        resource = TemporaryDirectory()
        path = resource.path / (str(latitude) + "_" + str(longitude) + ".json")

        endpoint = "reverse"
        flags = {
            "lat": str(latitude),
            "lon": str(longitude),
            "format": "jsonv2",
            "addressdetails": "1",
            "accept-language": "en",
            "zoom": "18",
        }

        url = f"{config['openstreetmap']['api_url']}/{endpoint}.php?"
        for k, v in flags.items():
            url += f"{k}={v}&"

        url = url.rstrip("&")
        super().__init__(url, path)


class CredentialsFile(FileResource):
    def create(self, mode=0o600):
        if self.exists():
            return

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        with self.path_not_exist_ok().open("w", encoding="utf8") as filed:
            filed.write(username + "\n")
            filed.write(password + "\n")

        self.path.chmod(mode)


class NordvpnServersURL(JsonURLResource):
    def __init__(self):
        config = Config()
        resource = TemporaryDirectory()
        super().__init__(
            config["connord"]["nordvpn_api_url"], resource.path / "servers.json"
        )


class NordvpnCredentialsFile(CredentialsFile):
    def __init__(self):
        config = Config()
        super().__init__(config["connord"]["nordvpn_credentials_file"])


class NordvpnConfigurationRootDirectory(DirectoryResource):
    def __init__(self):
        config = Config()
        super().__init__(config["connord"]["nordvpn_configurations_dir"])


class NordvpnOvpnConfigurationFile(FileResource):
    def __init__(self, domain: str, protocol: str = "udp"):
        if not domain.endswith(".nordvpn.com"):
            domain = f"{domain}.nordvpn.com"

        root = NordvpnConfigurationRootDirectory()
        filepath = (
            root.path_not_exist_ok() / f"ovpn_{protocol}" / f"{domain}.{protocol}.ovpn"
        )
        super().__init__(filepath)


class NordvpnConfigurationZipFile(ZipResource):
    def __init__(self, name: str = "ovpn.zip"):
        root = NordvpnConfigurationRootDirectory()
        super().__init__(root.path_not_exist_ok() / name)


class NordvpnConfigurationZipFileURL(URLResource):
    def __init__(self, name: str):
        config = Config()
        zip_resource = NordvpnConfigurationZipFile(name)
        url = (
            config["connord"]["nordvpn_configurations_url"]
            + "/"
            + zip_resource.path_not_exist_ok().name
        )
        super().__init__(url=url, path=zip_resource.path_not_exist_ok())
