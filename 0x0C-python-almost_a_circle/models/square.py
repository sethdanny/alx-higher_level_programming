#!/usr/bin/python3
"""Sqaure module."""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class which inherits attributies and method of Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor to initialize sqaure attributies"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """String representation of a square"""

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.__width}'

    @property
    def size(self):
        """retreives the size of width"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the size of width and height"""
        if not isinstance(value, int):
            raise TypeError('width and height must be an integer')

        if value <= 0:
            raise ValueError('width and height must be > 0')
        self.__width = value
