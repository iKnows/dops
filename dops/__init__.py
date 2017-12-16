#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dops/__init__.py 
@time: 2017/12/16 21:52
"""

import platform
import sys

from dops.core.logging import logger

__version__ = '1.0'
__author__ = 'ysicing <ops.ysicing@gmail.com>'
__license__ = 'LGPLv3'


try:
    from psutil import __version__ as psutil_version
except ImportError:
    print('PSutil library not found.Dops will exit')
    sys.exit(1)


def main():

    logger.info('Start Dops {}'.format(__version__))
    logger.info('{} {} and PSutil {} detected'.format(
        platform.python_implementation(),
        platform.python_version(),
        psutil_version))

    print('hello')