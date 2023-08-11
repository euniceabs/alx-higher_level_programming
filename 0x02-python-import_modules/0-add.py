#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add

    def add(a, b):
        return a + b

    a = 1
    b = 2
    grand_total = add(a, b)
    print(f'{a} + {b} = {a + b}')
