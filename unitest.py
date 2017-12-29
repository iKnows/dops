#!/usr/bin/env python3

import unittest

from dops.version import VERSION_INFO

pypi_version = dict(VERSION_INFO)['pypi']
print('Unitary tests for dops %s' % pypi_version)


class TestDops(unittest.TestCase):

    def version(self):
        print('dops version:{}'.format(pypi_version))


if __name__ == '__main__':
    unittest.main()