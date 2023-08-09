#!/usr/bin/python3
for current_letter in range(97, 123):
    if current_letter != 113 and current_letter != 101:
        print("{0}".format(chr(current_letter)), end="")
