#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = len(roman_string) - 1
    while i >= 0:
        value = roman_numerals[roman_string[i]]
        if i > 0 and value > roman_numerals[roman_string[i - 1]]:
            result -= value
        else:
            result += value
        i -= 1

    return result
