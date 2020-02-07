# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# board.py

from random import randrange


# Board class contains variables for height and length of the number of boxes,
# and height and length of the board the boxes are in.
class Board:
    def __init__(self, length, height, user= "Player", bLength=0, bHeight=0, grid=[[]]):
        self.length = length
        self.height = height
        self.bLength = (self.length * 2) + 1
        self.bHeight = (self.height * 2) + 1
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


# Takes (x, y) coordinates of box to update, and direction to draw line.
# The first two lines Convert values from grid of lenght*height
# to grid of bLenght*bHeight
    def updateBoard(self, x, y, direction):
        x = (x * 2) + 1
        y = (y * 2) + 1
        print("x: {0}, y: {1}".format(x, y))
        if (direction == "T"):
            y -= 1
        elif (direction == "B"):
            y += 1
        elif (direction == "L"):
            x -= 1
        elif (direction == "R"):
            x += 1

        print("x: {0}, y: {1}".format(x, y))
        if (x % 2 == 0 and y % 2 == 1):
            if (self.grid[y][x] == ' '):
                self.grid[y][x] = '|'
            else:
                return "printHelp"
        elif (x % 2 == 1 and y % 2 == 0):
            if (self.grid[y][x] == '   '):
                self.grid[y][x] = '___'
            else:
                return "printHelp"
        return self.checkBoxes()

    def checkBoxes(self):
        return False


# Prints the board to the command line
    def prettyPrint(self):
        print('\n'.join([''.join([str(cell) for cell in row])
                         for row in self.grid]))
        return
