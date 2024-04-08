#!/usr/bin/python3
"""
This module solves the N Queens problem.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on the board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row of the position to check.
        col (int): The column of the position to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if a queen can be placed, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N Queens problem using backtracking.

    Args:
        board (list): The chessboard.
        col (int): The column to place the next queen.
        n (int): The size of the chessboard.

    Returns:
        list: A list of lists representing the solved chessboard.
    """
    # Base case: If all queens are placed, return True
    if col == n:
        solutions.append([])
        for i in range(n):
            row = [j for j in range(n) if board[i][j] == 1]
            solutions[-1].append(row[0])
        return

    # Place this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, n)

            # If placing the queen in board[i][col] doesn't lead to a solution,
            # remove the queen from board[i][col]
            board[i][col] = 0


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
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

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(board, 0, n)

    # Print the solutions
    for solution in solutions:
        print(str(solution).replace(" ", "").replace(",", ""))
