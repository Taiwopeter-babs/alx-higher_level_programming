#!/usr/bin/python3
"""
    This module contains a class: Base
"""
import json
import os

class Base:
    """
        This class contains a private attribute
        and other methods

        Args:
            __nb_objects(int): a private attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            class constructor

            Args:
                id(int): public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of object"""

        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")

        json_string = json.dumps([obj for obj in list_dictionaries])

        return (json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON string representation of objects to file"""
        class_name = cls.__name__  # get the class name
        filename = str(class_name) + ".json"

        if (list_objs is None):
            string_to_save = Base.to_json_string([])
        else:
            """
                convert to dictionary representation
                and perform JSON operation
            """
            string_to_save = Base.to_json_string([obj.to_dictionary()
                                                 for obj in list_objs])
        # save/write to file
        with open(filename, "w+", encoding="utf-8") as class_file:
            class_file.write(string_to_save)
    
    @staticmethod
    def from_json_string(json_string):
        """Returns the python object of json string representation"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of class cls"""
        class_name = cls.__name__

        if class_name == "Rectangle":
            from models.rectangle import Rectangle
            dummy = Rectangle(6, 7, 4, 5, 100)
            dummy.update(**dictionary)
            return (dummy)

        if class_name == "Square":
            from models.square import Square
            dummy = Square(5, 3, 7, 200)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """Return a list of cls class instances"""
        # Get class name
        class_name = cls.__name__

        # Rectangle instances
        if class_name == "Rectangle":
            filename = "./Rectangle.json"
            if os.path.exists(filename):
                from models.rectangle import Rectangle
                with open(filename, "r+", encoding="utf-8") as json_file:
                    json_string = json_file.read()  # read file
                list_of_dict = Base.from_json_string(json_string)
                list_of_instances = [Rectangle.create(**dic) for dic in list_of_dict]
                return (list_of_instances)
        
        elif class_name == "Square":
            from models.square import Square
            filename = "./Square.json"
            if os.path.exists(filename):
                with open(filename, "r+", encoding="utf-8") as json_file:
                    json_string = json_file.read()  # read file
                list_of_dict = Base.from_json_string(json_string)
                list_of_instances = [Square.create(**dic) for dic in list_of_dict]
                return (list_of_instances)

        return ([])