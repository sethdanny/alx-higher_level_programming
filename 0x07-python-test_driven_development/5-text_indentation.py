#!/usr/bin/python3
"""module for indentation"""


def text_indentation(text):
    """function which returns indented block of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """end_characters = ['.', '?', ':']
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in end_characters:
            new_text += "\n\n"
            i += 1
            while text[i] == " ":
                i += 1
            continue
        i += 1
    print(new_text, end="") """
    text = text.strip()
    for char in text:
        print(char, end="")
        if char in ".?:":
            print("\n\n", end="")
