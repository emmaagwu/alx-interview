#!/usr/bin/python3 
"""
This module contains a function to calculate the fewest number of operations 
needed to result in exactly n H characters in a text file using only 'Copy All' 
and 'Paste' operations.
"""


def min_operations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H 
    characters in the file.

    Args:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations required.
    """
    if n <= 1:
        return 0
    
    # This function finds the minimum number of operations using the prime factorization method.
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
