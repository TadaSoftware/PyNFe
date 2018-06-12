#!/usr/bin/env python
from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements as parse
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements as parse

requirements = lambda f: [str(i.req) for i in parse(f, session=False)]

setup(
    name='PyNFe',
    version='0.4',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=requirements('requirements.txt'),
    zip_safe=False,
)
