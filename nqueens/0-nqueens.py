#!/usr/bin/python3
"""Solve the N queens problem"""
import sys

def n_not_valid():
    """Check if all passed value are correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return True
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return True
    if n < 4:
        print("N must be at least 4")
        return True
    return False

def is_safe(board, row, col):
    """Check if this position is safe"""
    for queen in board:
        queen_row = queen[0]
        queen_col = queen[1]

        if queen_col == col:
            return False
        if abs(queen_row - row) == abs(queen_col - col):
            return False
    return True

def solve(row, n, board):
    """Solve the problem with recursion"""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve(row + 1, n, board)
            board.pop()

if __name__ == "__main__":
    if n_not_valid():
        exit(1)
    
    N = int(sys.argv[1])

    solve(0, N, [])
