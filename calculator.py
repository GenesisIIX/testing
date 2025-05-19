"""Simple calculator module with basic arithmetic operations and a CLI."""

import argparse


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main(argv=None):
    """Run a simple command-line interface for the calculator."""
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")
    args = parser.parse_args(argv)

    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "sub":
        result = subtract(args.a, args.b)
    elif args.operation == "mul":
        result = multiply(args.a, args.b)
    elif args.operation == "div":
        result = divide(args.a, args.b)
    else:
        raise AssertionError("Unhandled operation")

    print(result)


if __name__ == "__main__":
    main()
