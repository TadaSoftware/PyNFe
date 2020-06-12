#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='PyNFe',
    version='0.4',
    author='TadaSoftware',
    author_email='tadasoftware@gmail.com',
    url='https://github.com/TadaSoftware',
    packages=setuptools.find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=[
        'pyopenssl',
        'requests',
        'lxml',
        'signxml',
    ],
    zip_safe=False,
    python_requires='>=3.6',
)
