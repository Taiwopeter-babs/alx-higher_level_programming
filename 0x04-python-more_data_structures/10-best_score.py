#!/usr/bin/python3


def best_score(a_dictionary):
    if (not a_dictionary):
        return (None)

    scores = [value for value in a_dictionary.values()]

    max_val = max(scores)

    for key in a_dictionary.keys():
        if (a_dictionary[key] == max_val):
            break

    return (key)
