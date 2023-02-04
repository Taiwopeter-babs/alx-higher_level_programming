#!/usr/bin/python3
"""
    This module contains a class: Base
"""
import json
import os
import csv


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

        if (not isinstance(list_objs, list)):
            string_to_save = Base.to_json_string([])

        elif (list_objs is None or len(list_objs) == 0):
            string_to_save = Base.to_json_string([])
        else:
            """
                convert to dictionary representation
                and perform JSON operation
            """
            for obj in list_objs:
                if not issubclass(type(obj), Base):
                    raise TypeError

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
            dummy = Rectangle(6, 7, 0, 0)
            dummy.update(**dictionary)
            return (dummy)

        if class_name == "Square":
            from models.square import Square
            dummy = Square(5, 0, 0)
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
                list_of_instances = [Rectangle.create(**dic)
                                     for dic in list_of_dict]
                return (list_of_instances)

        elif class_name == "Square":
            from models.square import Square
            filename = "./Square.json"
            if os.path.exists(filename):
                with open(filename, "r+", encoding="utf-8") as json_file:
                    json_string = json_file.read()  # read file
                list_of_dict = Base.from_json_string(json_string)
                list_of_instances = [Square.create(**dic)
                                     for dic in list_of_dict]
                return (list_of_instances)

        return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Creates a csv type file of class.__name__ and writes
            to it in csv formatted form.
        """
        class_name = cls.__name__
        filename = str(cls.__name__) + ".csv"

        if not isinstance(list_objs, list):
            list_to_iter = []

        elif list_objs is None or len(list_objs) == 0:
            list_to_iter = []

        else:

            for obj in list_objs:
                if not issubclass(type(obj), Base):
                    raise TypeError

            list_to_iter = [obj.to_dictionary() for obj in list_objs]

        if class_name == "Rectangle":
            with open(filename, "w", newline='') as csvfile:
                """
                    The fieldnames are the keys of the dictionary
                """
                fieldnames = ["id", "width", "height", "x", "y"]
                file_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                file_writer.writeheader()
                for dictionary in list_to_iter:
                    file_writer.writerow(dictionary)

        elif class_name == "Square":
            with open(filename, "w", newline='') as csvfile:
                fieldnames = ["id", "size", "x", "y"]
                file_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                file_writer.writeheader()
                for dictionary in list_to_iter:
                    file_writer.writerow(dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a csv file and returns instances of cls class"""
        # Get class name
        class_name = cls.__name__

        # Rectangle instances
        if class_name == "Rectangle":
            filename = "./Rectangle.csv"
            if os.path.exists(filename):
                from models.rectangle import Rectangle

                with open(filename, "r", newline="") as csvfile:
                    fieldnames = ["id", "width", "height", "x", "y"]
                    """
                        The fieldnames are ignored because the DictReader
                        class uses the values in the first row of the file
                        as fieldnames, and it returns eash row in a dictionary
                    """
                    list_of_dict = list(csv.DictReader(csvfile,
                                        fieldnames=None))
                    """
                        DictReader returns strings, hence the need for
                        conversion
                    """
                    for dic in list_of_dict:
                        for key in dic:
                            dic[key] = int(dic[key])

                list_of_instances = [Rectangle.create(**dic)
                                     for dic in list_of_dict]
                return (list_of_instances)

        elif class_name == "Square":
            filename = "./Square.csv"
            if os.path.exists(filename):
                from models.square import Square

                with open(filename, "r", newline="") as csvfile:

                    list_of_dict = list(csv.DictReader(csvfile,
                                        fieldnames=None))
                    for dic in list_of_dict:
                        for key in dic:
                            dic[key] = int(dic[key])

                list_of_instances = [Square.create(**dic)
                                     for dic in list_of_dict]
                return (list_of_instances)

        return ([])
