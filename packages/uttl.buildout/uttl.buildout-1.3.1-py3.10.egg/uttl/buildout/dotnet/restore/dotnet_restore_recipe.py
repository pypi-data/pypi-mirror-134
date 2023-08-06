import os.path
import re

from uttl.buildout.dotnet.dotnet_recipe import DotnetRecipe
from zc.buildout import UserError

class DotnetRestoreRecipe(DotnetRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options)

		# synonyms

		if 'config-file' in self.options:
			self.options['config-path'] = self.options['config-file']

		if 'packages-path' in self.options:
			self.options['packages-dir'] = self.options['packages-path']

		# arguments

		self.args += [ 'restore' ]

		# project-path

		if not 'project-path' in self.options:
			raise UserError('Missing mandatory "project-path" option.')

		self.args += [ os.path.abspath(self.options['project-path']) ]

		if 'config-path' in self.options:
			self.args += [ '--configfile', os.path.abspath(self.options['config-path']) ]

		if 'parallel' in self.options and self.options['parallel'] == '0':
			self.args += [ '--disable-parallel' ]

		if 'force' in self.options:
			self.args += [ '--force' ]

		if 'force-evaluate' in self.options:
			self.args += [ '--force-evaluate' ]

		if 'ignore-failed-sources' in self.options:
			self.args += [ '--ignore-failed-sources' ]

		if 'interactive' in self.options:
			self.args += [ '--interactive' ]

		if 'lock-file-path' in self.options:
			self.args += [ '--lock-file-path', self.options['lock-file-path'] ]

		if 'locked-mode' in self.options:
			self.args += [ '--locked-mode' ]

		if 'cache' in self.options and self.options['cache'] == '0':
			self.args += [ '--no-cache' ]

		if 'dependencies' in self.options and self.options['dependencies'] == '0':
			self.args += [ '--no-dependencies' ]

		if 'packages-dir' in self.options:
			self.args += [ '--packages', os.path.abspath(self.options['packages-dir']) ]

		if 'runtime' in self.options:
			self.args += [ '--runtime', self.options['runtime'] ]

		if 'source' in self.options:
			self.args += [ '--source', self.options['source'] ]

		if 'use-lock-file' in self.options:
			self.args += [ '--use-lock-file' ]

		if 'verbosity' in self.options:
			level = self.options['verbosity']

			if not any(level in v for v in ['quiet', 'minimal', 'normal', 'detailed', 'diagnostic']):
				raise UserError('Invalid verbosity level specified.')

			self.args += [ '--verbosity', level ]

		self.options['args'] = ' '.join(str(e) for e in self.args)

def uninstall(name, options):
	pass