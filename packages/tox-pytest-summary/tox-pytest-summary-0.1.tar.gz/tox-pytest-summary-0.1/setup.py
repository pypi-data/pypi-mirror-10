#!/usr/bin/env python

from setuptools import setup

__version__ = '0.1'

CLASSIFIERS = map(str.strip,
"""Environment :: Console
License :: OSI Approved :: GNU Affero General Public License v3
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Testing
""".splitlines())

setup(
    name="tox-pytest-summary",
    version=__version__,
    author="Federico Ceratto",
    author_email="federico.ceratto@gmail.com",
    description="Tox + Py.test summary",
    license="AGPLv3",
    url="https://github.com/FedericoCeratto/tox-pytest-summary",
    long_description="Tox + Py.test summary generator",
    classifiers=CLASSIFIERS,
    install_requires=[
        'xmltodict',
    ],
    py_modules=['tox_summary'],
    platforms=['Linux'],
)
