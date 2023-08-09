#!/usr/bin/python3
output_str = ""
for ascii_value in range(122, 96, -1):
    if ascii_value % 2 == 0:
        output_str += chr(ascii_value)
    else:
        output_str += chr(ascii_value - 32)

print("{}".format(output_str), end="")
