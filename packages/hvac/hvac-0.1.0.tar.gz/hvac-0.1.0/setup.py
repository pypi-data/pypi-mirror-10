#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='hvac',
    version='0.1.0',
    description='Hashicorp Vault API client',
    author='Ian Unruh',
    author_email='ianunruh@gmail.com',
    url='https://github.com/ianunruh/hvac',
    keywords=['hashicorp', 'vault'],
    packages=find_packages(),
    install_requires=[
        'requests',
        'six',
    ],
)
