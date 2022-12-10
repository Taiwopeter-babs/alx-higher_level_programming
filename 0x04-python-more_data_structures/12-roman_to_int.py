#!/usr/bin/python3


def roman_to_int(roman_string):
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    converted = 0

    if (not roman_string or type(roman_string) is not str):
        return (0)

    for idx, char in enumerate(roman_string):
        if (len(roman_string) > 1):
            if (idx == len(roman_string) - 1):
                converted += rom_num[char]
            else:
                if (rom_num[char] < rom_num[roman_string[idx + 1]]):
                    rom_num[char] *= -1

                converted += rom_num[char]
        else:
            converted += rom_num[char]

    return (converted)
