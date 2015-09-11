#! /usr/bin/env python

from startup import *
from utils.log import log
from utils.io import EOL, open_read
from utils.error_handling import Error

## Test Log class

class TestLogFunctions(unittest.TestCase):

    def setUp(self):
        # Simulate a structure for command line options
        class Options():
            def __init__(self):
                self.log_filename = None
                self.verbose = False
        self.options = Options()

    def tearDown(self):
        # Release instianciated objects
        del self.options

    def test_log(self):
        import os
        ## Test with options
        self.options.log_filename = "test/log.txt"
        msg = "These are options."
        log(msg, self.options)
        # Test log file
        expected_line = "These are options." + EOL
        log_file = open_read(self.options.log_filename)
        self.assertEqual(log_file.readline(), expected_line)
        log_file.close()
        ## Test without options
        msg = "This is a message."
        log(msg)
        # Test log file
        expected_lines = ["These are options." + EOL,
                          "This is a message." + EOL]
        log_file = open_read(self.options.log_filename)
        self.assertListEqual(log_file.readlines(), expected_lines)
        ## Test verbose mode (need to reset log filename)
        self.options.verbose = True
        log_filename = self.options.log_filename
        self.options.log_filename = None
        log(msg, self.options)
        # Test that log file remains unchanged
        log_file = open_read(log_filename)
        self.assertListEqual(log_file.readlines(), expected_lines)
        ## Test unwrittable file
        self.options.log_filename = "/usr/log.txt"
        test = False
        try:
            log(msg, self.options)
        except Error:
            test = True
        self.assertTrue(test)
        ## Remove log file
        os.remove(log_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLogFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
