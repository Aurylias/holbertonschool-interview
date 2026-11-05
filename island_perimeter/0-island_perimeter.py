#!/usr/bin/python3
"""A grid representing an island"""


def island_perimeter(grid):
    """Takes a rectangular grid with a width or height maximum of 100.
       O is water and 1 island. Lakes are not allowed. Return it's perimeter"""

    perimeter = 0
    rows = len(grid)
    if rows > 0:
        cols = len(grid[0])
    else:
        cols = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
