#!/usr/bin/env python

from distutils.core import setup

try:
    import setuptools
except ImportError, _:
    pass # No 'develop' command, oh well.

version = '0.1'

setup(name='ddby',
    version=version,
    description='Library for handling Money.',
    author="Brian O'Connor",
    author_email='brian@btoconnor.net',
    url='http://btoconnor.net',
    packages=['ddby'],
    long_description="""
    Deal with money objects, exchange values, and currencies in a pythonic way.
    """.strip(),
    license="MIT",
    platforms=["any"],
)
