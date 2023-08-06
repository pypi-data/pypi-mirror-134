#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 7:06 PM
@Author         : JQS
@File           : setup.py
@Introduction   : setup
"""

from setuptools import setup

setup(
    name='hocv',
    version='0.0.7',
    author='JQS',
    author_email='ink_fishing@protonmail.com',
    description='Python科学计算大作业',
    packages=['hocv'],
    url='https://github.com/swpfY/hocv.git',
    install_requires=['opencv-python', 'gradio'],
    entry_points={
        'console_scripts':[
            'hocv=hocv.main:index'
        ]
    }
)
