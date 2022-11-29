#!/usr/bin/python3

for num in range(0, 100):
    if (num < 99):
        print("{i:02d}".format(i=num), end=", ")
    else:
        print("{}".format(num))
