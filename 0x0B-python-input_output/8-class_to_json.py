#!/usr/bin/python3
"""
    This module contains a function that returns
    a dictionary object
"""
import json


def class_to_json(obj):
    """
        Return a dictionary
    """
    with open("./dump.json", "w+", encoding="utf-8") as my_file:
        json.dump(obj.__dict__, my_file)

    with open("./dump.json", "r+", encoding="utf-8") as my_file:
        ret = json.load(my_file)

    return (ret)
