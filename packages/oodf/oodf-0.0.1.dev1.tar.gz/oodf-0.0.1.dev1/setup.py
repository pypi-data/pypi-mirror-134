# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
import os

from setuptools import setup

from oodf.__lib__ import __version__, __package__, __description__, __author__, __license__, __author_email__

ori_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir("./libraries/python")

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

if __name__ == "__main__":
    setup(
        name=__package__,
        version=__version__,
        description=__description__,
        author=__author__,
        author_email=__author_email__,
        license=__license__,
        install_requires=requirements,
        zip_safe=False,
        include_package_data=True,
    )

os.chdir(ori_dir)
