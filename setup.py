#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='gtbhdsiggen',
    version='0.1',
    author='Frédéric Sureau',
    author_email='frederic.sureau@veo-labs.com',
    url='https://github.com/veo-labs/gtbhdsiggen',
    description='A python lib and tool to control Gefen HD Pattern Signal Generator on Linux',
    long_description=open('README.md').read(),
    packages=find_packages(),
    zip_safe=False,
    license='LGPL',
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
