#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='quick-arguments',
    version='0.0.2',
    description='A simple argument parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Thomas Ellison',
    author_email='thomasjlsn@gmail.com',
    url='https://gitlab.com/thomasjlsn/qargs',
    packages=['qargs'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
    ]
)
