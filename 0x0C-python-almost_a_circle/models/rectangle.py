#!/usr/bin/python3
""" Module for rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ Class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle instances"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Retrieves the area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the Rectangle instance with the # character."""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """returns string representation of a rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                 self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            raise ValueError("Atleast one argument is required")
        
    def to_dictionary(self):
        """Represents dictionary of a rectangle"""

        my_dict = { 'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict