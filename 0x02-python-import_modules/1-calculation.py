#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    Total_mul = mul(a, b)
    Total_add = add(a, b)
    Total_sub = sub(a, b)
    Total_div = div(a, b)

    print("{} + {} = {}".format(a, b, Total_add))
    print("{} - {} = {}".format(a, b, Total_sub))
    print("{} * {} = {}".format(a, b, Total_mul))
    print("{} / {} = {}".format(a, b, Total_div))
