#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='data',
    version='0.1',
    description='Work with unicode/non-unicode data from files or strings '
                'uniformly.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/data',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['six'],
)
