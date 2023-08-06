import os.path
import re

from uttl.buildout.command_recipe import CommandRecipe
from zc.buildout import UserError

class CmakeRecipe(CommandRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options, executable='cmake')

		# synonyms

		if 'source-path' in self.options:
			self.options['source-dir'] = self.options['source-path']

		if 'install-path' in self.options:
			self.options['install-dir'] = self.options['install-path']

		if 'configure-path' in self.options:
			self.options['configure-dir'] = self.options['configure-path']

		if 'build-path' in self.options:
			self.options['build-dir'] = self.options['build-path']

		# source

		source_dir = None

		if 'source-dir' in self.options:
			source_dir = os.path.abspath(self.options['source-dir'])
		elif 'install-dir' in self.options:
			source_dir = os.path.abspath(self.options['install-dir'])

		if not source_dir:
			raise UserError('Missing either "source-path" or "install-path" option.')

		# generator

		if 'generator' in self.options:
			self.args += [ '-G', self.options['generator'] ]

		# configure or build

		self.configure_dir = None

		if 'configure-dir' in self.options:
			if not 'generator' in self.options:
				raise UserError('Missing mandatory "generator" option.')

			self.configure_dir = os.path.abspath(self.options['configure-dir'])

			self.args += [ '-S', source_dir ]

			self.args += [ '-B', self.configure_dir ]
		else:
			if not 'build-dir' in self.options:
				raise UserError('Missing mandatory "build-dir" option.')

			self.args += [ '--build', os.path.abspath(self.options['build-dir']) ]

			if 'target' in self.options:
				self.args += [ '--target', self.options['target'] ]
			elif 'targets' in self.options:
				targets = self.options['targets'].splitlines()
				self.args += [ '--target', ' '.join(str(t) for t in targets) ]

			if 'config' in self.options:
				self.args += [ '--config', self.options['config'] ]

		# combine arguments

		self.options['args'] = ' '.join(str(e) for e in self.args)

		# artefacts

		if 'artefact-path' in self.options:
			self.artefacts += [ os.path.abspath(self.options['artefact-path']) ]

		# variables

		self.var_args = []

		if 'install-dir' in self.options:
			install_dir = os.path.abspath(self.options['install-dir'])
			self.options['var-CMAKE_INSTALL_PREFIX'] = os.path.abspath(install_dir) + ':PATH'

		split_name = re.compile(r'var-(.+)')
		split_type = re.compile(r'(.+):(\w*)$')

		for var in [var for var in list(self.options.keys()) if var.startswith('var-')]:
			# get name

			match = split_name.match(var)
			if not match:
				raise UserError('Failed to split variable name for "%s".' % (var))

			var_name = match.group(1)

			# get type and value

			var_value = self.options[var]

			match = split_type.match(var_value)
			if match:
				var_value = match.group(1)
				var_type = match.group(2)
			else:
				var_value = var_value
				var_type = 'STRING'

			if not any(var_type in t for t in ['BOOL', 'FILEPATH', 'PATH', 'STRING', 'INTERNAL']):
				raise UserError('Invalid variable type "%s" for "%s".' % (var_type, var))

			self.var_args += [ '-D%s:%s=%s' % (var_name, var_type, var_value) ]

		if len(self.var_args) > 0:
			if not 'generator' in self.options:
				raise UserError('Missing mandatory "generator" parameter.')

			self.var_args += [ '-G', self.options['generator'] ]

			self.var_args += [ '-S', source_dir ]

			self.var_args += self.additional_args

	def command_install(self):
		# change to configure directory

		prev_dir = None
		if self.configure_dir:
			prev_dir = os.getcwd()

			if not os.path.exists(self.configure_dir):
				os.makedirs(self.configure_dir, 0o777, True)

			os.chdir(self.configure_dir)

		# set variables

		if len(self.var_args) > 0:
			self.runCommand(self.var_args, parseLine=self.parseLine, quiet=True)

		# run command

		self.runCommand(self.args, parseLine=self.parseLine)

		# back to working directory

		if self.configure_dir:
			os.chdir(prev_dir)

	check_errors = re.compile(r'.*Error: (.*)')
	check_failed = re.compile(r'.*(Build FAILED|CMake Error|MSBUILD : error).*')
	check_artefacts = re.compile(r'.*(.+?) -> (.+)')
	check_installed = re.compile(r'.*-- (.+?): (.+)')

	def parseLine(self, line):
		# check for errors

		if self.check_errors.match(line) or self.check_failed.match(line):
			return False

		# add artefacts to options

		match = self.check_artefacts.match(line)
		if match:
			path = match.group(2)
			self.options.created(os.path.abspath(path))

		# add installed files to options

		match = self.check_installed.match(line)
		if match:
			what = match.group(1)
			path = match.group(2)

			if any(what in s for s in ['Installing', 'Up-to-date']):
				self.options.created(os.path.abspath(path))

		return True

def uninstall(name, options):
	pass