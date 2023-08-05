# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

tokens: List[TokenType] = []


@dataclass
class TokenType:
    represents: str  # The string representation of the token

    sot: str  # start of token
    eot: str  # end of token

    def __post_init__(self):
        tokens.append(self)


"""
All token types, defines the behaviour of the language.
"""

# Comments
TokenType("SINGLE-LINE-COMMENT", "/-/", "\n")
TokenType("MULTI-LINE-COMMENT", "/--", "--/")

# Keynotes
TokenType("SINGLE-LINE-KEYNOTE", "/!/", "\n")
TokenType("MULTI-LINE-KEYNOTE", "/!!", "!!/")
