#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints x number of elements in my_list[] that are only integers
        skips past non-integer values, but raises when index is out of
        range

    Params:
            my_list[]: list containing the elements
            x: number of elements to print
    Return:
            number of elements printed
    """
    idx = 0
    val = 0
    if (my_list):
        while (idx < x):
            try:
                print("{:d}".format(my_list[idx]), end='')
            except (TypeError, ValueError):
                pass
            except IndexError:
                raise
            else:
                val += 1
            idx += 1
        print()
        return (val)
    else:
        return (0)
