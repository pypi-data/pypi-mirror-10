# -*- coding: utf-8 -*-
from distutils.core import setup

version = '0.2.1'

setup(
    name="amazon-mws",
    version=version,
    description="A python interface for Amazon MWS",
    long_description=open('README.md', 'rt').read(),
    author="Juozas Kaziukenas",
    author_email="juozas@juokaz.com",
    url="https://github.com/juokaz/python-amazon-mws",
    packages=['mws'],
    platforms=['OS Independent'],
    license='LICENSE.txt'
)
