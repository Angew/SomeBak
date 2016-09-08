# Copyright Petr Kmoch 2016
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)

import os.path
import shutil
import sys
import tempfile
import unittest

testRootPath = os.path.dirname(__file__)

sys.path.append(os.path.join(os.path.dirname(testRootPath), 'code'))
import SomeBak
del sys.path[-1]


class TestCase(unittest.TestCase):
	def assertFileContains(self, file, contents, msg = None):
		with open(file) as f:
			self.assertEqual(f.read(), contents, msg = msg)



class MockArtefact:
	def __init__(self, **kwargs):
		for var, value in kwargs.items():
			setattr(self, var, value)



class TestCopy:
	groundTruth_plainFile = 'File1'
	groundTruth_subdirFile = 'File2'
	groundTruth_relocatedFile = 'File3'

	def setupProgram(self, targetDir):
		self.targetDir = targetDir
		self.program = program = SomeBak.Program()
		program.targetLocation = targetDir
		program.fileArtefacts = [
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'copyToEmpty', 'file1'), targetPath = targetDir),
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'copyToEmpty', 'subdir', 'file2'), targetPath = os.path.join(targetDir, 'subdir')),
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'copyToEmpty', 'file3'), targetPath = os.path.join(targetDir, 'subdir'))
		]

	def test_plainFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'file1'), self.groundTruth_plainFile)

	def test_subdirFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'subdir', 'file2'), self.groundTruth_subdirFile)

	def test_relocatedFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'subdir', 'file3'), self.groundTruth_relocatedFile)



class TestCopyToEmpty(TestCopy, TestCase):
	def setUp(self):
		self.targetDirObject = tempfile.TemporaryDirectory()
		self.setupProgram(self.targetDirObject.name)

	def tearDown(self):
		self.targetDirObject.cleanup()



class TestCopyToNonExistent(TestCopy, TestCase):
	def setUp(self):
		self.setupProgram(os.path.join(testRootPath, 'test_target_root'))
		self.deleteTargetDir()

	def tearDown(self):
		self.deleteTargetDir()

	def deleteTargetDir(self):
		shutil.rmtree(self.targetDir, ignore_errors = True)



class TestCopyOnce(TestCopy, TestCase):
	def setUp(self):
		self.targetDirObject = tempfile.TemporaryDirectory()
		targetDirPath = os.path.join(self.targetDirObject.name, 'root')
		shutil.copytree(src = os.path.join(testRootPath, 'data', 'copyOnce'), dst = targetDirPath)
		self.setupProgram(targetDirPath)
		self.groundTruth_plainFile = 'Original1'
		self.groundTruth_subdirFile = 'Original2'
		self.groundTruth_relocatedFile = 'Original3'

	def tearDown(self):
		self.targetDirObject.cleanup()



if __name__ == '__main__':
	unittest.main()
