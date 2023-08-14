#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    add1, add2 = 0, 0

    if len(tuple_a) >= 1:
        add1 = tuple_a[0]
    if len(tuple_b) >= 1:
        add1 += tuple_b[0]

    if len(tuple_a) >= 2:
        add2 = tuple_a[1]
    if len(tuple_b) >= 2:
        add2 += tuple_b[1]

    return (add1, add2)
