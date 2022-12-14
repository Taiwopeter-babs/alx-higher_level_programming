#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def arithmetic():
    operators = ["+", "-", "*", "/"]
    functions = [add, sub, mul, div]
    
    length = len(sys.argv) - 1
    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[3])
    
    if (operator == "*"):
        res = mul(arg1, arg2)
    elif (operator == "+"):
        res = add(arg1, arg2)
    print("{} {} {} = {}".format(arg1, operator, arg2, res))
    i = 0
    while (i < len(operators)):
        if (sys.argv[2] == operators[i]):
            res = functions[i](arg1, arg2)
            print("{} {} {} = {}".format(arg1, operators[i], arg2, res))
            exit(0)
        i += 1
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)    
