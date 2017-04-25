# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages
import pkgutil
import sys
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
	"""Post-installation for development mode."""
	def run(self):
		develop.run(self)


class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		install.run(self)

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', u'pentest', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = u'b0z'
''' % version
with open(path, 'w') as F:
	F.write(meta)

hooks_path = os.path.dirname(os.path.abspath(__file__)) + '/src/pentest/hooks'
jarvis_entry_points = {
	'console_scripts': [
		'pentest = pentest.__main__:main'
	]
}

for _, name, _ in pkgutil.iter_modules([hooks_path]):
	jarvis_entry_points['console_scripts'].append('{hook} = pentest.hooks.{hook}:main'.format(hook=name))

setup(
	# Basic info
	name=u'jarvis-pentest',
	version=version,
	author='b0z',
	author_email='bastien@faure.io',
	url='https://github.com/BastienFaure/jarvis',
	licence='MIT',
	description='The pentest companion',
	long_description=codecs.open('README.rst', 'rb', 'utf8').read(),
	cmdclass={
		'develop': PostDevelopCommand,
		'install': PostInstallCommand,
	},

	# Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Information Technology',
		'License :: OSI Approved :: MIT License',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: Software Development :: Libraries',
	],

	# Packages and dependencies
	package_dir={'': 'src'},
	packages=find_packages('src'),
	install_requires=[
            "netifaces",
            "slugify"
	],
	extras_require={
		'dev': [
			'python-boilerplate[dev]',
		],
	},

	# Other configurations
	zip_safe=False,
	platforms='any',
	# entry points
	entry_points=jarvis_entry_points,
)
