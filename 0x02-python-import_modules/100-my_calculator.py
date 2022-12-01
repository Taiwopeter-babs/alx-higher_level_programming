#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def tee_calc():
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    length = len(argv) - 1
    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    arg1 = int(argv[1])
    arg2 = int(argv[3])

    if (operator not in operations):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operations[operator](arg1, arg2)
    print("{} {} {} = {}".format(arg1, operator, arg2, result))


if __name__ == "__main__":
    tee_calc()
