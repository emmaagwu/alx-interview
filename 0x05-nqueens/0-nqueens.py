#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    """Checks if two queens are attacking each other.

    Args:
        pos1 (tuple): Position of the first queen.
        pos2 (tuple): Position of the second queen.

    Returns:
        bool: True if the queens are attacking each other, False otherwise.
    """
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or\
        abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def build_solutions(n, row, queens, solutions):
    """Recursively builds solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being processed.
        queens (list): Current queen positions.
        solutions (list): List of all valid solutions.
    """
    if row == n:
        solutions.append([list(queen) for queen in queens])
        return

    for col in range(n):
        new_queen = (row, col)
        if not any(is_attacking(new_queen, q) for q in queens):
            queens.append(new_queen)
            build_solutions(n, row + 1, queens, solutions)
            queens.pop()


def solve_n_queens(n):
    """Finds all solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all valid solutions.
    """
    solutions = []
    build_solutions(n, 0, [], solutions)
    return solutions


if __name__ == "__main__":
    n = get_input()
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
