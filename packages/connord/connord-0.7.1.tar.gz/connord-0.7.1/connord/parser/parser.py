# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.parser.parser
---------------------

This module provides a parser creating an AST of expressions from tokens. Finally, these
expressions can be evaluated.
"""

import re
from abc import ABC
from collections import UserDict
from typing import Any, List, Pattern

from connord.exceptions import EvaluationError
from connord.parser.lexer import (
    Token,
    TokenKind,
)


class Environment(UserDict):
    """A subclass of dictionary. The Environment in which an Expression is evaluated."""

    def update_hostname(self, domain: str):
        r"""
        Update the environment by the given domain, which is internally converted
        to a Hostname expression. If not present already the Hostname is added instead
        of updated.
        :param domain: String consisting of {country_code}{integer}. For example
        'us1000'.
        """
        self.update({"hostname": Hostname.from_domain(domain)})


class Expression:
    """Base class for all kind of expressions"""

    def eval(self, env: Environment) -> Any:
        raise NotImplementedError


class Alpha(str, Expression):
    """Subclass of `str`. An `Expression` consisting of alpha characters [a-zA-Z]"""

    def eval(self, env: Environment) -> str:
        return str(self)

    def __new__(cls, token: Token):
        return str.__new__(cls, token.value)


class Decimal(int, Expression):
    """Subclass of `int`. An `Expression` consisting of a positive integer."""

    def eval(self, env: Environment) -> int:
        return int(self)

    def __new__(cls, token: Token):
        return int.__new__(cls, token.value)


class Hostname(Expression):
    flag: str
    decimal: int

    regex: Pattern = re.compile(r"([a-zA-Z]{2})([0-9]+)(\..+\..+)?")

    def __init__(self, token: Token):
        self.flag, self.decimal = token.value

    def eval(self, env: Environment) -> Any:
        return self.flag + str(self.decimal)

    @classmethod
    def from_domain(cls, domain: str) -> "Hostname":
        """

        :param domain: a string made of a leading 2-letter country code and following
        arbitrary digits but at least one or a string like above followed by a domain
        name and top level qualifier (i.e. us1000.nordvpn.com)
        :return: a Hostname class
        """
        match = cls.regex.search(domain)
        if match:
            flag, decimal = match.group(1, 2)
            return cls(Token(TokenKind.HOSTNAME, (flag, int(decimal))))

        raise ValueError(f"Invalid domain {domain!r}")

    def __eq__(self, other):
        if isinstance(other, Hostname):
            return other.flag == self.flag and other.decimal == self.decimal

        return False

    def __repr__(self):
        return f"Hostname(flag={self.flag!r},decimal={self.decimal!r})"


class ComparisonOperator(Expression, ABC):
    token: Token
    hostname: Hostname

    def __init__(self, token: Token, hostname: Hostname):
        self.token = token
        self.hostname = hostname

    def compare(self, other: Hostname) -> bool:
        return (
            self.compare_func(other.decimal, self.hostname.decimal)
            if other.flag == self.hostname.flag
            else self.compare_func(other.flag, self.hostname.flag)
        )

    def compare_func(self, left, right) -> bool:
        raise NotImplementedError

    def eval(self, env: Environment):
        if "hostname" in env:
            other: Hostname = env["hostname"]
        else:
            raise EvaluationError(
                "Hostname needed in environment to evaluate comparison."
            )

        return self.compare(other)

    @staticmethod
    def is_comparison_token(token: Token):
        return token.kind in [
            TokenKind.LESS,
            TokenKind.LESS_EQUAL,
            TokenKind.EQUAL_EQUAL,
            TokenKind.BANG_EQUAL,
            TokenKind.GREATER,
            TokenKind.GREATER_EQUAL,
        ]

    def __eq__(self, other):
        if isinstance(other, ComparisonOperator):
            return other.token == self.token and other.hostname == self.hostname

        return False


class LessOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left < right


class LessEqualOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left <= right


class EqualOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left == right


class NotEqualOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left != right


class GreaterOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left > right


class GreaterEqualOperator(ComparisonOperator):
    def compare_func(self, left, right) -> bool:
        return left >= right


class LogicalOperator(Expression, ABC):
    token: Token
    left: Expression
    right: Expression

    def __init__(self, token: Token, left: Expression, right: Expression):
        self.token = token
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, LogicalOperator):
            return (
                other.token == self.token
                and other.left == self.left
                and other.right == self.right
            )

        return False

    def __repr__(self):
        return (
            f"LogicalOperator("
            f"token={self.token!r},left={self.left!r},right={self.right!r}"
        )

    @staticmethod
    def is_logical_token(token: Token):
        return token.kind in [TokenKind.COMMA, TokenKind.BAR]


class AndOperator(LogicalOperator):
    def eval(self, env: Environment):
        return self.left.eval(env) and self.right.eval(env)


class OrOperator(LogicalOperator):
    def eval(self, env: Environment):
        return self.left.eval(env) or self.right.eval(env)


class ParseError(Exception):
    pass


class Parser:
    """
    A recursive decent parser.

    lexp: logical operators: "," logical AND; "|" logical OR
    cexp: comparison operators like "<", "==" etc.
    pexp: primitives: alpha, decimal, hostname

    grammar:
        exp   ::= lexp
        lexp  ::= cexp lexp'
        lexp' ::= "," cexp lexp' | "|" cexp lexp' | []
        cexp  ::= "<" pexp  | "<=" pexp | ... | pexp
        pexp  ::= alpha | decimal | hostname
    """

    tokens: List[Token]
    index: int

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = 0

    def consume_n(self, n: int) -> List[Token]:
        """
        Consumes given amount of `Token`s. Returns a list consisting of these tokens and
        increases the `index` by this amount.

        :param n: Integer
        :return: List of :class:`Token`s
        :rtype: List[Token]
        """
        tokens = self.tokens[self.index : self.index + n]
        self.index += n
        return tokens

    def consume(self) -> Token:
        """
        Same as consume_n but only consume 1 `Token`
        :return: :class:`Token`
        :rtype: Token
        """
        return self.consume_n(1)[0]

    def curr(self) -> Token:
        """
        Return the `Token` at the current `index`

        :return: :class:`Token` object
        :rtype: Token
        """
        return self.tokens[self.index]

    def is_exhausted(self) -> bool:
        """
        Return True if all `Token`s are parsed
        :return: Boolean
        :rtype: bool
        """
        return self.index >= len(self.tokens)

    def expect(self, token: Token) -> bool:
        """
        Returns true if the given `Token` matches the current `Token`

        :param token: Token
        :return: Boolean
        :rtype: bool
        """
        return self.curr() == token

    @staticmethod
    def make_logical_expression(
        token: Token, left: Expression, right: Expression
    ) -> LogicalOperator:
        """
        Factory method to create a `LogicalOperator` depending on the given `Token`

        :param token: Token
        :param left: Expression
        :param right: Expression
        :return: :class:`LogicalOperator`
        :rtype: LogicalOperator
        """
        if token.kind == TokenKind.COMMA:
            return AndOperator(token, left, right)
        if token.kind == TokenKind.BAR:
            return OrOperator(token, left, right)

        raise ValueError(f"Unexpected token: {token!r}")

    @staticmethod
    def make_comparison_expression(
        token: Token, hostname: Hostname
    ) -> ComparisonOperator:
        """
        Factory method to create a subclass of the `ComparisonOperator` depending on the
        given `Token`

        :param token: Token
        :param hostname: Hostname expression
        :return: :class:`ComparisonOperator`
        :rtype: ComparisonOperator
        """
        if token.kind == TokenKind.LESS:
            return LessOperator(token, hostname)
        if token.kind == TokenKind.LESS_EQUAL:
            return LessEqualOperator(token, hostname)
        if token.kind == TokenKind.EQUAL_EQUAL:
            return EqualOperator(token, hostname)
        if token.kind == TokenKind.BANG_EQUAL:
            return NotEqualOperator(token, hostname)
        if token.kind == TokenKind.GREATER:
            return GreaterOperator(token, hostname)
        if token.kind == TokenKind.GREATER_EQUAL:
            return GreaterEqualOperator(token, hostname)

        raise ValueError(f"Unexpected token: {token!r}")

    def parse(self) -> Expression:
        """
        Parses the list of `Token`s to an `Expression`. See the class documentation for
        the grammar in use.
        :return: the final Expression
        """
        expression: Expression = self._parse_expression()
        if not self.is_exhausted():
            raise ParseError("Invalid state: Tokens left after parsing.")

        return expression

    def _parse_expression(self) -> Expression:
        """
        This method is the top level parsing method and serves as anchor for lower level
        parsing methods.
        :return:
        """
        return self._parse_logical()

    def _parse_logical(self) -> Expression:
        left = self._parse_comparison()
        return self._parse_logical_prime(left)

    def _parse_logical_prime(self, expression: Expression):
        if not self.is_exhausted():
            curr_token = self.curr()
        else:
            return expression

        if LogicalOperator.is_logical_token(curr_token):
            self.consume()
            right = self._parse_comparison()
            return self._parse_logical_prime(
                self.make_logical_expression(curr_token, expression, right)
            )

        return expression

    def _parse_comparison(self) -> Expression:
        curr_token = self.curr()
        if ComparisonOperator.is_comparison_token(curr_token):
            token: Token = self.consume()
            exp: Expression = self._parse_primitive()
            if isinstance(exp, Hostname):
                return self.make_comparison_expression(token, exp)

            raise ParseError(f"Expected a valid hostname but was {exp!r}")

        return self._parse_primitive()

    def _parse_primitive(self) -> Expression:
        if not self.is_exhausted():
            curr_token = self.consume()
        else:
            raise ParseError("Invalid state: No token left to parse.")

        if curr_token.kind == TokenKind.STRING:
            return Alpha(curr_token)
        if curr_token.kind == TokenKind.NUMBER:
            return Decimal(curr_token)
        if curr_token.kind == TokenKind.HOSTNAME:
            return Hostname(curr_token)
        if curr_token.kind == TokenKind.LPAREN:
            expression = self._parse_expression()

            if not self.is_exhausted():
                curr_token = self.consume()
            else:
                raise ParseError("Missing right parentheses.")

            if curr_token.kind == TokenKind.RPAREN:
                return expression

        raise ParseError(f"Invalid token: {curr_token!r}")
