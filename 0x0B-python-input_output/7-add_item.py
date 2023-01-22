#!/usr/bin/python3
"""
    This module is scripted to perform i/o
    with json

    Creates an object that accepts arguments from the command line,
    and appends them each to a list. The list is serialized to json
    file.
"""
import json
import sys
import os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def save_strings_from_command_line():
    filename = "./add_item.json"
    obj = []
    length = len(sys.argv)

    # if file doesn't exist, create it
    if not os.path.exists(filename):
        save_to_json_file(obj, filename)

    # load the json file into python object
    obj = load_from_json_file(filename)

    # append command line strings into the list
    idx = 1
    while idx < length:
        obj.append(sys.argv[idx])
        idx += 1

    # save/dump to json file
    save_to_json_file(obj, filename)


if __name__ == "__main__":
    save_strings_from_command_line()
