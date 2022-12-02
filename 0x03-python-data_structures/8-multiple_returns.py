#!/usr/bin/python3


def multiple_returns(sentence):

    if (sentence):
        str_len = len(sentence)
        first_char = sentence[0]

    else:
        first_char = None
        str_len = 0

    new_tuple = (str_len, first_char)

    return (new_tuple)
