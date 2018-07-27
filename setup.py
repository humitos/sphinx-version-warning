# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name='sphinx-version-warning',
    version='0.0.1',
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='Sphinx extension to add a warning banner',
    url='https://github.com/humitos/sphinx-version-warning',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    install_requires=[
        'munch',
        'slumber',
        'sphinx',
    ],
)
