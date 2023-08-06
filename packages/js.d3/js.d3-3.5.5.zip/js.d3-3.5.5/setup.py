#!/usr/bin/python

import setuptools
from setuptools import find_packages

setuptools.setup(
    name='js.d3',
    version='3.5.5',
    license='BSD',
    description='Fanstatic package for D3.js',
    long_description=open('README.rst').read(),
    author='Matt Good',
    author_email='matt@matt-good.net',
    url='https://github.com/fanstatic/js.d3/',
    platforms='any',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
    ],
    setup_requires=[
        'setuptools-git',
    ],
    entry_points={
        'fanstatic.libraries': [
            'd3=js.d3:library',
        ],
    },
)
