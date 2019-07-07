#!/usr/bin/env python
#
# This file is part of the snmplabs.com web-site contents.
#
# Copyright (c) 2017-2019, Ilya Etingof <etingof@gmail.com>
#

from setuptools import setup


classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.4
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Communications
Topic :: System :: Monitoring
Topic :: System :: Networking :: Monitoring
"""

params = {
    'zip_safe': True,
    'name': 'snmplabs.com',
    'version': '0.0.1',
    'description': 'snmplabs.com site contents',
    'maintainer': 'Ilya Etingof <etingof@gmail.com>',
    'author': 'Ilya Etingof',
    'author_email': 'etingof@gmail.com',
    'url': 'https://github.com/etingof/snmplabs.com',
    'platforms': ['any'],
    'classifiers': [x for x in classifiers.split('\n') if x],
    'license': 'BSD',
}

setup(**params)
