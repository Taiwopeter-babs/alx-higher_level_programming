#!/usr/bin/python3
"""
    This module contains a function that performs i/o
"""
import json


def from_json_string(my_str):
    """
    Serializes an object to json

    Args:
        obj(type: any): object to be serialized
    """
    return (json.loads(my_str))
