#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, (int, str)):
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
