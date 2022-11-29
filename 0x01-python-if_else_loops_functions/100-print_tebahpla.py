#!/usr/bin/python3


temp = 122

while (temp >= 97):
    print("{}".format(chr(temp) if temp % 2 == 0 else chr(temp - 32)), end='')
    temp -= 1
