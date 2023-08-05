# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

__version_major__ = 0
__version_minor__ = 0
__version_patch__ = 1
__version_extra__ = "dev"
__version_ident__ = 1
__version__ = ".".join(map(str, [__version_major__, __version_minor__, __version_patch__])) + \
              (f".{__version_extra__}{__version_ident__}" if __version_extra__ else "")

__package__ = "oodf"
__title__ = "Oodf Python Implementation"
__description__ = "A library for interacting with oodf (object oriented data format/file) in python."
__author__ = "Arthurdw"
__author_email__ = "mail@arthurdw.com"
__license__ = "MIT"
