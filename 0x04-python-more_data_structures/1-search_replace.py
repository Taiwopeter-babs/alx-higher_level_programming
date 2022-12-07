#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if (not my_list):
        return

    new = [] + list(map(lambda ch: ch if (ch != search) else replace,
                        my_list))
    return (new)
