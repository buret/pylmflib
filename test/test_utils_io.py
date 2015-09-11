#! /usr/bin/env python

from startup import *
from utils.io import open_file, open_read, open_write

## Test I/O functions

class TestIOFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_open_file(self):
        import sys, os
        utest_path = sys.path[0] + '/'
        test_filename = utest_path + "test_file"
        test_string = "Test string."
        # Test open file in write mode
        test_file = open_file(test_filename, 'w')
        test_file.write(test_string)
        test_file.close()
        # Test open file in read mode
        test_file = open_file(test_filename, 'r')
        self.assertEqual(test_file.readline(), test_string)
        test_file.close()
        # Remove test file
        os.remove(test_filename)

    def test_open_read(self):
        import sys, os
        utest_path = sys.path[0] + '/'
        test_filename = utest_path + "test_file"
        test_string = "Test string."
        # Write file
        test_file = open_file(test_filename, 'w')
        test_file.write(test_string)
        test_file.close()
        # Test open and read file
        test_file = open_read(test_filename)
        self.assertEqual(test_file.readline(), test_string)
        test_file.close()
        # Remove test file
        os.remove(test_filename)

    def test_open_write(self):
        import sys, os
        utest_path = sys.path[0] + '/'
        test_filename = utest_path + "test_file"
        test_string = "Test string."
        # Test open and write file
        test_file = open_write(test_filename)
        test_file.write(test_string)
        test_file.close()
        # Read file
        test_file = open_file(test_filename, 'r')
        self.assertEqual(test_file.readline(), test_string)
        test_file.close()
        # Remove test file
        os.remove(test_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestIOFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
