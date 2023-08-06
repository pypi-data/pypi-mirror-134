# -*- coding: utf-8 -*-

#  Copyright (C) 2021-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.exceptions
------------------

This module aims to contain all Connords' exceptions.
"""

from pathlib import Path


class ConnordError(Exception):
    """Main Exception class for connord module"""


class AreaError(ConnordError):
    """Thrown within this module"""


class CategoriesError(ConnordError):
    """Throw within this module"""


class ConnectError(ConnordError):
    """Thrown within this module"""


class OpenvpnCommandPanicError(ConnectError):
    """Raised when something went wrong running openvpn"""

    def __init__(self, problem: str, message: str = None):
        """Initialize

        :param problem: string to describe what went wrong
        :param message: If not None apply default message.
        """
        if not message:
            message = f"Running openvpn failed: {problem}"

        super().__init__(message)
        self.problem = problem


class CountryError(ConnordError):
    """Raised within this module"""


class FeatureError(ConnordError):
    """
    Thrown within this module
    """


class IptablesError(ConnordError):
    """Raise within this module"""


class LoadError(ConnordError):
    """The Error thrown within this module"""


class MalformedResourceError(ConnordError):
    """Raise when a path (like yaml) could not be parsed due to parsing errors."""

    def __init__(self, path: Path, problem: str, problem_mark: str):
        """Init

        :param path: the file in question
        :param problem: description of the problem
        :param problem_mark: hint where the problem arose
        """
        super().__init__(
            f"Malformed path: {str(path)!r}\n{problem!s}\n{problem_mark!s}"
        )

        self.resource = path
        self.problem = problem
        self.problem_mark = problem_mark


class ResourceNotFoundError(ConnordError):
    """Raised when a path is requested but doesn't exist"""

    def __init__(self, path: Path, message: str = None):

        # if a message is given use it else use the one defined here
        if message:
            super().__init__(message)
        else:
            super().__init__(f"Resource does not exist: {path!s}")

        #: A string representing a file path
        self.resource_file = path


class DomainNotFoundError(ConnordError):
    """Raised when a domain is requested but doesn't exist."""

    def __init__(self, domain: str, message: str = None):
        if not message:
            message = f"Domain not found: {domain!r}"

        super().__init__(message)
        self.domain = domain


class MalformedDomainError(ConnordError):
    """Raised when domain is not in the expected format."""

    def __init__(self, domain: str, problem: str, message: str = None):
        if not message:
            message = f"Invalid domain: {domain!r}: {problem}"

        super().__init__(message)
        self.problem = problem


class SqliteError(ConnordError):
    """Thrown within this module"""

    def __init__(self, error: BaseException = None, message: str = ""):
        super().__init__()
        self.error = error

        if not message:
            self.message = f"Database Error:\n  {error}"
        else:
            self.message = f"Database Error: {message}\n  {error}"


class UpdateError(ConnordError):
    """Raised during update"""


class UserError(ConnordError):
    """Thrown within this module"""


class EvaluationError(ConnordError):
    pass
