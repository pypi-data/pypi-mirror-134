# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
from unittest import TestCase

from libraries.python.tests import token_types


class TestTokenTypes(TestCase):
    # If this is correct for one token, we can assume that all tokens are correct
    def test_token_types(self):
        comment_token = token_types["SINGLE-LINE-COMMENT"]
        self.assertEqual(
            comment_token.represents,
            "SINGLE-LINE-COMMENT",
            "String representation of token is a single-line comment"
        )
        self.assertEqual(comment_token.sot, "/-/", "Single-line comment start-of-token")
        self.assertEqual(comment_token.eot, "\n", "Single-line comment end-of-token")
