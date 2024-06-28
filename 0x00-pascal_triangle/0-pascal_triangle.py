#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # first element of each row is 1
        for j in range(1, i):
            # sum of the two elements above this element in the triangle
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # last element of each row is 1
        triangle.append(row)

    return triangle
