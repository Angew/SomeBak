# Copyright Petr Kmoch 2016
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)

import argparse
import os
import os.path
import shutil
import sys



class Program:
	def __init__(self, args = ['SomeBak']):
		self.setOptions(self.parseArgs(args))


	def parseArgs(self, args):
		parser = argparse.ArgumentParser(
			prog = args[0]
		)
		parser.add_argument(
			'-o', '--output-dir',
			help = 'Root output directory',
			metavar = 'OUTPUT_DIR',
			default = '.',
			dest = 'targetLocation'
		)
		parser.add_argument(
			'--config-file-name',
			help = 'Alternative name of config files',
			metavar = 'NAME',
			default = 'SomeBak.cfg',
			dest = 'configFileName'
		)
		parser.add_argument(
			'configDir',
			help = 'Directory with initial configuration file',
			metavar = 'config',
			nargs = '?',
			default = '.'
		)
		return parser.parse_args(args[1:])


	def setOptions(self, options):
		self.targetLocation = os.path.abspath(options.targetLocation)
		self.configDir = os.path.abspath(options.configDir)
		self.configFileName = options.configFileName


	def processConfigDir(self, configDir):
		try:
			artefacts = []
			with open(os.path.join(configDir, self.configFileName)) as configFile:
				for line in configFile:
					artefact = self.processConfigLine(line)
					if artefact is not None:
						artefacts.append(artefact)	# WIP: needs to be an object with data
			return artefacts
		except OSError as err:
			# ToDo: log error
			return []


	def processConfigLine(self, line):
		# ToDo: fullPath, targetPath
		file = ''
		escaped = False
		for ch in line:
			if escaped:
				if ch in {'`', '|'}:
					file += ch
					escaped = False
				else
					# ToDo: log error (unknown escape)
					return ''
			else:
				if ch == '`':
					escaped = True
				elif ch == '|':
					return file
				else:
					file += ch
		if escaped:
			# ToDo: log error (loose escape)
			return ''
		return file


	def run(self):
		self.fileArtefacts = self.processConfigDir(self.configDir)
		for sourceFile in self.fileArtefacts:
			os.makedirs(sourceFile.targetPath, exist_ok = True)
			shutil.copy2(sourceFile.fullPath, os.path.join(self.targetLocation, sourceFile.targetPath))



if __name__ == '__main__':
	Program(sys.argv).run()
