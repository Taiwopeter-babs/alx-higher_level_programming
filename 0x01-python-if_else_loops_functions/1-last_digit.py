#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = number

result = num % 10


if (num < 0):
    string = f"Last digit of {num} is"
    num *= -1
    result = num % 10
    print(f"{string} -{result} and is less than 6 and not 0")

elif (num > 0):
    string = f"Last digit of {num} is"
    result = num % 10
    if (result > 5):
        print(f"{string} {result} and is greater than 5")
    elif (result < 6 and result > 0):
        print(f"{string} {result} and is less than 6 and not 0")
    elif (result == 0):
        print(f"{string} is 0 and is 0")

elif (num == 0):
    print("Last digit of 0 is 0 and is 0")
