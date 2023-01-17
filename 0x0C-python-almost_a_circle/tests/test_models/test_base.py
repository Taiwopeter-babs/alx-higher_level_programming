#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
import os
import unittest
import json
import csv

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class for instantiation test"""

    def setUp(self):
        # No ids given
        self.base1 = Base()
        self.base2 = Base()
        self.base4 = Base()

    def tearDown(self):
        """Delete created objects for test"""
        del self.base1
        del self.base2
        del self.base4

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


class TestJson(unittest.TestCase):
    """Tests JSON representations"""

    def setUp(self):
        """sets up objects"""
        self.rect = Rectangle(23, 44)
        self.sqr = Square(23, 44)
        self.tuple_arg = (1, 3)

    def tearDown(self):
        """Deletes objects created for tests"""
        del self.rect
        del self.sqr
        del self.tuple_arg

    def test_to_json_string(self):
        """Tests the to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3, 1, 4)

        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()

        list_dict = [r1_dict, r2_dict]

        json_dictionary = Base.to_json_string(list_dict)
        json_empty_dict = Base.to_json_string([])

        self.assertIsInstance(r1_dict, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(json_empty_dict, "[]")
        self.assertIsInstance(json_empty_dict, str)

    def test_save_to_file(self):
        """Test save_to_file for Rectangle class"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        rect = Rectangle(4, 10, 1, 0, 7)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r", encoding="utf-8") as m_file:
            content = m_file.read()

        res = [{"id": 7, "width": 4, "height": 10, "x": 1, "y": 0}]
        self.assertEqual(res, json.loads(content))

    def test_save_to_file_not_subclass(self):
        """Tests if objects' class are not subclasses of Base"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([self.rect, self.tuple_arg])

    def test_save_to_file_none(self):
        """Test for saving empty or None argument"""
        try:
            os.remove("Rectangle.json")
            os.remove("Squaree.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as r_file:
            content1 = r_file.read()
        self.assertEqual("[]", content1)

        with open("Square.json", "r", encoding="utf-8") as s_file:
            content2 = s_file.read()
        self.assertEqual("[]", content2)

    def test_save_to_file(self):
        """Test save_to_file for Square class"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        sqr = Square(4, 10, 10, 67)
        Square.save_to_file([sqr])

        with open("Square.json", "r", encoding="utf-8") as m_file:
            content = m_file.read()

        res = [{"id": 67, "size": 4, "x": 10, "y": 10}]
        self.assertEqual(res, json.loads(content))

    def test_save_to_file_not_subclass(self):
        """Tests if objects' class are not subclasses of Base"""
        with self.assertRaises(TypeError):
            Square.save_to_file([self.sqr, self.tuple_arg])

    def test_from_json_string(self):
        """Test method from_json_string with Rectangle"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        list_input = [
                {"id": 1000, "width": 500, "height": 250},
                {"id": 1001, "width": 700, "height": 350}
        ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertNotEqual(type(json_list_input), type(list_output))
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

        self.assertEqual(list_input[0], list_output[0])
        self.assertEqual(list_input[1], list_output[1])

    def test_dict_to_instance(self):
        """Test creating new instance from an existing one"""
        rect1 = Rectangle(2, 3, 5, 8, 11)
        r_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**r_dict)

        self.assertNotEqual(rect1, rect2)
        self.assertIsNot(rect1, rect2)

        s1 = Square(2, 3, 5, 80)
        s_dict = s1.to_dictionary()
        s2 = Square.create(**s_dict)

        self.assertNotEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_load_from_file_no_file(self):
        """Test load_from_file method on empty file"""
        if not os.path.exists("Rectangle.json"):
            self.assertEqual(Rectangle.load_from_file(), [])

        if not os.path.exists("Square.json"):
            self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test load_from_file method on existing file"""
        r1 = Rectangle(10, 7, 2, 8, 789)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))
        self.assertEqual(r1.width, list_rectangles_output[0].width)
        self.assertEqual(r1.height, list_rectangles_output[0].height)
        self.assertEqual(r1.x, list_rectangles_output[0].x)
        self.assertEqual(r1.y, list_rectangles_output[0].y)
        self.assertEqual(r1.id, list_rectangles_output[0].id)

    def test_load_from_file_exists(self):
        """Test load_from_file method on existing file"""
        s1 = Square(10, 7, 2, 789)
        s2 = Square(15, 8, 12, 436)
        list_square_input = [s1, s2]

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()

        self.assertNotEqual(id(s1), id(list_square_output[0]))
        self.assertEqual(s1.size, list_square_output[0].size)
        self.assertEqual(s1.x, list_square_output[0].x)
        self.assertEqual(s1.y, list_square_output[0].y)
        self.assertEqual(s1.id, list_square_output[0].id)

    def test_save_file_csv(self):
        """Tests save_to_file for csv formatted files"""
        try:
            os.remove("Square.csv")
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass

        """Rectangle class"""
        rect = Rectangle(4, 10, 1, 0, 7)
        Rectangle.save_to_file_csv([rect])

        with open("Rectangle.csv", "r", newline="") as csvfile:
            content = csv.DictReader(csvfile)
            res = {"id": '7', "width": '4', "height": '10', "x": '1', "y": '0'}
            for row in content:
                self.assertEqual(res, row)

        """Square class"""
        sqr = Square(8, 20, 2, 3)
        Square.save_to_file_csv([sqr])

        with open("Square.csv", "r", newline="") as csvfile:
            content = csv.DictReader(csvfile)
            res = {"id": '3', "size": '8', "x": '20', "y": '2'}
            for row in content:
                self.assertEqual(res, row)

    def test_csv_save_to_file_not_subclass_rect(self):
        """Tests if objects' class are not subclasses of Base"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([self.rect, self.tuple_arg])

    def test_csv_save_to_file_not_subclass_sqr(self):
        """Tests if objects' class are not subclasses of Base"""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([self.sqr, self.tuple_arg])

    def test_save_to_file_csv_none(self):
        """Test for saving empty or None argument"""
        try:
            os.remove("Rectangle.csv")
            os.remove("Squaree.csv")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file_csv(None)
        Square.save_to_file_csv(None)

        with open("Rectangle.csv", "r", newline='') as csvfile1:
            content1 = csv.DictReader(csvfile1)
            for row in content1:
                self.assertEqual("[]", row)

        with open("Square.csv", "r", newline="") as csvfile2:
            content2 = csv.DictReader(csvfile2)
            for row in content2:
                self.assertEqual("[]", row)

    def test_load_from_file_csv_no_file(self):
        """Test load_from_file method on empty file"""
        if not os.path.exists("Rectangle.csv"):
            self.assertEqual(Rectangle.load_from_file_csv(), [])

        if not os.path.exists("Square.csv"):
            self.assertEqual(Square.load_from_file_csv(), [])

    def test_load_from_file_csv_rect_exists(self):
        """Test load_from_file method on existing file"""
        r1 = Rectangle(10, 7, 2, 8, 789)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))
        self.assertEqual(r1.width, list_rectangles_output[0].width)
        self.assertEqual(r1.height, list_rectangles_output[0].height)
        self.assertEqual(r1.x, list_rectangles_output[0].x)
        self.assertEqual(r1.y, list_rectangles_output[0].y)
        self.assertEqual(r1.id, list_rectangles_output[0].id)

    def test_load_from_file_csv_sqr_exists(self):
        """Test load_from_file method on existing file"""
        s1 = Square(10, 7, 2, 789)
        s2 = Square(15, 8, 12, 436)
        list_square_input = [s1, s2]

        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

        Square.save_to_file_csv(list_square_input)
        list_square_output = Square.load_from_file_csv()

        self.assertNotEqual(id(s1), id(list_square_output[0]))
        self.assertEqual(s1.size, list_square_output[0].size)
        self.assertEqual(s1.x, list_square_output[0].x)
        self.assertEqual(s1.y, list_square_output[0].y)
        self.assertEqual(s1.id, list_square_output[0].id)
