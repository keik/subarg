#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='subarg',
      version='1.0.1',
      description="""Parse sub-arguments in `[` and `]` recursively""",
      author='keik',
      author_email='k4t0.kei@gmail.com',
      url='https://github.com/keik/subarg',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
      packages=find_packages())
