#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ function to return firstname and lastname """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
