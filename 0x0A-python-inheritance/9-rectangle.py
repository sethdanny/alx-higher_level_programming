#!/usr/bin/python3
""" module for Geometry """


BaseGeometry = __import__('8-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ module for rectangle class """

    def __init__(self, width, height):
        """ Initialize rectangle object """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area """
        return self.__width * self.__height
    
    def __str__(self):
        return f"[Rectangle] {self.__width} / {self.__height}"
