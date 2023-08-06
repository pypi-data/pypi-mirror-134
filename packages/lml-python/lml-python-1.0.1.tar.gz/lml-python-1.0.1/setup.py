#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lml(122809690@qq.com)
# Description:
# python setup.py sdist
# twine upload dist/*


from setuptools import setup, find_packages

# import setuptools
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name = 'lml-python',
    # name = ['lml-python','lml-py'],
    # packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version = '1.0.1',
    keywords='ct',
    # keywords=['ranking', 'ranking-metrics', 'ndcg', 'errs'],
    description = ['lml-python','lml-py'],
    license = 'MIT',
    url = 'https://github.com/122809690/lml_python',
    author = 'lml',
    author_email = '122809690@qq.com',
    packages = find_packages(),
    include_package_data = True,
    # platforms = 'any',
    python_requires='>=3.7',
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    # ],

    # install_requires = [
    #     'opencv-python>=4.4.0',
    #     'opencv-contrib-python>=4.4.0'
    #     ],
)