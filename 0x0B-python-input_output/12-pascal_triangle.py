#!/usr/bin/python3
"""module to define pascals triangle"""


def pascal_triangle(n):
    """returns list of lists of integers in pascal's triangle"""

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
