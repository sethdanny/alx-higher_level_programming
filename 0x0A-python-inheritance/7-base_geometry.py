#!/usr/bin/python3
""" module for Geometry """


class BaseGeometry:
    """ empty Geometry class """

    def __init__(self):
        """ Initialise data """
        pass

    def area(self):
        """ calculates the area of a geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validtaes integer value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
