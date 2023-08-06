# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.printer
---------------

This module contains the Printer class which should always be used when printing to
the terminal.
"""

import errno
import sys
import typing

from progress.bar import IncrementalBar  # type: ignore
from progress.spinner import Spinner  # type: ignore


class NullSpinner(Spinner):
    """Fake a Spinner doing nothing"""

    def start(self):
        pass  # empty override

    def update(self):
        pass  # empty override

    def show(self, *args, **kwargs):
        pass  # empty override

    def next(self, n=1):
        pass  # empty override

    def write(self, s):
        pass  # empty override

    def finish(self):
        pass  # empty override


class NullBar(IncrementalBar):
    """Fake an IncrementalBar doing nothing"""

    def start(self):
        pass  # empty override

    def update(self):
        pass  # empty override

    def show(self, *args, **kwargs):
        pass  # empty override

    def next(self, n=1):
        pass  # empty override

    def write(self, s):
        pass  # empty override

    def finish(self):
        pass  # empty override


class Borg:
    """Define a borg class"""

    _shared_state: typing.ClassVar[dict] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Printer(Borg):
    """Generic printer. Every intentional output must go through this printer
    to recognize quiet and verbose mode set on the command-line or in the
    configuration.
    """

    prefix = "connord: "

    def __init__(self, verbose: bool = False, quiet: bool = False):
        """Initialize the printer. The attributes don't change once they are set.

        :param verbose: if True print info messages
        :param quiet: if True suppress error and info messages
        """

        Borg.__init__(self)
        if "verbose" not in self.__dict__:
            self.verbose = verbose
        if "quiet" not in self.__dict__:
            self.quiet = quiet

    def yes_no(self, question: str) -> bool:
        reply = input(question + " (y/N): ").lower().strip()
        if not reply:
            return False
        if reply in ("y", "ye", "yes"):
            return True
        if reply in ("n", "no"):
            return False

        return self.yes_no("Invalid answer. Try 'y' or 'n' or enter for No.")

    def error(self, message: str):
        """Prints errors if not quiet"""
        if not self.quiet:
            print(self.prefix + message, file=sys.stderr)

    def info(self, message: str, no_prefix: bool = False, no_newline: bool = False):
        """Prints info messages if verbose"""
        if self.verbose and not self.quiet:
            if no_prefix:
                message_prefixed = message
            else:
                message_prefixed = self.prefix + message
            if no_newline:
                print(message_prefixed, end="")
            else:
                print(message_prefixed)

    @staticmethod
    def write(message: str):
        """Prints messages independently of verbose and quiet settings
        There's no need to call this function directly. Just pass Printer to the
        file attribute of the __builtin__ print method.

        Example: print('something', file=Printer())
        """
        try:
            print(message, end="")
        except IOError as error:
            if error.errno != errno.EPIPE:
                raise

    @staticmethod
    def format_prefix(prefix: str) -> str:
        if len(prefix) < 40:
            return f"{prefix!s:40}"

        return f"{prefix!s:40} "

    class Do:
        def __init__(self, message: str):
            self.printer = Printer()
            self.message = self.printer.format_prefix(message)

        def __enter__(self):
            self.printer.info(self.message, no_newline=True)

        # pylint: disable=redefined-builtin
        # noinspection PyShadowingBuiltins
        def __exit__(self, type, value, traceback):
            if type:
                self.printer.info("Error", no_prefix=True)
            else:
                self.printer.info("Done", no_prefix=True)

    def incremental_bar(self, message: str = "", **kwargs) -> IncrementalBar:
        """Return an Incremental bar if verbose else a NullBar(IncrementalBar)
        which does nothing but can be used like the usual IncrementalBar

        :param message: the prefix message
        :param kwargs: kwargs to pass through to the IncrementalBar
        :returns: IncrementalBar if verbose else NullBar
        """
        if self.verbose:
            return IncrementalBar(self.format_prefix(message), bar_prefix="|", **kwargs)

        return NullBar()

    def spinner(self, message: str = "", **kwargs) -> Spinner:
        """Return a Spinner"""
        if self.verbose:
            return Spinner(self.format_prefix(message), **kwargs)

        return NullSpinner()
