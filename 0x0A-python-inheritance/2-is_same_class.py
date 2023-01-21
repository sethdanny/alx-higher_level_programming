#!/usr/bin/python3
""" module of task 2 """


def is_same_class(obj, a_class):
    """ returns true if an object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
