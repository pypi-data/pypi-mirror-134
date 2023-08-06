#!/usr/bin/env python
# coding: utf-8

import os

a = os.system("cd Abhi_pdf && touch xxx.log")

from setuptools import setup, find_packages
setup(
    name='Abhi_pdf',
    version='7.3',
    author='Tector Pro',
    description='Testing something',
    packages=find_packages(),
    install_requires = []
    #entry_points={
    #    'console_scripts': [
    #        'ls = Abhi_pdf:main'
    #        ]
    #    }
)
