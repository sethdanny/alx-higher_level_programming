#!/usr/bin/python3
"""module for indentation"""


def text_indentation(text):
    """function which returns indented block of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    else:
        text = text.replace(". ", ".").replace(": ", ":").replace("? ", "?")
        for i in text:
            if i == '.' or i == '?' or i == ':':
                print(i, end="")
                print("\n")
            else:
                print(i, end="")
