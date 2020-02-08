# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# board.py

from random import randrange


# Board class contains variables for height and length of the number of boxes,
# the user's name, the users's score, Algie's score, and the number of boxes 
# that are owned.
class Board:
    def __init__(self, length, height, user="Player", uScore=0, aScore=0,
                 ownedBoxes=0):
        self.length = length
        self.height = height
        self.user = user
        self.uScore = uScore
        self.aScore = aScore
        self.bLength = (self.length * 2) + 1
        self.bHeight = (self.height * 2) + 1
        self.grid = self.createBoard()
        self.ownedBoxes = ownedBoxes

# Creates the initial board and populates boxes with random numbers.
    def createBoard(self):
        grid = []
        for i in range(self.bHeight):
            row = []
            for j in range(self.bLength):
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
    def updateBoard(self, x, y, direction, player):
        x = (x * 2) + 1
        y = (y * 2) + 1
        #print("x: {0}, y: {1} d: {2}".format(x, y, direction))
        if (direction == "T"):
            y = y - 1
        elif (direction == "B"):
            y = y + 1
        elif (direction == "L"):
            x = x - 1
        elif (direction == "R"):
            x = x + 1
        #print("x: {0}, y: {1} d: {2}".format(x, y, direction))

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
        return self.checkBoxes(x, y, direction, player)


# Takes the index of a drawn line and the direction it is drawn, and calls
# checkBox on each of the adjacent boxes
    def checkBoxes(self, x, y, direction, player):
        winState = False
        if (direction == "T" or direction == "B" and not winState):
            if (y + 1 < self.bHeight and not winState):
                winState = self.checkBox(x, y + 1, player)
                #print("CHECK y + 1")
            if (y - 1 >= 0 and not winState):
                winState = self.checkBox(x, y - 1, player)
                #print("CHECK y - 1")
        elif (direction == "L" or direction == "R" and not winState):
            if (x + 1 < self.bLength and not winState):
                winState = self.checkBox(x + 1, y, player)
                #print("CHECK x + 1")
            if (x - 1 >= 0 and not winState):
                winState = self.checkBox(x - 1, y, player)
                #print("CHECK x - 1")
        return winState


# Checks the top, bottom, left, and right sides of the box. If any are empty,
# return. Else, enter the player's initial and add to their score.
    def checkBox(self, x, y, player):
        if (self.grid[y - 1][x] == '   ' or self.grid[y + 1][x] == '   '):
            #print('Nope ___')
            return
        elif (self.grid[y][x - 1] == ' ' or self.grid[y][x + 1] == ' '):
            #print('Nope |')
            return
        else:
            score = int(self.grid[y][x])
            self.grid[y][x] = " {0} ".format(player[:1])
            self.ownedBoxes += 1
            if (player == self.user):
                self.uScore += score
            else:
                self.aScore += score
            return self.checkWin()


# Checks if there is any empty spot in the grid. If there is, return False, 
# as there are more moves, else return True, as there are no more moves
    def checkWin(self):
        for i in range(self.bHeight):
            for j in range(self.bLength):
                if (self.grid[i][j].strip() == ''):
                    return False
                else:
                    return True

# Prints the board to the command line
    def prettyPrint(self):
        print('\n'.join([''.join([str(cell) for cell in row])
                         for row in self.grid]))
        print("{0}: {1}\n".format(self.user, self.uScore) +
              "Algie: {0}".format(self.aScore))
        return
