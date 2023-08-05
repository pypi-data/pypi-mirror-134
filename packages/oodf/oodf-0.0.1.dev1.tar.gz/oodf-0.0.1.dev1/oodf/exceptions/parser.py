# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
from typing import Tuple

from .base import OODFException


class ParserException(OODFException):
    """Represents an exception which occurs during the parsing of OODF syntax."""

    def __init__(self, location: Tuple[int, int], message: str):
        self.line = location[0] + 1
        self.column = location[1] + 1
        super().__init__(f"[{self.line}:{self.column}] {message}")


class InvalidSyntax(ParserException):
    """Exception thrown when syntax does not match the expected syntax/is invalid OODF."""


class ExpectedEOT(InvalidSyntax):
    """Exception thrown when the EOF is reached but no EOT was found."""
