#!/usr/bin/python3

def magic_calculation(a, b):
    result_value = 0

    for loop_index in range(1, 3):
        try:
            if loop_index > a:
                raise Exception("Too far")
            result_value += (a ** b) / loop_index
        except Exception:
            result_value = b + a
            break

    return result_value
