#!/usr/bin/python3
"""Module for creating pascal tirangle"""


def pascal_triangle(n):
    """Create a list containing the pascal triangle"""
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])
    triangle.append([1, 1])
    idx = 1
    while (n - 2) != 0:
        newList = []
        newList.append(1)
        innerList = 0
        for _ in triangle[idx]:
            try:
                newList.append(triangle[idx][innerList] +
                               triangle[idx][innerList + 1])
            except IndexError:
                pass
            innerList += 1
        newList.append(1)
        triangle.append(newList)
        n -= 1
        idx += 1

    return triangle
