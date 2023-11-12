#!/usr/bin/python3
"""module for function to divide elements of a matrix in a list by a value """


def matrix_divided(matrix, div):
    """ function to divide elements of a matrix in a list by a value """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new_matrix = []

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(message)
        elif len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_list = []

        for i in rows:
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)

    return new_matrix
