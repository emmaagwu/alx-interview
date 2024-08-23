#!/usr/bin/python3
"""Module for determining the minimum number of coins needed to make change.
"""


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to achieve a given total
    using a set of coin denominations.

    Args:
        coins (list): A list of the available coin denominations.
        total (int): The target amount to reach.

    Returns:
        int: The fewest number of coins needed to reach the total. If it's not
        possible to meet the total with the given coins, returns -1.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    for coin in sorted_coins:
        if total == 0:
            break
        coins_used = total // coin
        coins_count += coins_used
        total -= coins_used * coin

    return coins_count if total == 0 else -1
