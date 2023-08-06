# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.version
---------------

This small module provides a function to print the connord version.
"""


from connord import __copyright__, __version__, resources
from connord.printer import Printer


def print_version():
    """Prints the version of connord along with the copyright."""
    printer = Printer()
    print(f"connord {__version__}", file=printer)
    print(__copyright__, file=printer)
    config_resource = resources.ConnordConfigurationDirectory()
    if config_resource.exists():
        printer.info(f"\nConfiguration directory: '{config_resource.path!s}'")
    else:
        printer.info(
            f"Default configuration directory "
            f"'{config_resource.path_not_exist_ok()}' does not exist."
        )
