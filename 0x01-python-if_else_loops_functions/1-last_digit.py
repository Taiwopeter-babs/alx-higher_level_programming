#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

result = number % 10

if (number < 0):
    result *= -1

string = "The last digit of {} is {}".format(number, result)

if (result > 5):
    print(string + ' ' + "and is greater than 5")
elif (result < 6 and result != 0):
    print(string + ' ' + "and is less than 6 and is not 0")
elif (result == 0):
    print(string + ' ' + "and is 0")
