# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.openvpn
---------------

This module contains functionality around the openvpn command.
"""

import os
import shlex
import signal
import subprocess
import time
from pathlib import Path
from typing import List, Union

from connord import iptables, resources, update
from connord.config import Config
from connord.exceptions import OpenvpnCommandPanicError, ResourceNotFoundError
from connord.printer import Printer
from connord.servers import Server
from connord.wrappers.commands import Command


class OpenvpnCommand(Command):
    """Wraps openvpn"""

    def __init__(
        self,
        server: Server,
        openvpn: str,
        daemon: bool,
        protocol: str,
        search_path: bool = True,
    ):
        """Init

        :param server: a server dictionary
        :param openvpn: openvpn options as one string
        :param daemon: True if openvpn shall be run in daemon mode
        :param protocol: 'udp' or 'tcp'
        """
        super().__init__("openvpn", search_command=search_path)
        self.server = server
        self.fqdn = server.fqdn
        self.daemon = daemon
        self.protocol = protocol
        self.make(daemon, openvpn)

    def make(self, daemon: bool, openvpn_options: str):
        """add the command-line arguments relevant for the openvpn command"""
        if openvpn_options:
            options = shlex.split(openvpn_options)
            self.add_arguments(*options)

        if daemon:
            self.add_option("daemon")

        config = Config()
        for k, v in config["openvpn"].items():
            if isinstance(v, bool):
                self.add_boolean_option(k, v)
            elif v in ("true", "True", "false", "False"):
                self.add_boolean_option(k, v in ("true", "True"))
            elif isinstance(v, list):
                self.add_list_option(k, v)
            elif isinstance(v, (int, float)):
                self.add_number_option(k, v)
            else:
                self.add_string_option(k, v)

        if not self.has_flag("config"):
            try:
                self.add_config_option()
            except ResourceNotFoundError:
                update.update()  # give updating a try else let the error happen
                self.add_config_option()
        else:
            index = self.cmd.index("--config")
            config_file = self.cmd[index + 1]
            self.remove_option("config")
            self.remove_argument(config_file)
            self.add_config_option(config_file=config_file)

        if not self.has_flag("writepid"):
            pid_resource = resources.PidFileResource(name="openvpn.pid")
            self.add_option("writepid", str(pid_resource.path_not_exist_ok()))

    def add_auth_user_pass_option(self, value: str):
        if value == "built-in":
            creds_resource = resources.NordvpnCredentialsFile()
            creds_path: Path = creds_resource.path
        else:
            creds_path = Path(value)

        self.add_option("auth-user-pass", str(creds_path))

    def add_string_option(self, key: str, value: str):
        """Handles string values and adds the option to self.cmd. The key
        auth-user-pass needs special treatment since the value can be 'built-in'
        to use the predefined path to the credentials file.

        :param key: the flag
        :param value: the value related to the flag
        """
        if key == "auth-user-pass":
            self.add_auth_user_pass_option(value)
        else:
            self.add_option(key, value)

    def add_list_option(self, flag: str, list_: List):
        """Handles list values to be added to the final command. The 'scripts' key
        needs special treatment.

        :param flag: the flag
        :param list_: the list of strings
        """
        if flag == "scripts":
            self.add_scripts_option(list_)
        else:
            self.add_option(flag, *list_)

    @staticmethod
    def _format_script_arg(script_name: str, path: str, file_: str) -> str:
        """Format the argument for the scripts key to combine the script path and the
        path to the environment file in one string. Handles the special value 'built-in'
        to resolve to the built-in path of the corresponding script.
        :param script_name: name of the script
        :param path: either 'built-in' or a user-defined path
        :param file_: The name for the file created by the script
        :returns: the formatted argument.
        """
        if path == "built-in":
            script_resource: resources.FileResource = resources.OpenvpnScript(
                name=script_name
            )
        else:
            script_resource = resources.FileResource(path=path)

        env_resource = resources.EnvironmentFile(file_)

        return f"'{script_resource.path!s}' {env_resource.path_not_exist_ok()!s}"

    def add_scripts_option(self, scripts: List[dict]):
        """Adds the formatted script paths to the resulting command-line

        :param scripts: list of scripts served as dictionaries
        """
        for script in scripts:
            name = script["name"]
            path = script["path"]
            file_ = script["creates"]
            if name in ("up", "down"):
                arg = self._format_script_arg("openvpn_up_down.bash", path, file_)
            elif name == "ipchange":
                arg = self._format_script_arg("openvpn_ipchange.bash", path, file_)
            else:
                if path == "built-in":
                    raise ResourceNotFoundError(
                        path, f"No built-in found for {name!r}."
                    )

                arg = self._format_script_arg(name, path, file_)

            self.add_option(name, arg)

    def add_config_option(self, config_file: Union[str, os.PathLike] = None):
        """Remove all openvpn command-line arguments from the ovpn config file
        to prevent overriding the command-line. Use final temporary file as
        value for the --config flag

        :param config_file: path to an optional configuration file
        """

        if not config_file:
            config_resource = resources.NordvpnOvpnConfigurationFile(
                self.fqdn, self.protocol
            )
            config_path = config_resource.path
        else:
            config_path = Path(config_file)

        tmp_config_resource = resources.TemporaryOpenvpnConfigurationFile()

        with config_path.open("r", encoding="utf8") as filed:
            lines = filed.readlines()
        with tmp_config_resource.path_not_exist_ok().open("w") as filed:
            for line in lines:
                if line != "\n":
                    fake_line = line.rstrip() + " $"
                    flag, _ = fake_line.split(maxsplit=1)
                    if not self.has_flag(flag):
                        filed.write(line)
                else:
                    filed.write(line)

        tmp_config_resource.path.chmod(mode=0o640)
        self.add_option("config", str(tmp_config_resource.path))

    @staticmethod
    def cleanup():
        """Cleanup temporary stuff and reset iptables."""
        stats_resource_dir = resources.StatsDirectory()
        stats_resource_dir.remove(ignore_errors=True)
        iptables.reset(fallback=True)

    @staticmethod
    def is_running(process: subprocess.Popen) -> bool:
        """Return true if openvpn is running"""
        return not bool(process.poll())

    def panic(self, process: subprocess.Popen, problem: str):
        """High-level command to shut down openvpn and cleanup temporary files.

        :raises OpenvpnCommandPanicError
        """
        if self.is_running(process):
            process.kill()

        self.cleanup()
        # TODO move to cleanup() ??
        tmp_ovpn_resource = resources.TemporaryOpenvpnConfigurationFile()
        tmp_ovpn_resource.remove(ignore_errors=True)
        raise OpenvpnCommandPanicError(problem)

    def _wait_for_environment_to_come_up(self, ovpn: subprocess.Popen):
        config = Config()
        for _ in range(300):
            try:
                if self.is_running(ovpn):
                    # delay initialization of iptables until environment files are
                    # created. If none are created the delay still applies as normal
                    # timeout
                    time.sleep(0.2)
                    for script in config["openvpn"]["scripts"]:
                        stage = script["stage"]
                        if stage in ("up", "always"):
                            stats_file = resources.StatsFile(script["creates"])
                            stats_file.check_exists()
                    break

                self.panic(ovpn, "Openvpn process stopped unexpected.")
            except ResourceNotFoundError:
                pass
        else:
            self.panic(ovpn, "Timeout reached.")

    def _write_stats(self):
        server_stats = resources.YamlStatsFile(filename="server")
        server_stats.write(self.server)

        last_stats = resources.YamlStatsFile(filename="stats")
        try:
            stats_dict = last_stats.read()
        except ResourceNotFoundError:
            stats_dict = {}

        stats_dict["last_server"] = {}
        stats_dict["last_server"]["domain"] = self.fqdn
        stats_dict["last_server"]["protocol"] = self.protocol
        last_stats.write(stats_dict)

    def _apply_iptables_configurations(self, ovpn: subprocess.Popen):
        templates = iptables.YamlTemplates()
        templates.filter_by_predicate(lambda t: not t.is_fallback())
        if not templates.apply(self.server, self.protocol):
            self.panic(ovpn, "Applying iptables failed.")

    def run(self, **kwargs) -> bool:
        """High-level command to run openvpn with the assembled command-line.
        Shuts down openvpn after a timeout. Waits this time for openvpn to startup
        and writes the environment files from the scripts. As soon as they are
        present iptables rules are applied. If something goes wrong call the panic
        method

        :returns: True if everything went fine or running in daemon mode.
        """

        self.cleanup()

        stats_directory = resources.StatsDirectory()
        stats_directory.create()

        printer = Printer()
        printer.info(f"Running openvpn with '{self.cmd}'")
        with subprocess.Popen(self.cmd, **kwargs) as ovpn:
            # give openvpn a maximum of 60 seconds to startup.
            self._wait_for_environment_to_come_up(ovpn)
            self._write_stats()
            self._apply_iptables_configurations(ovpn)

            if self.is_running(ovpn):
                ovpn.wait()
            else:
                self.panic(ovpn, "Openvpn process stopped unexpected.")

        return True


def run_openvpn(server: Server, openvpn: str, daemon: bool, protocol: str) -> bool:
    """Intermediate function to set up openvpn and wrap the final run."""
    openvpn_cmd = OpenvpnCommand(server, openvpn, daemon, protocol)
    # openvpn_cmd.forge()

    try:
        retval = openvpn_cmd.run()
        # Waiting for openvpn to shut down until it has cleared everything
        time.sleep(1)
    except KeyboardInterrupt:
        retval = True
        time.sleep(1)

    if not openvpn_cmd.daemon:
        resources.TemporaryOpenvpnConfigurationFile().remove(ignore_errors=True)
        openvpn_cmd.cleanup()

    return retval


def kill_openvpn(pid: int = None):
    """Kill all openvpn processes currently running or if pid is given this process.
    :param pid: integer with a process id. Can be any pid but intention is to shut down
    openvpn this way. If None all openvpn process are shutdown targets
    """
    if pid:
        os.kill(pid, signal.SIGTERM)
    else:
        cmd = ["ps", "-A"]
        with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
            out, _ = proc.communicate()
            for line in out.decode().splitlines():
                if "openvpn" in line:
                    pid = int(line.split(None, 1)[0])
                    os.kill(pid, signal.SIGTERM)
