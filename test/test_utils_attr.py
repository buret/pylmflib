#! /usr/bin/env python

from startup import *
from utils.attr import check_attr_type, check_attr_range, check_date_format

## Test attribute functions

class TestAttrFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_attr_type(self):
        check_attr_type(1, int, "int")
        check_attr_type("1", str, "str")
        check_attr_type(set(), set, "set")
        check_attr_type(dict(), dict, "dict")
        check_attr_type(list(), list, "list")
        check_attr_type(dict(), list, "error")

    def test_check_attr_range(self):
        range = [1, "allowed value", [2, 3]]
        mapping = {10 : 1}
        self.assertEqual(check_attr_range(1, range, "ok"), range[0])
        self.assertEqual(check_attr_range("allowed value", range, "ok"), range[1])
        self.assertEqual(check_attr_range([2, 3], range, "ok"), range[2])
        self.assertEqual(check_attr_range(10, range, "ok", mapping), range[0])
        check_attr_range(10, range, "error")
        check_attr_range(11, range, "error", mapping)

    def test_check_date_format(self):
        # Test error cases
        dates = ["2014", "YYYY-MM-DD", "2014-10-8", "08-10-2014", "2014/10/08"]
        for date in dates:
            check_date_format(date)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAttrFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
