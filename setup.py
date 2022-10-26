#!/usr/bin/env python3

from setuptools import setup


setup(
    name='weasel',
    version='0.2',
    description='Enter the weasel',
    long_description=open('README.md').read(),
    author='Michael Uhl',
    author_email='uhlm@informatik.uni-freiburg.de',
    url='https://github.com/michauhl/weasel',
    license='MIT',
    scripts=['bin/weasel.py'],
    zip_safe=False,
)
