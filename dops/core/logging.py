#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dops/logs.py 
@time: 2017/12/16 23:46
"""

import time
import logging
import platform
import logging.config
from datetime import datetime
from dops.config import Configlog


system = platform.system().lower()

if system == 'darwin':
    LOG_FILE = '/tmp/dops.log'
else:
    LOG_FILE = '/var/log/dops.log'


def dops_logger(env_key='LOG_FILE'):

    _logger = logging.getLogger()

    config = Configlog

