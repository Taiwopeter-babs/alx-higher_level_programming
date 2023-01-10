#!/usr/bin/python3
"""
    This module contains a function that performs i/o
    with json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes object to json file

    Args:
        my_obj: object to be serialized
        filename(str): filename of file accepting json
    """
    with open(filename, "w+", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
