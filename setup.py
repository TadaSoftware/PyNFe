#!/usr/bin/env python

import sys, doctest, os, glob
from setuptools import setup, find_packages

setup(
    name='PyNFe',
    version='0.2',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    zip_safe=False,
)
