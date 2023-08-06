#!/usr/bin/env python

from setuptools import setup

setup(
    name='colibri2trilegal',
    author='Phil Rosenfield',
    author_email='philip.rosenfield@unipd.it',
    version='1.3',
    py_modules=['colibri2trilegal'],
    scripts=['colibri2trilegal'],
    install_requires=['matplotlib', 'numpy']
)