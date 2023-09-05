#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def is_safe(board, row, col, size):
    """
    Checks if it is safe to place a queen at a given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        size (int): The size of the chessboard.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < size:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(size):
    """
    Solves the N Queens problem and returns all possible solutions.

    Args:
        size (int): The size of the chessboard.

    Returns:
        list: A list of all possible solutions to the N Queens problem.
    """
    def backtrack(board, row):
        # Base case: All queens have been placed
        if row == size:
            solutions.append([board[i][:] for i in range(size)])
            return

        # Try placing a queen in each column of the current row
        for col in range(size):
            if is_safe(board, row, col, size):
                # Place the queen
                board[row][col] = 1

                # Move on to the next row
                backtrack(board, row + 1)

                # Remove the queen (backtracking)
                board[row][col] = 0

    # Initialize an empty chessboard
    board = [[0] * size for _ in range(size)]
    solutions = []

    # Start backtracking from the first row
    backtrack(board, 0)

    return solutions


if __name__ == "__main__":
    # Parse the command line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens size")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
        if size < 4:
            raise ValueError
    except ValueError:
        print("Size must be an integer greater or equal to 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_nqueens(size)

    # Print the solutions
    for solution in solutions:
        print([[i, solution[i].index(1)] for i in range(size)])
