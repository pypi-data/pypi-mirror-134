import logging

class BaseRecipe(object):
	def __init__(self, buildout, name, options):
		self.buildout, self.name, self.options = buildout, name, options
		self.log = logging.getLogger(self.name)

	def install(self):
		return self.options.created()

	def update(self):
		pass