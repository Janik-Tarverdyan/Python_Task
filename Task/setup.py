#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages


def read_dependencies(filename):
    global line
    dependencies = []
    with open(filename) as f:
        for line in f.readlines():
            if not line or line.startswith('#'):
                continue
            dependencies.append(line.strip())
        return dependencies


setup(
    name="Task",
    version='1.0',
    author='Janik Tarverdyan',
    author_email='Mr.Tarverdyan@yandex.com',
    packages=find_packages(sys.modules['__main__'].__file__),
    include_package_data=True,
    install_requires=read_dependencies('requirements.txt'),
)
