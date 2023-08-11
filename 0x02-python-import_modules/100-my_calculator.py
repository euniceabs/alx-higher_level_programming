#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        total_value = add(a, b)
    elif operator == '-':
        total_value = sub(a, b)
    elif operator == '*':
        total_value = mul(a, b)
    elif operator == '/':
        total_value = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {total_value}")
