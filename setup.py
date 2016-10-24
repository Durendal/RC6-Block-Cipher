#!/usr/bin/env python

from setuptools import setup, find_packages
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='RC6 Block Cipher',
	author='shashankrao',
	author_email='rshashank192@gmail.com',
	version='0.1dev',
	packages=find_packages(),
	license='GPL',
	description='Module for encrypting and decrypting with the rc6 block cipher',
	long_description=open('README.md').read(),
	
)


