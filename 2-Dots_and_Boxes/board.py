# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# board.py

from random import randrange


# Board class contains variables for height and length of the number of boxes,
# and height and length of the board the boxes are in.
class Board:
    def __init__(self, length, height, bLength=0, bHeight=0, grid=[[]]):
        self.length = length
        self.height = height
        self.bLength = (self.length ** 2) + 1
        self.bHeight = (self.height ** 2) + 1
        if (grid == [[]]):
            self.grid = self.createBoard()
        else:
            self.grid = grid

# Creates the initial board and populates boxes with random numbers.
    def createBoard(self):
        grid = []
        for i in range(self.bLength):
            row = []
            for j in range(self.bHeight):
                if (i % 2 == 0 and j % 2 == 0):
                    row.append('.')
                elif (i % 2 == 1 and j % 2 == 1):
                    row.append(' {0} '.format(randrange(1, 6)))
                elif (i % 2 == 0 and j % 2 == 1):
                    row.append('   ')
                elif (i % 2 == 1 and j % 2 == 0):
                    row.append(' ')
            grid.append(row)
        return grid

# Prints the board to the command line
    def prettyPrint(self):
        print('\n'.join([''.join([str(cell) for cell in row])
                         for row in self.grid]))
        return
