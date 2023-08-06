import os.path
import re

from uttl.buildout.command_recipe import CommandRecipe
from zc.buildout import UserError

class DevenvRecipe(CommandRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options, executable='devenv.com')

		# synonyms

		if 'solution' in self.options:
			self.options['solution-path'] = self.options['solution']

		# solution

		if not 'solution-path' in self.options:
			raise UserError('Missing mandatory "solution-path" option.')

		self.args += [ os.path.abspath(self.options['solution-path']) ]

		# actions on a project

		if 'build' in self.options:
			self.args += [ '/Build', self.options['build'] ]

		if 'rebuild' in self.options:
			self.args += [ '/Rebuild', self.options['rebuild'] ]

		if 'clean' in self.options:
			self.args += [ '/Clean', self.options['clean'] ]

		if 'deploy' in self.options:
			self.args += [ '/Deploy', self.options['deploy'] ]

		if 'project' in self.options:
			if not any(action in ['build', 'rebuild', 'clean', 'deploy'] for action in self.options):
				raise UserError('Missing a "build", "rebuild", "clean", or "deploy" option in order to use "project".')

			self.args += [ '/Project', self.options['project'] ]

		# commands

		if 'command' in self.options:
			self.args += [ '/Command', '"%s"' % self.options['command'] ]

		self.options['args'] = ' '.join(str(e) for e in self.args)

	def command_install(self):
		self.runCommand(self.args, parseLine=self.parseLine)

	check_errors = re.compile(r'.*Error: (.*)')
	check_failed = re.compile(r'.*(Build FAILED).*')
	check_artefacts = re.compile(r'.*(.+) -> (.+)')

	def parseLine(self, line):
		# check for errors

		if self.check_errors.match(line) or self.check_failed.match(line):
			return False

		# add artefacts to options

		match = self.check_artefacts.match(line)
		if match:
			self.options.created(match.group(2))

		return True

def uninstall(name, options):
	pass