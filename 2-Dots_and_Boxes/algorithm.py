# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# algorithm.py

import math

from board import Board



def minimax (board, depth, alpha=None, beta=None, maximizingPlayer=True):
    moves = board.getAvailableMoves()
    if (depth == 0 or len(moves) == 0):
        return heuristic(board.state)
    if (maximizingPlayer):
        value = -math.inf
        for move in moves:
            x, y, direction = interpretDirection(move, board.bLength, 
                                                   board.bHeight)
            state = board.getUpdatedBoard(x, y, direction)
            child = Board(board.length, board.height, board.user, board.uScore, 
                          board.aScore, state, board.ownedBoxes)
            value = max(value, minimax(child, depth - 1, alpha, beta, False))

            if (alpha is not None):
                alpha = max(alpha, value)
            else: # alpha is None
                alpha = value
            if (alpha >= beta):
                break # Prune
        return value
    else: # maximizingPlayer is False
        value = math.inf
        for move in moves:
            x, y, direction = interpretDirection(move, board.bLength, 
                                                   board.bHeight)
            state = board.getUpdatedBoard(x, y, direction)
            child = Board(board.length, board.height, board.user, board.uScore, 
                          board.aScore, state, board.ownedBoxes)
            value = min(value, minimax(child, depth - 1, alpha, beta, True))

            if (beta is not None):
                beta = min(beta, value)
            else: # beta is None
                beta = value
            if (alpha >= beta):
                break # Prune
        return value


# Based on the x and y position, 
# a move including an x and y position along with a direction is returned.
def interpretDirection(move, bLength, bHeight):
    x = move[0]
    y = move[1]

    if (x % 2 == 0 and y % 2 == 1):
        if (x - 1 in range(bLength)):
            x = int((x - 2) / 2)
            y = int((y - 1) / 2)
            return (x, y, "R")
        else: # x + 1 is in range
            x = int(x / 2)
            y = int((y - 1) / 2)
            return (x, y, "L")
    if (x % 2 == 1 and y % 2 == 0):
        if (y - 1 in range(bHeight)):
            x = int((x - 1) / 2)
            y = int((y - 2) / 2)
            return (x, y, "B")
        else: # y + 1 is in range
            x = int((x - 1) / 2)
            y = int(y / 2)
            return (x, y, "T")

def heuristic(state):
    return 0