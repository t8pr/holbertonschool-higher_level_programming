#!/usr/bin/python3
"""Module that solves the N queens problem using backtracking."""
import sys


def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe.

    Args:
        board (list): Current queen placements.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively solves the N queens problem using backtracking.

    Args:
        n (int): Size of the board.
        row (int): Current row being processed.
        board (list): Current queen placements.
        solutions (list): List to store all solutions.
    """
    if row == n:
        solutions.append([queen[:] for queen in board])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve(n, row + 1, board, solutions)
            board.pop()


if __name__ == "__main__":
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
    solutions = []
    solve(n, 0, [], solutions)
    for sol in solutions:
        print(sol)
