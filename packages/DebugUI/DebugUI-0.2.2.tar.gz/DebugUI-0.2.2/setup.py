#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='DebugUI',
    author='luyou',
    url='https://github.com/alibaba/MNN',
    description='DebugUI python sdk',
    version='0.2.2',
    platforms=['many'],
    packages=['DebugUI'
              ],
    install_requires=[
      "Pillow",
      "streamlit>=0.55.2"
    ]
)