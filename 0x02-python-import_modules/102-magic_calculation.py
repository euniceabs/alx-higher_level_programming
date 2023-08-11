#!/usr/bin/python3

def magic_calculation(a, b):
    import magic_calculation_102

    if a < b:
        add = magic_calculation_102.add

        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        sub = magic_calculation_102.sub
        return sub(a, b)
