#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    for j in range(x):
        try:
            if type(my_list[j]) is int:
                print("{:d}".format(my_list[j]), end="")
                int_count += 1
        except (TypeError, ValueError):
            pass
    print()
    return int_count
