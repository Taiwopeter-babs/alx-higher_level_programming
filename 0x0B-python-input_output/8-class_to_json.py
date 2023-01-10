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
    encoded_json_data = json.dumps(obj.__dict__, sort_keys=True)
    decoded_json = json.loads(encoded_json_data)

    return (decoded_json)
