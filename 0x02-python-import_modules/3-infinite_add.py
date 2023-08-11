#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    int_args = []
    for arg in sys.argv[1:]:
        int_args.append(int(arg))

    sum_args = sum(int_args)
    print(sum_args)
