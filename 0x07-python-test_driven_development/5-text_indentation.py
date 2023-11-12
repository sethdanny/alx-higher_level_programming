#!/usr/bin/python3
"""module for indentation"""


def text_indentation(text):
    """function which returns indented block of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    current_line = ""

    for char in text:
        current_line += char
        if char in ".?:":
            current_line = current_line.strip()
            print(current_line)
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
