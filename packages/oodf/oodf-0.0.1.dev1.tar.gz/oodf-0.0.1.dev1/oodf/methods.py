# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from .core import tokenize, transpile


def load(content: str) -> dict:
    """
    Load/parse an oodf string into a python dictionary.

    Parameters:
    -----------
    content: :class:`str`
        The oodf string to parse.

    Returns:
    --------
    :class:`dict`
        The parsed oodf dictionary.

    Raises:
    -------
    InvalidSyntax
        The OODF syntax is invalid. *(More specifications in error message)*
    ExpectedEOT
        No end of token was found. *(which means that the OODF string is not well-formed, and no end signature was
        found)*
    """
    return transpile(tokenize(content))
