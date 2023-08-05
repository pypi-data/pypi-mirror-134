#!/usr/bin/env python

"""Packaging script."""

from setuptools import setup, find_packages
from os.path import splitext
from os.path import basename
from glob import glob

__author__ = "Carsten Rambow"
__copyright__ = "Copyright 2021-present, Carsten Rambow (spps.dev@elomagic.de)"
__license__ = "Apache-2.0"

with open('README.md') as f:
    readme = f.read()

setup(
    name="spps-py",
    version="1.0.0rc1",
    description="Simple Password Protection Solution for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Carsten Rambow",
    author_email="spps.dev@elomagic.de",
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Security',
                 'Topic :: Security :: Cryptography',
                 'Topic :: Software Development'],
    url="https://github.com/elomagic/spps-py",
    project_urls={
        'Source': 'https://github.com/elomagic/spps-py',
        'Tracker': 'https://github.com/elomagic/spps-py/issues'
    },
    license="Apache-2.0",
    python_requires=">=3.9",
    install_requires=[
        'pycryptodome>=3.10.1'
    ],
    keywords=["encrypt", "decrypt", "password", "security", "hide", "protect", "key", "secret", "AES", "GCM"],
    package_dir={'': 'src'},
    packages=find_packages(
        where='src',
        exclude=["contrib", "docs", "tests*", "tasks"]
    ),
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    setup_requires=[
        'pytest-runner'
    ]
)
