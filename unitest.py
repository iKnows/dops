#!/usr/bin/env python3

import unittest

from dops.version import VERSION_INFO
from dops.plugins.node import NodeInfo, SystemInfo

pypi_version = dict(VERSION_INFO)['pypi']
print('Unitary tests for dops %s' % pypi_version)


class TestDops(unittest.TestCase):

    def test_001_version(self):
        print('dops version:{}'.format(pypi_version))

    def test_002_node_info(self):
        n = NodeInfo()
        s = SystemInfo()
        print("System info: {}".format(s.get_sysinfo()))


if __name__ == '__main__':
    unittest.main()