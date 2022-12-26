#!/usr/bin/python3
def add_integer(a, b=98):
    """ function to calculate two integers """

    if not isinstance(a, (int, float)):
        raise typeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise typeError("b must be an integer")

    return int(a) + int(b)
