#!/usr/bin/env python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyNFe',
    version='0.4.2',
    author='TadaSoftware',
    author_email='tadasoftware@gmail.com',
    description="Interface library with the Brazilian Electronic Invoice web services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TadaSoftware/PyNFe',
    project_urls={
        "Bug Tracker": "https://github.com/TadaSoftware/PyNFe/issues",
        "Wiki": "https://github.com/TadaSoftware/PyNFe/wiki",
        "Discussions": "https://github.com/TadaSoftware/PyNFe/discussions"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=['tests']),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=[
        'pyopenssl',
        'requests',
        'lxml',
        'signxml',
    ],
    extras_require={
        'nfse': [
            'suds-jurko',
            'pyxb==1.2.4',
        ],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
