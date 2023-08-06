# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.parser.lexer
--------------------

This module provides a lexer, which is tokenizing strings. These tokens can be used by a
parser to create an AST.
"""

from enum import Enum
from typing import Any, Callable, List, Optional, Tuple


class TokenKind(Enum):
    """An `Enum` of the different kinds of tokens the `Lexer` can parse."""

    NUMBER = "<number>"
    STRING = "<string literal>"
    HOSTNAME = "<hostname>"
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="
    EQUAL = "="
    EQUAL_EQUAL = "=="
    BANG_EQUAL = "!="
    BANG = "!"
    COMMA = ","
    BAR = "|"
    LPAREN = "("
    RPAREN = ")"


class Token:
    """The `Token` class consists of a `TokenKind` and a value."""

    kind: TokenKind
    value: Any

    def __init__(self, kind: TokenKind, value: Any):
        self.kind = kind
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Token):
            return other.kind == self.kind and other.value == self.value

        return False

    def __repr__(self):
        return f"Token(kind={self.kind.value!r},value={self.value!r}"

    def __str__(self):
        return str(self.value)


class TokenError(Exception):
    pass


class Lexer:
    """Parses a given string to a list of `Token`s"""

    tokens: List[Token]
    string: str
    index: int

    def __init__(self, string: str):
        self.tokens = []
        self.string = string
        self.index = 0

    def curr(self) -> str:
        """
        Return current character

        :return: character as string
        """
        return self.string[self.index]

    def peek(self) -> str:
        """
        Return next character without increasing the index

        :return: character as string
        """
        return self.string[self.index + 1]

    def next(self, char: str) -> bool:
        """
        Return true if the next character matches the argument

        :param char: the character to match
        :return: true if the next character matches 'char'
        """
        return self.index + 1 < len(self.string) and self.peek() == char

    def is_exhausted(self) -> bool:
        """
        Return true if the index is greater or equal than the string length
        :return: bool
        """
        return self.index >= len(self.string)

    def consume(self, n: int = 1) -> str:
        """
        Increases the index and returns the substring from current position + n

        :param n: Amount of characters to consume
        :return: The substring for index + n
        """
        sub = self.string[self.index : self.index + n]
        self.index += n
        return sub

    def make_token(
        self,
        kind: TokenKind,
        value: Optional[Any] = None,
        expect: Optional[Tuple[str, TokenKind, Any]] = None,
        consume: bool = True,
    ):
        """
        Creates a :class:`Token` depending on the parameters.

        :param kind: Create a `Token` of this `TokenKind` if expect is `None`
        :param value: Create a `Token` with this value if expect is `None`. If `None`
        create the token with `TokenKind.value` instead.
        :param expect: If the expected character matches then create this `TokenKind`
        with given value instead of kind and value parameters.
        :param consume: Set to `False` if the characters shall not be consumed
        :return: The created `Token`
        """
        consume_count = 1
        if expect:
            char, next_kind, next_value = expect
            if self.next(char):
                consume_count = 2
                kind = next_kind
                value = next_value

        if consume:
            self.consume(consume_count)

        return Token(kind, value) if value else Token(kind, kind.value)

    # pylint: disable=too-many-return-statements
    def _parse(self, char: str) -> Optional[Token]:
        if char == "(":
            return self.make_token(TokenKind.LPAREN)
        if char == ")":
            return self.make_token(TokenKind.RPAREN)
        if char == "<":
            return self.make_token(
                TokenKind.LESS, expect=("=", TokenKind.LESS_EQUAL, "<=")
            )
        if char == "=":
            return self.make_token(
                TokenKind.EQUAL, expect=("=", TokenKind.EQUAL_EQUAL, "==")
            )
        if char == "!":
            return self.make_token(
                TokenKind.BANG, expect=("=", TokenKind.BANG_EQUAL, "!=")
            )
        if char == ">":
            return self.make_token(
                TokenKind.GREATER, expect=("=", TokenKind.GREATER_EQUAL, ">=")
            )
        if char == "|":
            return self.make_token(TokenKind.BAR)
        if char == ",":
            return self.make_token(TokenKind.COMMA)
        if char.isdecimal():
            number = self.lex_decimal()
            return self.make_token(TokenKind.NUMBER, number, consume=False)
        if char.isalpha():
            string = self.lex_alpha()
            if not self.is_exhausted() and self.curr().isdecimal():
                number = self.lex_decimal()
                return self.make_token(
                    TokenKind.HOSTNAME, (string, number), consume=False
                )

            return self.make_token(TokenKind.STRING, string, consume=False)
        if char.isspace():
            # ignore whitespace
            self.consume()
            return None

        raise TokenError(f"Unrecognized character {char!r} at column {self.index}")

    def lex(self) -> List[Token]:
        """
        The main method to start parsing the input string to a list of `Token`s
        :return: The list of `Token`s
        """
        while not self.is_exhausted():
            token = self._parse(self.curr())
            if token:
                self.tokens.append(token)

        return self.tokens

    def _lex_sub(self, func: Callable) -> str:
        start = self.index
        while not self.is_exhausted():
            char = self.curr()
            if not func(char):
                break

            self.index += 1

        return self.string[start : self.index]

    def lex_alpha(self) -> str:
        """
        Parse a sequence of alpha [a-zA-Z] characters to a string
        :return: The resulting substring consisting of alpha characters
        """
        return self._lex_sub(lambda c: c.isalpha())

    def lex_decimal(self) -> int:
        """
        Parse a sequence of decimal [0-9] characters to an integer
        :return: The resulting integer
        """
        sub = self._lex_sub(lambda c: c.isdecimal())
        return int(sub)
