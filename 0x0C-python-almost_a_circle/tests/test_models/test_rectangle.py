#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """class for instantiation test"""
    

    @classmethod
    def setUpClass(cls):
        """set attributes to be used throughout class"""
        pass
        

    def setUp(self):
        """Set up for each test"""
        pass

    def test_for_id(self):
        """Test for id attribute in Rectangle class"""
        r1 = Rectangle(2, 4)
        r2 = Rectangle(3, 6)
        r3 = Rectangle(2, 4, 0, 0, 7)
        r4 = Rectangle(3, 6, 2, 8)
        r5 = Rectangle(3, 6, 2, 8, 3.2)
        r6 = Rectangle(3, 6, 2, 8, "Tee")

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.id, r4.id - 2)
        self.assertEqual(r5.id, 3.2)
        self.assertEqual(r6.id, "Tee")
    
    def test_for_width_attribute(self):
        """Test for width attribute"""
        r1 = Rectangle(34, 4)

        with self.assertRaises(TypeError) as err_0:
            Rectangle(3.2, 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Rectangle("3", 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Rectangle(-3, 4, 5, 6)
        self.assertEqual("width must be > 0", str(err_2.exception))

        with self.assertRaises(ValueError) as err_3:
            Rectangle(0, 4, 5, 6)
        self.assertEqual("width must be > 0", str(err_3.exception))

        self.assertEqual(r1.width, 34)

    def test_for_height_attribute(self):
        """Test for height attribute"""
        r1 = Rectangle(3, 5)

        with self.assertRaises(TypeError) as err_0:
            Rectangle(3, 5.3, 5, 6)
        self.assertEqual("height must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Rectangle(3, "5", 5, 6)
        self.assertEqual("height must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Rectangle(3, -5, 5, 6)
        self.assertEqual("height must be > 0", str(err_2.exception))

        with self.assertRaises(ValueError) as err_3:
            Rectangle(3, 0, 5, 6)
        self.assertEqual("height must be > 0", str(err_3.exception))

        self.assertEqual(r1.height, 5)

    def test_for_x_attribute(self):
        """Test for x-coordinate attribute"""
        r1 = Rectangle(3, 5, 2)
        r2 = Rectangle(3, 5)

        with self.assertRaises(TypeError) as err_0:
            Rectangle(3, 4, 5.0, 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Rectangle(3, 4, "5", 6)
        self.assertEqual("x must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Rectangle(3, 4, -5, 6)
        self.assertEqual("x must be >= 0", str(err_2.exception))

        self.assertEqual(r1.x, 2)
        self.assertEqual(r2.x, 0)
