#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 15:41
# @Author  : zico.guo
# @Site    :
# @File    : setup.py
# @Software: PyCharm
# @Description:

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="new_lib",
    version="0.0.1",
    author="zico.guo",
    description="yes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
