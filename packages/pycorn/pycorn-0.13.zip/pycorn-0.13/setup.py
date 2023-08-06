#!/usr/bin/env python
from setuptools import setup

setup(
    name='pycorn',
    version='0.13',
    author='Yasar L. Ahmed',
    packages=['pycorn',],
    scripts=['examplescripts/pycorn-bin.py'],
    license='GNU General Public License v2 (GPLv2)',
    description='A script to extract data from UNICORN result (res) files',
    long_description=open('README.rst').read(),
    url='https://github.com/pyahmed/PyCORN',
)
