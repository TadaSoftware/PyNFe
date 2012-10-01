#!/usr/bin/env python

import sys, doctest, os, glob
from setuptools import setup, find_packages

setup(
    name='PyNFe',
    version='0.1-custom',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    zip_safe=False,
)
