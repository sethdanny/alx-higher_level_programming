#!/usr/bin/python3
"""module for indentation"""


def text_indentation(text):
    """function which returns indented block of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for char in text:
        print(char, end="")
        if char in ".?:":
            print("\n\n", end="")
