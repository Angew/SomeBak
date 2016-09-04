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


	def run(self):
		for sourceFile in self.fileArtefacts:
			os.makedirs(sourceFile.targetPath, exist_ok = True)
			shutil.copy2(sourceFile.fullPath, os.path.join(self.targetLocation, sourceFile.targetPath))



if __name__ == '__main__':
	Program(sys.argv).run()
