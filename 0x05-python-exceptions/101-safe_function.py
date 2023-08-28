#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        function_result = fct(*args)
    except Exception as exception_message:
        sys.stderr.write("Exception: {}\n".format(exception_message))
        return None
    else:
        return function_result
