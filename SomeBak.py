import os
import os.path
import shutil
import sys



class Program:
	def __init__(self, args):
		self.args = args[1:]

	def run(self):
		targetLocation = self.args[0]
		# ToDo: canonise path
		for sourceFile in self.fileArtefacts:
			shutil.copy2(sourceFile.fullPath, os.path.join(targetLocation, sourceFile.targetPath))



if __name__ == '__main__':
	Program(sys.argv).run()
