#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subarg
from setuptools import setup, find_packages

setup(name='subarg',
      version=subarg.__version__,
      description=subarg.__desc__,
      author=subarg.__author__,
      author_email=subarg.__author_email__,
      url=subarg.__url__,
      packages=find_packages())
