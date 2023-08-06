# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.formatter
-----------------

This module provides the base class for further Formatters.
"""

from typing import List, Union

from connord.printer import Printer


class Formatter:
    """Basic formatter class"""

    lines: List[str]
    max_line_length: int

    def __init__(self, max_line_length: int = 80):
        """Init

        :param max_line_length: Every calculation depends on the maximum column width
        """

        self.max_line_length = max_line_length
        self.lines = []

    def format_ruler(self, sep: str = "=") -> str:
        """Returns a ruler with sep as fill with max_line_length as width."""
        return sep * self.max_line_length

    def center_string(self, string: str, sep: str = " ") -> str:
        """Return a string within sep as fill with max_line_length as width."""
        left = (self.max_line_length - len(string) - 2) // 2
        right = self.max_line_length - left - len(string) - 2
        return f"{left * sep} {string} {right * sep}"

    def write(self, string: str):
        """Append the string to the output. This function is named write to be
        compatible to the built-in print function. Passing the formatter object to
        the print function as file uses this 'write' function to add the string to the
        output.
        """
        self.lines.append(string)

    def get_output(self, rstrip: bool = True) -> str:
        """Return the possibly stripped output collected so far"""
        return "".join(self.lines).rstrip() if rstrip else "".join(self.lines)

    def get_stream_file(self, stream: bool = False) -> Union[Printer, "Formatter"]:
        """Return self as stream if False else stdout"""
        return Printer() if stream else self
