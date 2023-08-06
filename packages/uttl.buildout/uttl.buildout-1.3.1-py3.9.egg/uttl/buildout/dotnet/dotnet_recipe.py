from uttl.buildout.command_recipe import CommandRecipe
from zc.buildout import UserError

class DotnetRecipe(CommandRecipe):
	def __init__(self, buildout, name, options):
		super().__init__(buildout, name, options, executable='dotnet')

def uninstall(name, options):
	pass