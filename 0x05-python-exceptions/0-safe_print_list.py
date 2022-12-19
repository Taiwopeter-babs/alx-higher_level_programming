#!usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        for idx, ele in enumerate(my_list):
            if (idx < x):
                print(my_list[idx], end='')
            idx += 1
        print()
    except IndexError:
        return (None)
    else:
        return (idx)
