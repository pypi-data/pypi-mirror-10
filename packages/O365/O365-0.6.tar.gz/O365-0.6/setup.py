#!/usr/bin/env python

from distutils.core import setup
setup(name='O365',
	version='0.6',
	description='Python library for working with Microsoft Office 365',
	author='Toben Archer',
	author_email='sandslash+O365@gmail.com',
	maintainer='Toben Archer',
	maintainer_email='sandslash+O365@gmail.com',
	url='https://github.com/Narcolapser/python-o365',
	packages=['O365'],
	install_requires=['requests'],
	license='Apache 2.0'
	)

