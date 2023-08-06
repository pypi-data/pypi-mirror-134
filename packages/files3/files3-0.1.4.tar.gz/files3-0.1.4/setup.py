#!/usr/bin/env python
# coding:utf-8

from setuptools import find_packages, setup

setup(
name='files3',
version='0.1.4',
description='(pickle based) save Python objects in binary to the file system and manage them (more convenient?)',
author_email='2229066748@qq.com',
maintainer="Eagle'sBaby",
maintainer_email='2229066748@qq.com',
packages=find_packages(),
platforms=["all"],
license='Apache Licence 2.0',
classifiers=[
'Programming Language :: Python',
'Programming Language :: Python :: 3',
],
keywords = ['file', 'pickle', 'bin'],
python_requires='>=3',
package_data={"":["pyfilehash.pyd"]},
install_requires=[
    'pycparser',
    'pycryptodome',
],
)
