#!/usr/bin/python3
""" module for class list and its sub class"""


class MyList(list):
    """ subclass inherites from list class """

    def print_sorted(self):
        """ print a sorted copy of list """
        new_list = list.copy(self)
        list.sort(new_list)
        print(new_list)
