#! /usr/bin/env python

from startup import *
from utils.error_handling import Error, InputError, OutputError, Warning
from utils.io import EOL

## Test Error class

if __name__ == '__main__':
    utest_path = "utest/"

class TestErrorFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Error object
        self.error = Error("This is an error.")

    def tearDown(self):
        # Release instantiated objects
        del self.error

    def test_init(self):
        self.assertEqual(self.error.msg, "This is an error.")
        self.assertIsNone(self.error.excp)
        # The caller is the Error instantiation of the setUp() function, so please update these lines if needed
        self.assertEqual(self.error.frame_info.filename, utest_path + 'test_utils_error_handling.py')
        self.assertEqual(self.error.frame_info.lineno, 16)
        self.assertEqual(self.error.frame_info.function, 'setUp')
        self.assertListEqual(self.error.frame_info.code_context, ['        self.error = Error("This is an error.")\n'])

    def test_str(self):
        self.assertEqual(str(self.error), "  File \"" + utest_path + "test_utils_error_handling.py\", line 16, in setUp" + EOL + "    Error: This is an error.")

    def test_handle(self):
        test = False
        try:
            print
            self.error.handle()
        except SystemExit:
            test = True
        self.assertTrue(test)

suite = unittest.TestLoader().loadTestsFromTestCase(TestErrorFunctions)

## Test InputError class

class TestInputErrorFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an InputError object
        self.error = InputError("This is an input error.")

    def tearDown(self):
        # Release instantiated objects
        del self.error

    def test_init(self):
        self.assertEqual(self.error.msg, "This is an input error.")
        self.assertIsNone(self.error.expr)
        # The caller is the InputError instantiation of the setUp() function, so please update these lines if needed
        self.assertEqual(self.error.frame_info.filename, utest_path + 'test_utils_error_handling.py')
        self.assertEqual(self.error.frame_info.lineno, 51)
        self.assertEqual(self.error.frame_info.function, 'setUp')
        self.assertListEqual(self.error.frame_info.code_context, ['        self.error = InputError("This is an input error.")\n'])

    def test_str(self):
        self.assertEqual(str(self.error), "  File \"" + utest_path + "test_utils_error_handling.py\", line 51, in setUp" + EOL + "    Error: This is an input error.")

    def test_handle(self):
        test = False
        try:
            print
            self.error.handle()
        except SystemExit:
            test = True
        self.assertTrue(test)

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestInputErrorFunctions))

## Test OutputError class

class TestOutputErrorFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Output Error object
        self.error = OutputError("This is an output error.")

    def tearDown(self):
        # Release instantiated objects
        del self.error

    def test_init(self):
        self.assertEqual(self.error.msg, "This is an output error.")
        self.assertIsNone(self.error.expr)
        # The caller is the OutputError instantiation of the setUp() function, so please update these lines if needed
        self.assertEqual(self.error.frame_info.filename, utest_path + 'test_utils_error_handling.py')
        self.assertEqual(self.error.frame_info.lineno, 86)
        self.assertEqual(self.error.frame_info.function, 'setUp')
        self.assertListEqual(self.error.frame_info.code_context, ['        self.error = OutputError("This is an output error.")\n'])

    def test_str(self):
        self.assertEqual(str(self.error), "  File \"" + utest_path + "test_utils_error_handling.py\", line 86, in setUp" + EOL + "    Error: This is an output error.")

    def test_handle(self):
        test = False
        try:
            print
            self.error.handle()
        except SystemExit:
            test = True
        self.assertTrue(test)

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOutputErrorFunctions))

## Test Warning class

class TestWarningFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Warning object
        self.warning = Warning("This is a warning.")

    def tearDown(self):
        # Release instantiated objects
        del self.warning

    def test_init(self):
        self.assertEqual(self.warning.msg, "This is a warning.")
        # The caller is the Warning instantiation of the setUp() function, so please update these lines if needed
        self.assertEqual(self.warning.frame_info.filename, utest_path + 'test_utils_error_handling.py')
        self.assertEqual(self.warning.frame_info.lineno, 121)
        self.assertEqual(self.warning.frame_info.function, 'setUp')
        self.assertListEqual(self.warning.frame_info.code_context, ['        self.warning = Warning("This is a warning.")\n'])

    def test_str(self):
        self.assertEqual(str(self.warning), "  File \"" + utest_path + "test_utils_error_handling.py\", line 121, in setUp" + EOL + "    Warning: This is a warning.")

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWarningFunctions))

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
