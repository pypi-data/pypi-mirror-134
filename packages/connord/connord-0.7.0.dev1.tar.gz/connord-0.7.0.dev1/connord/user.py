# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.user
------------

This module is a utility class around users and permissions.
"""

import functools
import os
import subprocess
from typing import Any


def is_root() -> bool:
    """
    Returns true if user is root

    :return: True if effective uid is 0
    """
    return os.geteuid() == 0


def needs_root(func) -> Any:
    """Decorator for functions needing root access"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if is_root():
            return func(*args, **kwargs)

        raise PermissionError(f"Function '{func.__name__}' needs root access.")

    return wrapper


def prompt_sudo() -> bool:
    """
    Prompt for sudo password and change effective uid to root on success.

    :return: True if user has root access now
    """

    if os.geteuid() != 0:
        message = "[connord][sudo] password needed: "
        return subprocess.check_call(f"sudo -v -p '{message}'", shell=True) == 0

    return True
