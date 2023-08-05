# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from unittest import TestCase

from libraries.python.oodf import load
from libraries.python.oodf.core import tokenize
from libraries.python.oodf.core.lexer import Token
from libraries.python.oodf.exceptions import InvalidSyntax, ExpectedEOT
from libraries.python.tests import token_types
from libraries.python.tests.utils import get_sample


class TestComments(TestCase):
    data = get_sample("comments")
    tokens = [
        Token(token_types["SINGLE-LINE-COMMENT"], "Welcome to oodf"),
        Token(
            token_types["MULTI-LINE-COMMENT"],
            "A simple, yet effective way to grant your config files access to the power of objects.\n"
            "If you have any suggestions, please let us know by creating a pull request."
        )
    ]

    def test_comments_tokenize(self):
        self.assertEqual(self.tokens, tokenize(self.data), "Should tokenize comments")

    def test_comments_parse(self):
        self.assertEqual({}, load(self.data), "Comments should be removed for parsing to a python dictionary")

    def test_keynotes_raises_invalid_syntax(self):
        self.assertRaises(InvalidSyntax, tokenize, "/- This is not a valid syntax\n")
        self.assertRaises(InvalidSyntax, tokenize, "/-\nThis is not a valid syntax!\n-/")

    def test_keynotes_raises_expected_eot(self):
        self.assertRaises(ExpectedEOT, tokenize, "/-/ EOT is not in place")
        self.assertRaises(ExpectedEOT, tokenize, "/--\nEOT is not in place\n")
