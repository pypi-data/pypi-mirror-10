#!/bin/sh

sed -i "/__version__/s/'.*'/'$1'/" addcourse/version.py
git commit -a -m "version bump to v$1"
git tag -s "v$1" -m "version $1"
python setup.py sdist bdist_egg bdist_rpm
python3 setup.py bdist_egg bdist_rpm
twine upload dist/*

