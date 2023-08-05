# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from typing import Dict, Any, List, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lexer import Token

ValidType = Union[str, int, float, bool, None]
TranspiledContent = Dict[ValidType, Union[ValidType, Dict[ValidType, Any]]]


def transpile(tokens: List[Token]) -> TranspiledContent:
    """
    Transpile a collection of tokens into a python dictionary.

    Parameters:
    -----------
    tokens: List[:class:`oodf.core.lexer.Token`]
        The collection of tokens whom must be transpiled.
        This collection can be retrieved through the lexer output. (tokenize)
    """
    # TODO: Implement transpiler

    transpiled: TranspiledContent = {}

    # Ignore keynotes & comments
    def should_ignore(tk: Token) -> bool:
        for keyword in ["keynote", "comment"]:
            if keyword in tk.type.represents.lower():
                return False
        return True

    tokens = filter(should_ignore, tokens)

    # TODO: Implement transpiler
    for token in tokens:
        pass

    return transpiled
