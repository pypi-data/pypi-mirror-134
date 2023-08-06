#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

setup(name='jiaguup',
      version='0.2.3',
      description='jiaguup Natural Language Processing, fix for tensorflow2',
      author='William.Du',
      author_email='duyq0519@outlook.com',
      url='https://github.com/willsdu/jiaguup',
      license='MIT',
      packages=['jiaguup'],
      package_dir={'jiaguup': 'jiaguup'},
      package_data={'jiaguup': ['*.*', 'cluster/*', 'data/*', 'model/*',
		'normal/*', 'segment/*', 'segment/dict/*','segment/model/*',
		'sentiment/*', 'sentiment/model/*', 'topic/*']}
      )
