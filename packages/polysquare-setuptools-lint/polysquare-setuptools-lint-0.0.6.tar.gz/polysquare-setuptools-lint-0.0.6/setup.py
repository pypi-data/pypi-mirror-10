# /setup.py
#
# Installation and setup script for polysquare-setuptools-lint
#
# See /LICENCE.md for Copyright information
"""Installation and setup script for polysquare-setuptools-lint."""

from polysquare_setuptools_lint import (PolysquareLintCommand,
                                        can_run_frosted,
                                        can_run_pychecker,
                                        can_run_pylint)

from setuptools import find_packages
from setuptools import setup

ADDITIONAL_LINTERS = list()
ADDITIONAL_DEPENDENCY_LINKS = list()

# Don't install linters unless we can run them on this platform.
if can_run_pychecker():
    ADDITIONAL_LINTERS += ["pychecker"]
    ADDITIONAL_DEPENDENCY_LINKS += [
        ("http://downloads.sourceforge.net/project/pychecker/pychecker/0.8.19/"
         "pychecker-0.8.19.tar.gz#egg=pychecker-0.8.19")
    ]

if can_run_pylint():
    ADDITIONAL_LINTERS += ["pylint", "pylint-common"]

if can_run_frosted():
    ADDITIONAL_LINTERS += ["frosted"]

setup(name="polysquare-setuptools-lint",
      version="0.0.6",
      description="""Provides a 'polysquarelint' command for setuptools""",
      long_description_markdown_filename="README.md",
      author="Sam Spilsbury",
      author_email="smspillaz@gmail.com",
      url="http://github.com/polysquare/polysquare-setuptools-lint",
      classifiers=["Development Status :: 3 - Alpha",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.1",
                   "Programming Language :: Python :: 3.2",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Build Tools",
                   "License :: OSI Approved :: MIT License"],
      license="MIT",
      keywords="development linters",
      packages=find_packages(exclude=["test"]),
      cmdclass={
          "polysquarelint": PolysquareLintCommand
      },
      install_requires=[
          "setuptools",
          "parmap",
          "pep8",
          "dodgy",
          "mccabe",
          "pep257",
          "pyflakes",
          "pyroma",
          "vulture",
          "prospector>=0.10.1",
          "flake8==2.3.0",
          "flake8-blind-except",
          "flake8-docstrings",
          "flake8-double-quotes",
          "flake8-import-order",
          "flake8-todo",
          "six"
      ] + ADDITIONAL_LINTERS,
      dependency_links=[
          ("https://github.com/smspillaz/prospector/tarball/fix-116-builds"
           "#egg=prospector-0.10.1")
      ] + ADDITIONAL_DEPENDENCY_LINKS,
      extras_require={
          "green": [
              "mock",
              "nose",
              "nose-parameterized",
              "setuptools-green",
              "testtools"
          ],
          "upload": ["setuptools-markdown"]
      },
      entry_points={
          "distutils.commands": [
              ("polysquarelint=polysquare_setuptools_lint:"
               "PolysquareLintCommand"),
          ]
      },
      zip_safe=True,
      include_package_data=True)
