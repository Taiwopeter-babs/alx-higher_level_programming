#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
from io import StringIO
import sys
import os
import unittest
import json
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

        with self.assertRaises(TypeError) as err_0:
            Rectangle((2, 3), 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle([2, 3], 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(range(4), 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        self.assertEqual(r1.width, 34)
        self.assertIsInstance(r1.width, int)

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

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, (4, 7), 5, 6)
        self.assertEqual("height must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, [4, 6], 5, 6)
        self.assertEqual("height must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, range(4), 5, 6)
        self.assertEqual("height must be an integer", str(err_0.exception))

        self.assertEqual(r1.height, 5)
        self.assertIsInstance(r1.height, int)

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

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, 4, (5, 5), 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, 4, [5, 5], 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(4, 4, range(5), 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        self.assertEqual(r1.x, 2)
        self.assertEqual(r2.x, 0)
        self.assertIsInstance(r1.x, int)

    def test_for_y_attribute(self):
        """Test for y-coordinate attribute"""
        r1 = Rectangle(3, 5, 2, 9)
        r2 = Rectangle(3, 5, 2)

        with self.assertRaises(TypeError) as err_0:
            Rectangle(3, 4, 5, 9.0)
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Rectangle(3, 4, 5, "6")
        self.assertEqual("y must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Rectangle(3, 4, 5, -6)
        self.assertEqual("y must be >= 0", str(err_2.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, 4, 5, (6, 6))
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(2, 4, 5, [6, 6])
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Rectangle(4, 4, 5, range(6))
        self.assertEqual("y must be an integer", str(err_0.exception))

        self.assertEqual(r1.y, 9)
        self.assertEqual(r2.y, 0)
        self.assertIsInstance(r1.y, int)

    def test_rectangle_area(self):
        """Test rectangle area"""
        r1 = Rectangle(3, 5, 2, 9)
        self.assertEqual(15, r1.area())

        """Test large output"""
        r2 = Rectangle(777777777, 777777777, 3, 5, 2)
        self.assertEqual(r2.area(), 604938270395061729)


class TestDisplay(unittest.TestCase):
    """class for testing __str__ and display methods in Rectangle class"""

    @classmethod
    def setUpClass(cls):
        """set up objects for global tests cases"""
        cls.without_coordinates = Rectangle(4, 3)
        cls.with_coordinates = Rectangle(4, 3, 2, 4)
        cls.rect_update = Rectangle(5, 5, 5, 5)

    @classmethod
    def tearDownClass(cls):
        """Tear down instances and objects"""
        del cls.without_coordinates
        del cls.with_coordinates
        del cls.rect_update

    @staticmethod
    def show_output(instance_of_class, method):
        """
            This returns the captured output from StringIO

            Args:
                instance_of_class(Rectangle): instance of rectangle class
                method(str): The instance method to call
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        if (method == "print"):
            print(instance_of_class)
        else:
            instance_of_class.display()

        sys.stdout = sys.__stdout__

        return (captured_output)

    def test_str_method(self):
        """Test the __str__ method"""
        r1 = Rectangle(2, 5, 1, 2, 7)

        _str_output = "[Rectangle] ({}) 1/2 - 2/5\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_without_coord_and_id(self):
        """Test the __str__ without coordinates and id"""
        r1 = Rectangle(2, 5)

        _str_output = "[Rectangle] ({}) 0/0 - 2/5\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_with_changing_attr(self):
        """Test string with changing attributes"""
        r1 = Rectangle(2, 5)
        r1.width = 4
        r1.height = 7

        _str_output = "[Rectangle] ({}) 0/0 - 4/7\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_without_attributes(self):
        """Test __str__ without attributes"""
        with self.assertRaises(TypeError):
            r = Rectangle()
            r.__str__()

    def test_display_shape_1(self):
        """Test display shape of rectangle with '#' with coordinates"""
        show_output1 = TestDisplay.show_output(TestDisplay.without_coordinates,
                                               "display")
        display_output1 = "####\n####\n####\n"
        self.assertEqual(show_output1.getvalue(), display_output1)

    def test_display_shape_2(self):
        """Test shape of rectangle with '#' without coordinates"""

        show_output2 = TestDisplay.show_output(TestDisplay.with_coordinates,
                                               "display")
        display_output2 = "\n\n\n\n  ####\n  ####\n  ####\n"
        self.assertEqual(show_output2.getvalue(), display_output2)

    def test_update_args(self):
        """Tests update method"""
        TestDisplay.rect_update.update(3)
        update1 = TestDisplay.show_output(TestDisplay.rect_update, "print")
        display_update1 = "[Rectangle] (3) 5/5 - 5/5\n"

        TestDisplay.rect_update.update(3, 7)
        update2 = TestDisplay.show_output(TestDisplay.rect_update, "print")
        display_update2 = "[Rectangle] (3) 5/5 - 7/5\n"

        TestDisplay.rect_update.update(3, 7, 4)
        update3 = TestDisplay.show_output(TestDisplay.rect_update, "print")
        display_update3 = "[Rectangle] (3) 5/5 - 7/4\n"

        TestDisplay.rect_update.update(3, 7, 4, 2)
        update4 = TestDisplay.show_output(TestDisplay.rect_update, "print")
        display_update4 = "[Rectangle] (3) 2/5 - 7/4\n"

        TestDisplay.rect_update.update(3, 7, 4, 2, 8)
        update5 = TestDisplay.show_output(TestDisplay.rect_update, "print")
        display_update5 = "[Rectangle] (3) 2/8 - 7/4\n"

        self.assertEqual(update1.getvalue(), display_update1)
        self.assertEqual(update2.getvalue(), display_update2)
        self.assertEqual(update3.getvalue(), display_update3)
        self.assertEqual(update4.getvalue(), display_update4)
        self.assertEqual(update5.getvalue(), display_update5)

    def test_update_kwargs(self):
        """Test kwargs update"""
        r2 = Rectangle(10, 10, 10, 10, 1)

        r2.update(y=4)
        update1 = TestDisplay.show_output(r2, "print")
        display_update1 = "[Rectangle] (1) 10/4 - 10/10\n"

        r2.update(width=2, x=3)
        update2 = TestDisplay.show_output(r2, "print")
        display_update2 = "[Rectangle] (1) 3/4 - 2/10\n"

        r2.update(height=6, y=7)
        update3 = TestDisplay.show_output(r2, "print")
        display_update3 = "[Rectangle] (1) 3/7 - 2/6\n"

        r2.update(89)
        update4 = TestDisplay.show_output(r2, "print")
        display_update4 = "[Rectangle] (89) 3/7 - 2/6\n"

        r2.update(id=99, x=15, width=7, y=8, height=11)
        update5 = TestDisplay.show_output(r2, "print")
        display_update5 = "[Rectangle] (99) 15/8 - 7/11\n"

        r2.update(30, 9, height=9)
        update6 = TestDisplay.show_output(r2, "print")
        display_update6 = "[Rectangle] (30) 15/8 - 9/11\n"

        self.assertEqual(update1.getvalue(), display_update1)
        self.assertEqual(update2.getvalue(), display_update2)
        self.assertEqual(update3.getvalue(), display_update3)
        self.assertEqual(update4.getvalue(), display_update4)
        self.assertEqual(update5.getvalue(), display_update5)
        self.assertEqual(update6.getvalue(), display_update6)

    def test_dictionary_representation(self):
        """Tests dictionary representation of class"""
        rect = Rectangle(4, 6, 2)
        rect_dict = rect.to_dictionary()
        rect_display = "[Rectangle] ({}) 2/0 - 4/6\n".format(rect.id)

        self.assertIsInstance(rect_dict, dict)

        rect2 = Rectangle(2, 2)
        rect2.update(**rect_dict)
        rect_update = TestDisplay.show_output(rect2, "print")

        self.assertEqual(rect_update.getvalue(), rect_display)
        self.assertNotEqual(rect, rect2)
