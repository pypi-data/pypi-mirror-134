# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

"""
Test suites for the oodf library.
"""
from typing import Dict

from libraries.python.oodf import tokens
from libraries.python.oodf.tokens import TokenType

# TokenTypes used for easy access to the token types.
token_types: Dict[str, TokenType] = {t.represents: t for t in tokens}
