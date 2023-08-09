#!/usr/bin/python3
def print_last_digit(number):
    l_d = abs(number) % 10
    print(l_d, end='')
    return l_d
