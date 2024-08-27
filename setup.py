#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='weasel',
    version='0.4',
    description='Enter the weasel',
    long_description=open('README.md').read(),
    author='Michael Uhl',
    author_email='uhlm@informatik.uni-freiburg.de',
    url='https://github.com/michauhl/weasel',
    license='MIT',
    scripts=['bin/weasel.py'],
    packages=find_packages(exclude=['test']),
    zip_safe=False,
)
