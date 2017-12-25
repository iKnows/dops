#!/usr/bin/env bash

pip3 install twine

python3 setup.py sdist bdist_wheel

twine upload dist/*

rm -rf ./build/
rm -rf ./dist/
rm -rf ./dops.egg-info/