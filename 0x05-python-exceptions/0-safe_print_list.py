#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x number of elements in my_list[]


    Params:
            my_list[]: list containing the elements
            x: number of elements to print
    Return:
            number of elements printed
    """
    idx = 0

    while (idx < x):
        try:
            print(my_list[idx], end='')
        except IndexError:
            break
        idx += 1
    print()
    return (idx)
