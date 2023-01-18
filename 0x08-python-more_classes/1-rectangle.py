#!/usr/bin/python3

""" module for a rectangle """


class Rectangle(object):
    """ creates a rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializing the data """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ sets the width of the instance """
        return self.__width

    @width.setter
    def width(self, value):
        """ gets the width of a rectangle class """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ sets the height of the rectangle class """
        return self.__height

    @height.setter
    def height(self, value):
        """ gets the height of the instance """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height = value
