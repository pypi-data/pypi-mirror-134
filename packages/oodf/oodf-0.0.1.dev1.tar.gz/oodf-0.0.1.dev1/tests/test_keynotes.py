# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from unittest import TestCase

from libraries.python.oodf import load
from libraries.python.oodf.core import tokenize
from libraries.python.oodf.core.lexer import Token
from libraries.python.oodf.exceptions import InvalidSyntax, ExpectedEOT
from libraries.python.tests import token_types
from libraries.python.tests.utils import get_sample

a_beautiful_day_text = """
I don't know why
You think that you could hold me
When you couldn't get by by yourself
And I don't know who
Would ever want to tear the seam of someone's dream

Baby, it's fine, you said that we should just be friends
While I came up with that line and I'm sure
That it's for the best
If you ever change your mind, don't hold your breath

'Cause you may not believe
That baby, I'm relieved, hmm
When you said goodbye, my whole world shines

Hey hey hey
It's a beautiful day and I can't stop myself from smiling
If we're drinking, then I'm buying
And I know there's no denying
It's a beautiful day, the sun is up, the music's playing
And even if it started raining
You won't hear this boy complaining
'Cause I'm glad that you're the one who got away
It's a beautiful day

It's my turn to fly, so girls, get in line
'Cause I'm easy, no playing this guy like a fool
Now I'm alright
Might've had me caged before, but not tonight

And you may not believe, hmm
That baby, I'm relieved
This fire inside, it burns too bright
I don't want to say "So long", I just want to say "Goodbye"

It's a beautiful day and I can't stop myself from smiling
If we're drinking, then I'm buying
And I know there's no denying
That it's a beautiful day, the sun is up, the music's playing
And even if it started raining
You won't hear this boy complaining
'Cause I'm glad that you're the one who got away, hmm

'Cause if you ever think I'll take up
My time with thinking of our break-up
Then, you've got another thing coming your way
'Cause it's a beautiful day

Beautiful day
Oh, baby, any day that you're gone away
It's a beautiful day

~ Michael Bublé - It's a Beautiful Day
"""


class TestKeynotes(TestCase):
    data = get_sample("keynotes")
    tokens = [
        Token(token_types["SINGLE-LINE-KEYNOTE"], "What a beautiful day it is, am I right?"),
        Token(token_types["MULTI-LINE-KEYNOTE"], a_beautiful_day_text.strip())
    ]

    def test_keynotes_tokenize(self):
        self.assertEqual(self.tokens, tokenize(self.data), "Should tokenize keynotes")

    def test_keynotes_parse(self):
        self.assertEqual({}, load(self.data), "Keynotes should be removed for parsing to a python dictionary")

    def test_keynotes_raises_invalid_syntax(self):
        self.assertRaises(InvalidSyntax, tokenize, "/! This is not a valid syntax\n")
        self.assertRaises(InvalidSyntax, tokenize, "/!\nThis is not a valid syntax\n!/")

    def test_keynotes_raises_expected_eot(self):
        self.assertRaises(ExpectedEOT, tokenize, "/!/ EOT is not in place")
        self.assertRaises(ExpectedEOT, tokenize, "/!!\nEOT is not in place\n")
