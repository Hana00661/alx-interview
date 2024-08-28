#!/usr/bin/python3
"""
N-Queens Challenge
"""

import sys


def solve_n_queens(n):
    """Solves the N-Queens problem.

    Args:
        n: The size of the chessboard.

    Returns:
        A list of solutions, where each solution is a list of tuples representing
        the queen positions.
    """

    solutions = []
    placed_queens = []  # coordinates format [row, column]
    solve_n_queens_helper(n, 0, placed_queens, solutions)
    return solutions


def solve_n_queens_helper(n, row, placed_queens, solutions):
    if row >= n:
        solutions.append(placed_queens[:])
        return

    for col in range(n):
        if is_safe(row, col, placed_queens):
            placed_queens.append((row, col))
            solve_n_queens_helper(n, row + 1, placed_queens, solutions)
            placed_queens.pop()


def is_safe(row, col, placed_queens):
    for queen_row, queen_col in placed_queens:
        if queen_col == col or queen_row == row or abs(queen_row - row) == abs(queen_col - col):
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print(solution)
