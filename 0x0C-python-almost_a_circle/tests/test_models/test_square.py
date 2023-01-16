#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
from io import StringIO
import sys
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """class for instantiation test"""

    def test_for_id(self):
        """Test for id attribute in Square class"""
        r1 = Square(2)
        r2 = Square(3)
        r3 = Square(2, 0, 0, 7)
        r4 = Square(3, 6, 2)
        r5 = Square(3, 2, 8, 3.2)
        r6 = Square(3, 2, 8, "Tee")

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.id, r4.id - 2)
        self.assertEqual(r5.id, 3.2)
        self.assertEqual(r6.id, "Tee")

    def test_for_size_attribute(self):
        """Test for width attribute"""
        r1 = Square(4)

        with self.assertRaises(TypeError) as err_0:
            Square(3.2, 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Square("3", 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Square(-3, 4, 5, 6)
        self.assertEqual("width must be > 0", str(err_2.exception))

        with self.assertRaises(ValueError) as err_3:
            Square(0, 4, 5, 6)
        self.assertEqual("width must be > 0", str(err_3.exception))

        with self.assertRaises(TypeError) as err_0:
            Square((2, 3), 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square([2, 3], 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(range(4), 4, 5, 6)
        self.assertEqual("width must be an integer", str(err_0.exception))

        self.assertEqual(r1.size, 4)
        self.assertIsInstance(r1.size, int)

    def test_for_x_attribute(self):
        """Test for x-coordinate attribute"""
        r1 = Square(3, 5, 2)
        r2 = Square(3)

        with self.assertRaises(TypeError) as err_0:
            Square(3, 5.0, 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Square(3, "5", 6)
        self.assertEqual("x must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Square(3, -5, 6)
        self.assertEqual("x must be >= 0", str(err_2.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(2, (5, 5), 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(2, [5, 5], 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(4, range(5), 6)
        self.assertEqual("x must be an integer", str(err_0.exception))

        self.assertEqual(r1.x, 5)
        self.assertEqual(r2.x, 0)
        self.assertIsInstance(r1.x, int)

    def test_for_y_attribute(self):
        """Test for y-coordinate attribute"""
        r1 = Square(3, 5, 2, 9)
        r2 = Square(3, 5)

        with self.assertRaises(TypeError) as err_0:
            Square(3, 5, 9.0)
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_1:
            Square(3, 5, "6")
        self.assertEqual("y must be an integer", str(err_1.exception))

        with self.assertRaises(ValueError) as err_2:
            Square(3, 5, -6)
        self.assertEqual("y must be >= 0", str(err_2.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(2, 5, (6, 6))
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(2, 5, [6, 6])
        self.assertEqual("y must be an integer", str(err_0.exception))

        with self.assertRaises(TypeError) as err_0:
            Square(4, 5, range(6))
        self.assertEqual("y must be an integer", str(err_0.exception))

        self.assertEqual(r1.y, 2)
        self.assertEqual(r2.y, 0)
        self.assertIsInstance(r1.y, int)

    def test_rectangle_area(self):
        """Test rectangle area"""
        r1 = Square(3, 2, 9)
        self.assertEqual(9, r1.area())

        """Test large output"""
        r2 = Square(777777777, 3, 5, 2)
        self.assertEqual(r2.area(), 604938270395061729)


class TestDisplay(unittest.TestCase):
    """class for testing __str__ and display methods in Square class"""

    @classmethod
    def setUpClass(cls):
        """set up objects for global tests cases"""
        cls.without_coordinates = Square(4)
        cls.with_coordinates = Square(4, 2, 4)
        cls.square_update = Square(5, 5, 5)

    @classmethod
    def tearDownClass(cls):
        """Tear down instances and objects"""
        del cls.without_coordinates
        del cls.with_coordinates
        del cls.square_update

    @staticmethod
    def show_output(instance_of_class, method):
        """
            This returns the captured output from StringIO

            Args:
                instance_of_class(Square): instance of rectangle class
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
        r1 = Square(2, 1, 2, 7)

        _str_output = "[Square] ({}) 1/2 - 2\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_without_coord_and_id(self):
        """Test the __str__ without coordinates and id"""
        r1 = Square(2)

        _str_output = "[Square] ({}) 0/0 - 2\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_with_changing_attr(self):
        """Test string with changing attributes"""
        r1 = Square(2, 5, 8)
        r1.size = 4
        r1.x = 7
        r1.y = 5

        _str_output = "[Square] ({}) 7/5 - 4\n".format(r1.id)
        show_output = TestDisplay.show_output(r1, "print")

        self.assertEqual(show_output.getvalue(), _str_output)

    def test_str_without_attributes(self):
        """Test __str__ without attributes"""
        with self.assertRaises(TypeError):
            r = Square()
            r.__str__()

    def test_display_shape_1(self):
        """Test display shape of rectangle with '#' with coordinates"""
        show_output1 = TestDisplay.show_output(TestDisplay.without_coordinates,
                                               "display")
        display_output1 = "####\n####\n####\n####\n"
        self.assertEqual(show_output1.getvalue(), display_output1)

    def test_display_shape_2(self):
        """Test shape of rectangle with '#' without coordinates"""

        show_output2 = TestDisplay.show_output(TestDisplay.with_coordinates,
                                               "display")
        display_output2 = "\n\n\n\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(show_output2.getvalue(), display_output2)

    def test_update_args(self):
        """Tests update method"""
        TestDisplay.square_update.update(3)
        update1 = TestDisplay.show_output(TestDisplay.square_update, "print")
        display_update1 = "[Square] (3) 5/5 - 5\n"

        TestDisplay.square_update.update(3, 7)
        update2 = TestDisplay.show_output(TestDisplay.square_update, "print")
        display_update2 = "[Square] (3) 5/5 - 7\n"

        TestDisplay.square_update.update(3, 7, 4)
        update3 = TestDisplay.show_output(TestDisplay.square_update, "print")
        display_update3 = "[Square] (3) 4/5 - 7\n"

        TestDisplay.square_update.update(3, 7, 4, 2)
        update4 = TestDisplay.show_output(TestDisplay.square_update, "print")
        display_update4 = "[Square] (3) 4/2 - 7\n"

        TestDisplay.square_update.update(3, 7, 2, 8)
        update5 = TestDisplay.show_output(TestDisplay.square_update, "print")
        display_update5 = "[Square] (3) 2/8 - 7\n"

        self.assertEqual(update1.getvalue(), display_update1)
        self.assertEqual(update2.getvalue(), display_update2)
        self.assertEqual(update3.getvalue(), display_update3)
        self.assertEqual(update4.getvalue(), display_update4)
        self.assertEqual(update5.getvalue(), display_update5)

    def test_update_kwargs(self):
        """Test kwargs update"""
        r2 = Square(10, 10, 10, 1)

        r2.update(y=4)
        update1 = TestDisplay.show_output(r2, "print")
        display_update1 = "[Square] (1) 10/4 - 10\n"

        r2.update(size=2, x=3)
        update2 = TestDisplay.show_output(r2, "print")
        display_update2 = "[Square] (1) 3/4 - 2\n"

        r2.update(y=7)
        update3 = TestDisplay.show_output(r2, "print")
        display_update3 = "[Square] (1) 3/7 - 2\n"

        r2.update(89)
        update4 = TestDisplay.show_output(r2, "print")
        display_update4 = "[Square] (89) 3/7 - 2\n"

        r2.update(id=99, x=15, size=7, y=8)
        update5 = TestDisplay.show_output(r2, "print")
        display_update5 = "[Square] (99) 15/8 - 7\n"

        r2.update(30, 9, height=9)
        update6 = TestDisplay.show_output(r2, "print")
        display_update6 = "[Square] (30) 15/8 - 9\n"

        self.assertEqual(update1.getvalue(), display_update1)
        self.assertEqual(update2.getvalue(), display_update2)
        self.assertEqual(update3.getvalue(), display_update3)
        self.assertEqual(update4.getvalue(), display_update4)
        self.assertEqual(update5.getvalue(), display_update5)
        self.assertEqual(update6.getvalue(), display_update6)

    def test_dictionary_representation(self):
        """Tests dictionary representation of class"""
        sqr = Square(4, 6, 2)
        sqr_dict = sqr.to_dictionary()
        sqr_display = "[Square] ({}) 6/2 - 4\n".format(sqr.id)

        self.assertIsInstance(sqr_dict, dict)

        sqr2 = Square(2, 2)
        sqr2.update(**sqr_dict)
        sqr_update = TestDisplay.show_output(sqr2, "print")

        self.assertEqual(sqr_update.getvalue(), sqr_display)
        self.assertNotEqual(sqr, sqr2)
