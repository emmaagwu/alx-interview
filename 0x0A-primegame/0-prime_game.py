#!/usr/bin/python3

""" Prime Game Algorithm Python """


def is_prime(n):
    """Checks if a given number n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_primes(n, primes):
    """
    Calculates and appends all primes up to n in the primes list.
    For non-prime numbers, append 0 to preserve index alignment.
    """
    current_max = primes[-1]  # Current highest prime
    if n > current_max:
        for i in range(current_max + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    Determines the winner after x rounds given an array of numbers nums.
    - x: number of rounds.
    - nums: list of integers where each number represents a round's limit.
    Returns the player ("Maria" or "Ben") with the most wins.
    If the result is a tie, return None.
    """
    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # Initialize prime numbers list.

    # Precompute primes up to the maximum number in nums
    calculate_primes(max(nums), primes)

    for round_num in range(x):
        num = nums[round_num]
        # Count the primes up to num
        primes_count = sum(1 for i in primes[:num + 1] if i != 0)

        # Determine the winner for the current round
        if primes_count % 2 == 1:
            winner = "Maria"
        else:
            winner = "Ben"

        # Update the win count for the winner
        players_wins[winner] += 1

    # Determine the overall winner
    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"
    else:
        return None
