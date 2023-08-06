import configparser
import os
import re
import subprocess
import types

from uttl.buildout.base_recipe import BaseRecipe
from zc.buildout import UserError

class VersionCheckRecipe(BaseRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options)

		self.options.setdefault('version-file', name + '.ini')
		self.options.setdefault('required-major', '0')
		self.options.setdefault('required-minor', '0')
		self.options.setdefault('version-major', '0')
		self.options.setdefault('version-minor', '0')
		self.options.setdefault('version-debug', '0')

		# convert body into function, adapted from mr.scripty

		if not 'body' in self.options:
			raise UserError('Missing mandatory "body" option.')

		newbody = 'def checkVersion(self):\n'
		indent = True
		for line in self.options['body'].split('\n'):
			if line.startswith("..."):
				line = line[4:]
			if indent:
				newbody += "  "
				newbody += line + '\n'
			if line.startswith('"""'):
				indent = not indent

		exec(newbody, globals(), locals())
		f = types.MethodType(eval('checkVersion'), self)
		setattr(self, 'checkVersion', f)

		# version file

		self.version_file = os.path.join(buildout['buildout']['parts-directory'], self.options['version-file'])

		# check version using script method

		success, self.version_major, self.version_minor, self.version_debug, self.path = self.checkVersion()
		if not success:
			raise UserError('Failed to check version.')

		self.options['version-major'] = str(self.version_major)
		self.options['version-minor'] = str(self.version_minor)
		self.options['version-debug'] = str(self.version_debug)
		self.options['path'] = self.path

		self.log.debug('path %s version %s.%s.%s' % (self.options['path'], self.options['version-major'], self.options['version-minor'], self.options['version-debug']))

	def install(self):
		# read or create version object

		self.options.created(self.version_file)

		self.version = configparser.ConfigParser()
		if os.path.exists(self.version_file):
			self.version.read_file(open(self.version_file))
		else:
			self.version['version'] = {
				'major': '0',
				'minor': '0',
				'debug': '0'
			}

		# version check

		installed = [
			int(self.options['version-major']),
			int(self.options['version-minor']),
			int(self.options['version-debug'])
		]
		cached = [
			int(self.version['version']['major']),
			int(self.version['version']['minor']),
			int(self.version['version']['debug']),
		]
		required = [
			int(self.options['required-major']),
			int(self.options['required-minor'])
		]

		# check for newer version

		if installed[0] > cached[0] or installed[1] > cached[1] or installed[2] > cached[2]:
			self.log.info('Found new version: %d.%d.%d != %d.%d.%d' % (
				installed[0], installed[1], installed[2],
				cached[0], cached[1], cached[2])
			)

			self.version['version'] = {
				'major': str(installed[0]),
				'minor': str(installed[1]),
				'debug': str(installed[2])
			}
			self.version['location'] = {
				'path': self.options['path']
			}

			with open(self.version_file, 'w+') as f:
				self.version.write(f)

		# check version against required

		if installed[0] < required[0] or (installed[0] >= required[0] and installed[1] < required[1]):
			self.log.error('Dependency at %d.%d.%d is out of date, >= %d.%d is required' % (
				installed[0], installed[1], installed[2],
				required[0], required[1]))

			raise UserError('Version mismatch')

		return self.options.created()

	update = install

def uninstall(name, options):
	pass