#!/usr/bin/python3
"""Module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an
object"""

def class_to_json(obj):
    """returns object description"""
    my_dict = {}
    for key, value in obj.__dict__.items():
        my_dict[key] = value
    return my_dict
