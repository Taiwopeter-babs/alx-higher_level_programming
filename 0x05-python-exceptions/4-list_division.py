#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new = []
    idx = 0

    if (not my_list_1 or my_list_2):
        if (not my_list_1):
            return (my_list_2)
        elif (not my_list_2):
            return (my_list_1)

    while (idx < list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new.append(result)
        idx += 1
    return (new)
