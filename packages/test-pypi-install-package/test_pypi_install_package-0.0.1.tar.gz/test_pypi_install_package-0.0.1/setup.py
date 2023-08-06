#!/usr/bin/env python
# encoding: utf-8
"""
@time: 2022/1/11 17:38
"""
from setuptools import setup
import setuptools
import test_pypi_package


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setup(
    name='test_pypi_install_package',
    version='0.0.1',
    packages=setuptools.find_packages(),
    author='xiaosa',
    author_email='xiaosa.yjh@alibaba-inc.com',
    url='https://code.alipay.com/xiaosa.yjh/auto_insight',
    description='test pypi package',
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)











