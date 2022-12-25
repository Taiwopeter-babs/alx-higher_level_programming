#!/usr/bin/python3
"""
    This module contains a function that prints portions of a text, and
    delimits them with specified characters, separating the portions
    with two lines.

    Args:
        text: This argument can have leading and trailing white spaces
            and even spaces in between. It must be a string instance.
    Raises:
        TypeError: if `text` argument is not a string.

    Example:
        >>> text = "    Chemistry. An interesting study?  Ans:  Yes   "
        >>> text_indentation(text)
        Chemistry.
        An interesting study?
        Ans:
        Yes>>>
"""


def text_indentation(text):
    """Prints portions of text with delimiters separated by two lines"""

    chars = ['.', '?', ':']
    sep = ["\t", " ", "\r", "\n", "\r"]
    new = ""

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespaces
    _text = text.strip()

    # Remove whitespaces in between texts after specified separators
    for idx, char in enumerate(_text):
        if _text[idx] in sep and _text[idx - 1] in chars:
            continue
        elif _text[idx] in sep and _text[idx + 1] in sep:
            continue
        elif _text[idx] in sep and _text[idx - 1] in sep:
            continue
        new += _text[idx]

    for char in new:
        if char in chars:
            print("{}\n".format(char))
            continue
        print(char, end='')
