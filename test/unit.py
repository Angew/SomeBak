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
	def setupProgram(self, targetDir):
		self.targetDir = targetDir
		self.program = program = SomeBak.Program()
		program.targetLocation = targetDir
		program.fileArtefacts = [
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'file1'), targetPath = targetDir),
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'subdir', 'file2'), targetPath = os.path.join(targetDir, 'subdir')),
			MockArtefact(fullPath = os.path.join(testRootPath, 'data', 'file3'), targetPath = os.path.join(targetDir, 'subdir'))
		]

	def test_plainFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'file1'), 'File1')

	def test_subdirFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'subdir', 'file2'), 'File2')

	def test_relocatedFile(self):
		self.program.run()
		self.assertFileContains(os.path.join(self.targetDir, 'subdir', 'file3'), 'File3')



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



class TestCommandLineArg_OutputDir(TestCase):
	def testOmitted(self):
		program = SomeBak.Program(['SomeBak'])
		self.assertEqual(program.targetLocation, os.path.abspath('.'))

	def testAbsolutePath(self):
		for arg in ('-o', '--output'):
			with self.subTest(option = arg):
				program = SomeBak.Program(['SomeBak', arg, os.path.abspath('dir')])
				self.assertEqual(program.targetLocation, os.path.abspath('dir'))

	def testRelativePath(self):
		for arg in ('-o', '--output'):
			with self.subTest(option = arg):
				program = SomeBak.Program(['SomeBak', arg, os.path.join('dir', 'sub')])
				self.assertEqual(program.targetLocation, os.path.abspath(os.path.join('dir', 'sub')))



class TestCommandLineArg_ConfigDir(TestCase):
	def testOmitted(self):
		program = SomeBak.Program(['SomeBak'])
		self.assertEqual(program.configDir, os.path.abspath('.'))

	def testAbsolutePath(self):
		program = SomeBak.Program(['SomeBak', os.path.abspath('dir')])
		self.assertEqual(program.configDir, os.path.abspath('dir'))

	def testRelativePath(self):
		program = SomeBak.Program(['SomeBak', os.path.join('dir', 'sub')])
		self.assertEqual(program.configDir, os.path.abspath(os.path.join('dir', 'sub')))



if __name__ == '__main__':
	unittest.main()
