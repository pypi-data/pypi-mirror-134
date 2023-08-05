# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import TYPE_CHECKING, Tuple

from ..exceptions import ExpectedEOT, InvalidSyntax
from ..tokens import tokens

if TYPE_CHECKING:
    from .transpiler import ValidType
    from ..tokens import TokenType
    from typing import List, Union, Dict, Any


@dataclass
class Token:
    type: TokenType
    content: Union[ValidType, List[ValidType], Dict[ValidType, Union[ValidType, Any]]]


CachedToken = Tuple[int, bool, Token]


def tokenize(content: str) -> List[Token]:
    """
    Tokenize OODF syntax.

    Parameters:
    -----------
    content: :class:`str`
        A string in OODF syntax.

    Raises:
    -------
    InvalidSyntax
        The OODF syntax is invalid and could not be tokenized.
    ExpectedEOT
        No end of token was found.
    """
    # TODO: Optimize in the future
    registered_tokens: List[Token] = []

    __tkn_cache: Dict[str, CachedToken] = {}
    __end_buffer: str = ""
    __loc: Tuple[int, int] = (0, 0)

    for row, line in enumerate(content.splitlines(True)):
        for col, char in enumerate(line):
            __loc = (row, col)
            if not __tkn_cache:
                for tt in tokens:
                    if tt.sot[0] == char:
                        __tkn_cache[tt.represents] = (0, False, Token(tt, ""))

                if not __tkn_cache and char not in ["\n", " "]:
                    raise InvalidSyntax(__loc, f"Unexpected character '{char}'")
                continue

            for tt, (current, end, token) in deepcopy(__tkn_cache).items():
                if len(token.type.sot) <= current + 1:
                    end = True
                elif not end:
                    current += 1

                    if char != token.type.sot[current]:
                        del __tkn_cache[tt]

                        if not __tkn_cache:
                            raise InvalidSyntax(
                                __loc,
                                f"Unexpected character {repr(char)}, expected {repr(token.type.sot[current])}"
                            )
                        continue

                if end:
                    if current + 1 > len(token.type.eot):
                        current = 0

                    if token.type.eot[current] == char:
                        __end_buffer += char
                        current += 1

                        if current >= len(token.type.eot):
                            token.content = token.content.strip()
                            registered_tokens.append(token)
                            __end_buffer = ""
                            __tkn_cache = {}
                            continue
                    else:
                        current = 0

                        if __end_buffer:
                            token.content += __end_buffer
                            __end_buffer = ""

                        token.content += char

                __tkn_cache[tt] = (current, end, token)

    if __tkn_cache:
        token = list(__tkn_cache.values())[0][2]
        raise ExpectedEOT(__loc, f"Expected end of token ({repr(token.type.eot)}) for {repr(token.type.represents)}")

    return registered_tokens
