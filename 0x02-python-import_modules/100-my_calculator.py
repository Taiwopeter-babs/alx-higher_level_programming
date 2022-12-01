#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def arithmetic():
    operators = ["+", "-", "*", "/"]
    functions = [add, sub, mul, div]

    length = len(argv) - 1
    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    arg1 = int(argv[1])
    arg2 = int(argv[3])

    i = 0
    while (i < len(operators)):
        if (argv[2] == operators[i]):
            res = functions[i](arg1, arg2)
            print("{} {} {} = {}".format(arg1, operators[i], arg2, res))
            exit(0)
        i += 1
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)


if __name__ == "__main__":
    arithmetic()
