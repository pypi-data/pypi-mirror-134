#!/usr/bin/python
# -*- coding: UTF-8 -*-


from setuptools import setup
# from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='py2c',
    # 打包文件的名称，默认与py2c.py在同一路径下
    ext_modules=cythonize(r'D:\BCZX\RPA\self\GExecutor\main\test.py')
)