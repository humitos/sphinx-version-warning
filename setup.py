# -*- coding: utf-8 -*-

import setuptools
import versionwarning

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sphinx-version-warning',
    version=versionwarning.version,
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='Sphinx extension to add a warning banner',
    url='https://github.com/humitos/sphinx-version-warning',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    zip_safe=False,
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
