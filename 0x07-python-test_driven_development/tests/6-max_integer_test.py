#!/usr/bin/python3
"""Unittest for max_integer[...]
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        """setup the variables for tests"""
        self.int_list = [2, 5, 8, 1, 15, 9]
        self.float_in_list = [-1, 6, 3.6, 7, 31]
        self.negative_int = [-2, -8, -15, -4, -35]
        self.string_in_list = [4, 8, -2, '2', 6]
        self.tuple_arg = (1, 2, 4, 6, 9)
        self.empty_list = []
        self.single_element = [2]
        self.string_arg = "1234566"

    def test_ideal_case(self):
        """Test for list that contains integers"""
        self.assertEqual(max_integer(self.int_list), 15)
        self.assertEqual(max_integer(self.negative_int), -2)

    def test_for_string(self):
        """Test for string type in list and string argument"""
        with self.assertRaises(TypeError):
            max_integer(self.string_in_list)

        with self.assertRaises(TypeError):
            max_integer(self.string_arg)

    def test_for_float(self):
        """Test for float type in list"""
        with self.assertRaises(TypeError):
            max_integer(self.float_in_list)

    def test_for_argument_type(self):
        """Test for argument type in function"""
        with self.assertRaises(TypeError):
            max_integer(self.tuple_arg)

    def test_for_empty_and_single(self):
        """test for empty list and list with one element"""
        self.assertEqual(max_integer(self.empty_list), None)
        self.assertEqual(max_integer(self.single_element), 2)
