#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:\n1: {}".format(args[0]))
    else:
        print("{} arguments:".format(num_args))

        for idx, arg in enumerate(args, start=1):
            print("{}: {}".format(idx, arg))
