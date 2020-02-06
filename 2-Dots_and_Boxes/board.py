# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# board.py

from box import Box


class Board:
    def __init__(self, length, height, grid=None):
        self.length = length
        self.height = height
        if (grid is not None):
            self.grid = grid
        else:
            self.grid = self.createBoard()

    def createBoard(self):
        grid = []
        for i in range(self.length):
            grid.append([])
            for j in range(self.height):
                grid[i].append(Box())
        return grid

    def prettyPrint(self):
        board = [[None] * ((self.height ** 2) + 1)] * ((self.length ** 2) + 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                s = 'i: {0}, j: {1}'.format(i, j)
                board[i][j] = s
                print(s)
        print(board)
        return