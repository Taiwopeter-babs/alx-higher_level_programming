#!/usr/bin/python3

for num1 in range(0, 10):
    for num2 in range(0, 10):
        if (num1 < num2 and num1 + num2 < 17):
            print("{}{}".format(num1, num2), end=", ")
        elif (num1 < num2 and num1 + num2 == 17):
            print("{}{}".format(num1, num2))
