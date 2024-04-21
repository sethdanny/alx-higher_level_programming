#!/usr/bin/python3
""" Module for Base Class
"""


class Base:
    """Class with private attributies __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Intantiate instance attributies
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
