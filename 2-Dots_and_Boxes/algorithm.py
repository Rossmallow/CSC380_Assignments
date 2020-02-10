# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# algorithm.py

import math

from board import Board

def minimax(board, depth, alpha=(-math.inf, None), beta=(math.inf, None),
            maximizingPlayer=True):
    moves = board.getAvailableMoves()
    print("MOVES: {0}".format(moves))
    movesLeft = len(moves)
    if (depth == 0 or movesLeft >= 1):
        move = moves.pop()
        print("MOVE: {0}".format(move))
        return getHeuristic(board, move), move
    elif (maximizingPlayer):
        value = (-math.inf, None)
        for move in moves:
            board = copyBoard(board)
            board.updateBoard(move[0], move[1], move[2], "Algie")
            minimaxValue = minimax(board, depth - 1, alpha, beta, False)
            print("MAX value: {1}, minimaxValue: {0} ".format(minimaxValue[0], 
                                                              value[0]))
            if (value[0] < minimaxValue[0]):
                value = minimaxValue
            if (alpha[0] < value[0]):
                alpha = value
            if (alpha[0] >= beta[0]):
               break # Prune
        return value
    else: # maximizingPlayer is False
        value = (math.inf, None)
        for move in moves:
            board = copyBoard(board)
            board.updateBoard(move[0], move[1], move[2], "Algie")
            minimaxValue = minimax(board, depth - 1, alpha, beta, True)
            print("MIN value: {1}, minimaxValue: {0} ".format(minimaxValue[0], 
                                                              value[0]))
            if (value[0] > minimaxValue[0]):
                value = minimaxValue
            if (beta[0] > value[0]):
                beta = value
            if (alpha[0] >= beta[0]):
                break # Prune
        return value


def updateState(state, x, y, direction):
    x, y = convertIndexValues(x, y, direction)

    if (x % 2 == 0 and y % 2 == 1):
        if (state[x][y] == ' '):
            state[x][y] = '|'
    elif (x % 2 == 1 and y % 2 == 0):
        if (state[x][y] == '   '):
            state[x][y] = '___'
    return state


def getHeuristic(board, move):
    x = move[0]
    y = move[1]
    direction = move[2]
    print("x: {0}, y: {1}, direction: {2}".format(x, y, direction))
    x, y = convertIndexValues(x, y, direction)
    print("x: {0}, y: {1}".format(x, y))
    state = board.getState()
    state[y][x] = 'LINE'
    heuristic = 0

    if (direction == "T" or direction == "B"):
        if (y + 1 < board.bHeight):
            heuristic += getBoxHeuristic(state, x, y + 1)
        if (y - 1 >= 0):
            heuristic += getBoxHeuristic(state, x, y - 1)
    elif (direction == "L" or direction == "R"):
        if (x + 1 < board.bLength):
            heuristic += getBoxHeuristic(state, x + 1, y)
        if (x - 1 >= 0):
            heuristic += getBoxHeuristic(state, x - 1, y)

    print("HEURIISTIC: {0}".format(heuristic))
    return heuristic


def getBoxHeuristic(state, x, y):
    if (not state[x][y].strip().isdigit()):
        print("NOT DIGIT" + state[x][y])
        return 0
    heuristic = int(state[x][y])
    print("x: {0}, y: {1}, heuristic: {2}".format(x, y, heuristic))

    if (state[y - 1][x] == '   ' or state[y + 1][x] == '   '):
        return heuristic
    elif (state[y][x - 1] == ' ' or state[y][x + 1] == ' '):
        return heuristic
    else: # Box is complete
        return heuristic + (heuristic * 100)


def convertIndexValues(x, y, direction):
    x = (x * 2) + 1
    y = (y * 2) + 1
    if (direction == "T"):
        y = y - 1
    elif (direction == "B"):
        y = y + 1
    elif (direction == "L"):
        x = x - 1
    elif (direction == "R"):
        x = x + 1
    return x, y


def copyBoard(board):
    newBoardInfo = board.getInfo()
    newBoard = Board(newBoardInfo[0], newBoardInfo[1],newBoardInfo[2],
                     newBoardInfo[3], newBoardInfo[4], newBoardInfo[5],
                     newBoardInfo[6])
    return newBoard