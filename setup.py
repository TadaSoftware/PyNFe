#!/usr/bin/env python
from setuptools import setup, find_packages
from pip.req import parse_requirements as parse

requirements = lambda f: [str(i.req) for i in parse(f, session=False)]

setup(
    name='PyNFe',
    version='0.2',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=requirements('requirements.txt'),
    zip_safe=False,
)
