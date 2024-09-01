#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if not isinstance(grid, list) or not grid:
        return 0

    n = len(grid)
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            # Check the four potential edges (up, right, down, left)
            if i == 0 or grid[i - 1][j] == 0:  # Up
                perimeter += 1
            if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Right
                perimeter += 1
            if i == n - 1 or grid[i + 1][j] == 0:  # Down
                perimeter += 1
            if j == 0 or grid[i][j - 1] == 0:  # Left
                perimeter += 1

    return perimeter
