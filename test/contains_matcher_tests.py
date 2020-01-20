import unittest
import sys
sys.path.append('../src')

from contains_matcher.matcher import contains

class TestContainsMatcher(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertTrue(contains({}, []))

    def test_single_key(self):
        self.assertTrue(contains({ "key" : "value" }, [ "key" ]))
        self.assertFalse(contains({ "key" : "value" }, [ "not_key" ]))

    def test_single_value(self):
        self.assertTrue(contains({ "key" : "value" }, [ "value" ]))
        self.assertFalse(contains({ "key" : "value" }, [ "not_value" ]))

    def test_one_element_list(self):
        self.assertTrue(contains([ "value" ], [ "value" ]))
        self.assertFalse(contains([ "value" ], [ "not_value" ]))

    def test_key_value_pair(self):
        self.assertTrue(contains({ "key" : "value" }, [ "key", "value" ]))
        self.assertFalse(contains({ "key" : "value" }, [ "not_key", "value" ]))
        self.assertFalse(contains({ "key" : "value" }, [ "key", "not_value" ]))

if __name__ == '__main__':
    unittest.main()
