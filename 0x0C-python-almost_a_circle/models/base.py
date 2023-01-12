#!/usr/bin/python3
"""
    This module contains a class: Base
"""

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
