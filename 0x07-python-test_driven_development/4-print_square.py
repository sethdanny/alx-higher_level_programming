#!/usr/bin/python3
"""module to print a sqaure with # character"""


def print_square(size):
    """function which returns the square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
