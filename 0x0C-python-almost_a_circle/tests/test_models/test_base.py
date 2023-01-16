#!/usr/bin/python3
"""
    Test module for class Base and methods in it
"""
import os
import unittest
import json

from models.base import Base
from models.rectangle import Rectangle



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


class TestJson(unittest.TestCase):
    """Tests JSON representations"""

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
        except:
            pass
        rect = Rectangle(4, 10, 1, 0, 7)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r", encoding='utf-8') as m_file:
            content = m_file.read()

        res = [{"id": 7, "width": 4, "height": 10, "x": 1, "y": 0}]
        self.assertEqual(res, json.loads(content))
        
