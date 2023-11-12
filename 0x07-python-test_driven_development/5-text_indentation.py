#!/usr/bin/python3
"""module for indentation"""


def text_indentation(text):
    """function which returns indented block of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_characters = ['.', '?', ':']

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        print(line)
        if line[-1] in end_characters:
            print()
