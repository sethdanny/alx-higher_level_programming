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
