import os
import shutil

from uttl.buildout.base_recipe import BaseRecipe
from zc.buildout import UserError

class CopyFileRecipe(BaseRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options)

		self.options.setdefault('source-dir', os.getcwd())
		self.options.setdefault('destination-dir', os.getcwd())

		# synonyms

		if 'source-path' in self.options:
			self.options['source-dir'] = self.options['source-path']

		if 'destination-path' in self.options:
			self.options['destination-dir'] = self.options['destination-path']

		# paths

		self.src_dir = os.path.abspath(self.options['source-dir'])

		self.dst_dir = os.path.abspath(self.options['destination-dir'])
		if not os.path.exists(self.dst_dir):
			os.makedirs(self.dst_dir, 0o777, True)

		# get files

		if not 'files' in self.options:
			raise UserError('Missing mandatory "files" option.')

		self.files = [os.path.join(self.dst_dir, file) for file in self.options['files'].splitlines()]

	def install(self):
		self.log.debug(str(self.files))

		for f in self.files:
			self.options.created(f)

		for dst_path in self.files:
			filename = os.path.basename(dst_path)

			src_path = os.path.join(self.src_dir, filename)

			# check if file is missing

			if not os.path.exists(dst_path):
				self.log.debug('%s does not exist at destination' % (filename))

				self.copyFile(src_path, dst_path, filename)

				continue

			# check if source was modified

			src_modified = os.path.getmtime(src_path)
			dst_modified = os.path.getmtime(dst_path)

			if src_modified > dst_modified:
				self.log.debug('%s was modified (%d > %d)' % (filename, src_modified, dst_modified))

				self.copyFile(src_path, dst_path, filename)

		return self.options.created()

	update = install

	def copyFile(self, src, dst, filename):
		if not os.path.exists(src):
			raise FileNotFoundError(src)

		self.log.info('Copying "' + filename + "'...")

		shutil.copy(src, dst)

def uninstall(name, options):
	pass