# Copyright Petr Kmoch 2016
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)

import os
import os.path
import shutil
import sys



class Program:
	def __init__(self, args = ['SomeBak']):
		self.args = args[1:]
		try:
			self.targetLocation = os.path.abspath(self.args[0])
		except IndexError:
			self.targetLocation = os.path.abspath('.')

	def run(self):
		for sourceFile in self.fileArtefacts:
			os.makedirs(sourceFile.targetPath, exist_ok = True)
			targetFullPath = os.path.join(self.targetLocation, sourceFile.targetPath)
			if not os.path.lexists(os.path.join(targetFullPath, os.path.basename(sourceFile.fullPath))):
				shutil.copy2(sourceFile.fullPath, targetFullPath)



if __name__ == '__main__':
	Program(sys.argv).run()
