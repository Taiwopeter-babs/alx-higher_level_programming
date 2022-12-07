#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if (not a_dictionary):
        return

    if (value not in a_dictionary.values()):
        return (a_dictionary)

    # new = {key: val for (key, val) in a_dictionary.items()
    # if a_dictionary[key] != value}
    # print(new)

    for key in a_dictionary.copy():
        if (a_dictionary[key] == value):
            del a_dictionary[key]

    return (a_dictionary)
