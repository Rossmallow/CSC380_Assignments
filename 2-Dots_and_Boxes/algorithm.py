# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# algorithm.py

import math

from board import Board


# Minimax algorithm that alternates between trying to find the best move for 
# the AI, and the best move for the user.
def minimax(board, depth, alpha=(-math.inf, None), beta=(math.inf, None),
            maximizingPlayer=True, move=None):
    moves = board.getAvailableMoves()
    movesLeft = len(moves)

    # If no more moves or depth is reached, return a heuristic 
    # and the move to achieve it.
    if (movesLeft == 0 or depth == 0):
        return (board.aScore - board.uScore, move)

    if (maximizingPlayer):
        value = (-math.inf, None)
        for m in moves:
            board = copyBoard(board)
            board.updateBoard(m[0], m[1], m[2], "Algie")
            if (move is None):
                minimaxValue = minimax(board, depth - 1, alpha, beta, False, m)
            else:
                minimaxValue = minimax(board, depth - 1, alpha, beta, False, move)
            if (value[0] < minimaxValue[0]):
                value = minimaxValue
            if (alpha[0] < value[0]):
                alpha = value
            if (alpha[0] >= beta[0]):
               break # Prune
        return value
    else: # maximizingPlayer is False
        value = (math.inf, None)
        for m in moves:
            board = copyBoard(board)
            board.updateBoard(m[0], m[1], m[2], board.user)
            if (move is None):
                minimaxValue = minimax(board, depth - 1, alpha, beta, True, m)
            else:
                minimaxValue = minimax(board, depth - 1, alpha, beta, True, move)
            if (value[0] > minimaxValue[0]):
                value = minimaxValue
            if (beta[0] > value[0]):
                beta = value
            if (alpha[0] >= beta[0]):
                break # Prune
        return value


# Uses values of current board to create and return a copy of it.
def copyBoard(board):
    newBoardInfo = board.getInfo()
    newBoard = Board(newBoardInfo[0], newBoardInfo[1],newBoardInfo[2],
                     newBoardInfo[3], newBoardInfo[4], newBoardInfo[5],
                     newBoardInfo[6])
    return newBoard