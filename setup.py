#!/usr/bin/env python

import os
import re
import sys
from io import open

from setuptools import setup, find_packages


if sys.version_info < (3, 5) or sys.version_info[:3] < (2, 7, 13):
    print('Dops requires at least Python 3.6 or Python 2.7.13 to run.')
    sys.exit(1)


from dops.version import  VERSION_INFO
version = dict(VERSION_INFO)['pypi']
if not version:
    raise RuntimeError('Cannot find Dops version information.')

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


def get_data_files():
    data_files = [
        ('share/doc/dops', ['README.rst'])
    ]

    return data_files


def get_install_requires():
    requires = ['psutil>=5.4.2']
    if sys.platform.startswith('win'):
        requires.append('bottle')

    return requires

setup(
    name='dops',
    version=version,
    description="Dops tool",
    long_description=long_description,
    author='ysicing',
    author_email='ops.ysicing@gmail.com',
    url='https://github.com/ysicing/dops',
    license='LGPLv3',
    keywords="cli dops system",
    install_requires=get_install_requires(),
    #packages=['dops'],
    packages=find_packages(),
    include_package_data=True,
    data_files=get_data_files(),
    entry_points={"console_scripts": ["dops=dops:main"]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console :: Curses',
        'Environment :: Web Environment',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring'
    ]
)