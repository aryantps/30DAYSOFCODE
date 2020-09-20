#!usr/bin/env python

from daily_byte_sep_20 import uncommon
import unittest

class TestUncommon(unittest.TestCase):
    def test_basic(self):
        testcase = ["the quick","brown fox"]
        expected = ["the", "quick", "brown", "fox"]
        self.assertEqual(uncommon(testcase[0],testcase[1]), expected)

    def test_another(self):
        testcase = ["the tortoise beat the haire","the tortoise lost to the haire"]
        expected = ["beat","lost","to"]
        self.assertEqual(uncommon(testcase[0],testcase[1]), expected)

    def test_and_one_other(self):
        testcase = ["copper coffee pot", "hot coffee pot"]
        expected = ["copper", "hot"]
        self.assertEqual(uncommon(testcase[0],testcase[1]), expected)


unittest.main()