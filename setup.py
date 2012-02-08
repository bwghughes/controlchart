#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import controlchart

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

if sys.argv[-1] == "test":
    os.system("python test_controlchart.py")
    sys.exit()

required = []

setup(
    name='controlchart',
    version=controlchart.__version__,
    description='Control Charts for Humans.',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='http://variat.io/',
    packages= [
        'controlchart',
    ],
    install_requires=required,
    license='ISC',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
