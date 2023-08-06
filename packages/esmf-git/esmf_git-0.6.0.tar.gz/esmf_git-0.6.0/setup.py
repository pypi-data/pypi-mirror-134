#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

import os
import sys
import codecs
import subprocess

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


if sys.argv[-1] == "publish":
    subprocess.call(f"{sys.executable} setup.py sdist bdist_wheel upload", shell=False)
    sys.exit()

required = [""]

setup(
    name="esmf_git",
    version="0.6.0",
    description="Standard Git Library for ESMF applications.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Ryan Long",
    author_email="ryan.long@noaa.gov",
    url="",
    py_modules=["esmf_git"],
    install_requires=required,
    tests_require=["pytest", "bump2version"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
