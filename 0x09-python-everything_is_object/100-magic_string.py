#!/usr/bin/python3
"""magic function"""


def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Best, " * (magic_string.n - 1) + "School")
