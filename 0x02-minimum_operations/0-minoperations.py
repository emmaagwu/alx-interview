#!/usr/bin/env python3
"""
This module contains a function to calculate the fewest number of operations
needed to result in exactly n H characters in a text file using only 'Copy All'
and 'Paste' operations.
"""


def minOperations(n):
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

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]
