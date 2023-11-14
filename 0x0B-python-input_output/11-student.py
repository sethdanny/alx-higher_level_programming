#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if isinstance(attrs, list) and\
            all(isinstance(item, str)
                for item in attrs):
            return {key: value
                    for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        for key, value in json.items():
            self.__dict__[key] = value
