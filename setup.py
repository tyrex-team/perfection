#!/usr/bin/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from perfection import __version__

setup(
    name='perfection-tyrex',
    version=__version__,
    url='https://github.com/tyrex-team/perfection',
    license='MIT',
    author='Eddie Antonio Santos',
    author_email='easantos@ualberta.ca',
    maintainer="Thomas Calmant",
    maintainer_email="thomas.calmant@inria.fr",
    description='Perfect hashing utilities for Python',
    long_description=open('README.rst').read(),
    packages=['perfection',],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
