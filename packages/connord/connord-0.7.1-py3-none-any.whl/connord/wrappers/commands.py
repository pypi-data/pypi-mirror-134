# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.wrappers.commands
-------------------------

This module provides a base class for commands executed with subprocess.Popen
"""

import os
import subprocess
from pathlib import Path
from typing import List, Tuple, Union

from connord.exceptions import ConnordError
from connord.printer import Printer


class Command:
    exec: Path
    cmd: List[str]

    def __init__(self, command: str, search_command: bool = True):
        """
        Initialize the command.

        :param command: String of the command to execute with Popen.
        :param search_command: Boolean: If True search for the command in PATH else take
        the command string as is, for example if the command string already is the full
        path to the command.
        """
        self.exec = self._search_path(command) if search_command else Path(command)
        self.cmd = [str(self.exec)]

    def add_option(
        self,
        flag: str,
        *args: str,
        long_opt: bool = True,
        unique: bool = True,
    ):
        """
        Adds an option to the command. Options are flags (--FLAG or -FLAG) with zero
        or more arguments.

        :param flag: String: The option name
        :param args: String: zero or more arguments for the option as strings.
        :param long_opt: Boolean. Use long options (--OPTION). (default: True)
        :param unique:  Boolean. Don't add the option if already present.
        (default: True)
        """
        flag_type = "--" if long_opt else "-"
        option = flag if flag.startswith("-") else flag_type + flag

        if unique and option in self.cmd:
            return

        self.cmd.append(option)
        for arg in args:
            if arg:
                self.cmd.append(arg)

    def add_boolean_option(
        self, flag: str, arg: bool, long_opt: bool = True, unique: bool = True
    ):
        if arg:
            self.add_option(flag, long_opt=long_opt, unique=unique)

    def add_number_option(
        self,
        flag: str,
        arg: Union[int, float],
        long_opt: bool = True,
        unique: bool = True,
    ):
        self.add_option(flag, str(arg), long_opt=long_opt, unique=unique)

    def add_options(
        self,
        *args: Tuple[str, List[str]],
        long_opt: bool = True,
        unique: bool = True,
    ):
        """
        Adds multiple option to the command.

        :param args: Tuple of option name and the list of arguments
        :param long_opt: Boolean: use long options (--OPTION). (default: True)
        :param unique: Boolean. Don't add the option if already present.
        (default: True)
        """
        for flag, arg in args:
            if arg:
                self.add_option(flag, *arg, long_opt=long_opt, unique=unique)
            else:
                self.add_option(flag, long_opt=long_opt, unique=unique)

    def add_arguments(self, *args: str):
        """
        Add an argument to the command. Arguments don't have an option and are commonly
        added as last.

        :param args: String: zero or more arguments
        """
        for arg in args:
            if arg:
                self.cmd.append(arg)

    def remove_option(self, option: str):
        for o in self.cmd[1:].copy():
            if o.startswith("-") and o.lstrip("-") == option:
                self.cmd.remove(o)

    def remove_argument(self, argument: str):
        self.cmd.remove(argument)

    def has_flag(self, flag: str):
        if flag.startswith("-"):
            return flag in self.cmd

        return f"--{flag}" in self.cmd or f"-{flag}" in self.cmd

    def run(self, **kwargs):
        """
        Execute the command with all current options and arguments.

        :param kwargs: kwargs to pass to the Popen class.
        :return: The return code of the process.
        :rtype: int
        """
        with subprocess.Popen(self.cmd, **kwargs) as proc:
            return proc.wait()

    @staticmethod
    def _search_path(command: str):
        searchpaths = [Path(p) for p in os.environ["PATH"].split(":")]
        printer = Printer()
        with printer.Do(f"Searching for {command} executable\n"):
            for s in searchpaths:
                path = s / command
                if path.exists() and os.access(path, os.X_OK):
                    printer.info(f"Found: {path!s}")
                    return path

        raise ConnordError(
            f"No executable '{command}' found in search path."
            f" Is '{command}' installed?"
        )
