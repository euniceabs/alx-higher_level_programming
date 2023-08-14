#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first_element = True
        for number in row:
            if not first_element:
                print(" ", end="")
            print("{:d}".format(number), end="")
            first_element = False
        print()
    if not matrix:
        print()
