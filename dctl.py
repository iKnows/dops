#!/usr/bin/env python3
# coding=utf-8

import dops
import sys

if __name__ == '__main__':
    try:
        sys.exit(dops.main())
    except KeyboardInterrupt:
        print("exit....")
