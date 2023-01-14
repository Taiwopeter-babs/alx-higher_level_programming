#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
import os
import unittest

from models.base import Base



class TestBase(unittest.TestCase):
    """class for instantiation test"""

    def setUp(self):
        # No ids given
        self.base1 = Base()
        self.base2 = Base()
        self.base4 = Base()


    def test_no_id(self):
        """Test for no args"""
        self.assertEqual(self.base1.id, self.base2.id - 1)
        self.assertEqual(self.base1.id, self.base4.id - 2)

    def test_none_id(self):
        """Test for None args"""
        base1 = Base(None)
        base2 = Base(None)
        base4 = Base(None)
        self.assertEqual(base1.id, base4.id - 2)

    def test_unique_id(self):
        """Test for unique arg"""
        base3 = Base(14)

        self.assertEqual(self.base1.id, self.base2.id - 1)
        self.assertEqual(self.base1.id, self.base4.id - 2)
        self.assertEqual(14, base3.id)

    def test_access_private_attribute(self):
       """Test for Error thrown if access to private class instance"""
       with self.assertRaises(AttributeError):
           print(Base.__nb_objects)

    def test_str_id(self):
        """Test for string id"""
        self.assertEqual("Taiwo", Base("Taiwo").id)

    def test_float_id(self):
        """Test for float id"""
        self.assertEqual(12.7, Base(12.7).id)
