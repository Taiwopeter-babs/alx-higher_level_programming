#!/usr/bin/python3
import sys


if __name__ == "__main__":

    length = len(sys.argv) - 1

    if (length == 0):
        print("{}".format(length))

    elif (length == 1):
        print("{}".format(sys.argv[1]))

    elif (length > 1):

        result = 0

        for idx in range(1, length + 1):
            result += int(sys.argv[idx])
            final = result
        print("{}".format(final))
