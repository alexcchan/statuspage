#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'statuspage',
	version = '0.0.0',
	packages = ['statuspage'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/statuspage/tree/master',
	keywords = 'statuspage api',
	description = 'StatusPage API Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


