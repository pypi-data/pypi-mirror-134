import os
import subprocess

from subprocess import CalledProcessError
from uttl.buildout.base_recipe import BaseRecipe
from zc.buildout import UserError

class CommandRecipe(BaseRecipe):
	def __init__(self, buildout, name, options, executable='cmd.exe'):
		super().__init__(buildout, name, options)

		self.options.setdefault('executable', executable)
		self.options.setdefault('working-dir', os.getcwd())

		# always install
		
		self.always_install = False

		if 'always-install' in self.options:
			self.always_install = self.options['always-install'] == '1'

		# working directory

		self.working_dir = None

		if 'working-dir' in self.options:
			self.working_dir = os.path.abspath(self.options['working-dir'])

		# artefacts

		self.artefacts = []

		if 'artefacts' in self.options:
			self.artefacts += [os.path.abspath(path) for path in self.options['artefacts'].splitlines()]

		# arguments

		self.additional_args = []

		if 'arguments' in self.options:
			self.additional_args = self.options['arguments'].splitlines()

		self.args = self.additional_args

	def install(self):
		# register installed artefacts

		for a in self.artefacts:
			self.options.created(a)

		# switch working directory

		prev_dir = None

		if self.working_dir:
			prev_dir = os.getcwd()
			os.chdir(self.working_dir)

		# run command

		self.command_install()

		# back to previous directory

		if self.working_dir:
			os.chdir(prev_dir)

		return self.options.created()

	def command_install(self):
		self.runCommand(self.args)

	def update(self):
		if self.always_install:
			return self.install()

		# use private api to check for files that need to be installed

		(installed_part_options, installed_exists) = self.buildout._read_installed_part_options()

		part_options = installed_part_options[self.name]
		if not part_options:
			self.log.info('Installing again due to missing options.')
			return self.install()

		if not '__buildout_installed__' in part_options:
			self.log.info('No files were installed previously.')
			return self.install()

		installed = (path.rstrip() for path in part_options['__buildout_installed__'].split())
		for path in installed:
			if not os.path.exists(path):
				self.log.info('Installing again due to missing file.')
				self.log.debug('MISSING: %s' % (path))
				return self.install()

	def runCommand(self, args, prefixArgs=[], parseLine=lambda line: True, quiet=False, expected=0):
		args = prefixArgs + [ self.options['executable'] ] + args

		self.log.debug(str(args))

		success = True

		try:
			with subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
				for line in iter(proc.stdout.readline, b''):
					stripped = line.rstrip().decode('UTF-8')

					if not quiet:
						self.log.info(stripped)

					if not parseLine(stripped):
						success = False

				proc.communicate()

				self.log.debug('returned %d' % (proc.returncode))

				if proc.returncode != expected or not success:
					raise CalledProcessError(proc.returncode, args)
		except FileNotFoundError:
			raise UserError('Failed to execute "%s".' % (str(args)))

		return success