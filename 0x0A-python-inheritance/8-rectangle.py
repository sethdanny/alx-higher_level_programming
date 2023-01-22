#!/usr/bin/python3
""" module for Geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ module for rectangle class """

    def __init__(self, width, height):
        """ Initialize rectangle data """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
