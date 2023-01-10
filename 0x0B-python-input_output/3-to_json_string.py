#!/usr/bin/python3
"""
    This module contains a function that performs i/o
"""
import json


def to_json_string(my_obj):
    """
    Serializes an object to json

    Args:
        obj(type: any): object to be serialized
    """
    return (json.dumps(my_obj, sort_keys=True))
