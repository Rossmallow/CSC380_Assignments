# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# board.py

from random import randrange


# Board class contains variables for height and length of the number of boxes,
# the user's name, the users's score, Algie's score, and the number of boxes 
# that are owned.
class Board:
    def __init__(self, length, height, user="Player", uScore=0, aScore=0,
                 state=None, ownedBoxes=0):
        self.length = length
        self.height = height
        self.user = user
        self.uScore = uScore
        self.aScore = aScore
        self.bLength = (self.length * 2) + 1
        self.bHeight = (self.height * 2) + 1
        if (state is None):
            self.state = self.createBoard()
        else: # state is not None
            self.state = state
        self.ownedBoxes = ownedBoxes

# Creates the initial board and populates boxes with random numbers.
    def createBoard(self):
        state = []
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
            state.append(row)
        return state


# Takes (x, y) coordinates of box to update, and direction to draw line.
# The first two lines Convert values from state of lenght*height
# to state of bLenght*bHeight
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
            if (self.state[y][x] == ' '):
                self.state[y][x] = '|'
            else:
                return "printHelp"
        elif (x % 2 == 1 and y % 2 == 0):
            if (self.state[y][x] == '   '):
                self.state[y][x] = '___'
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
        if (self.state[y - 1][x] == '   ' or self.state[y + 1][x] == '   '):
            #print('Nope ___')
            return
        elif (self.state[y][x - 1] == ' ' or self.state[y][x + 1] == ' '):
            #print('Nope |')
            return
        else:
            score = int(self.state[y][x])
            self.state[y][x] = " {0} ".format(player[:1].upper())
            self.ownedBoxes += 1
            if (player == self.user):
                self.uScore += score
            else:
                self.aScore += score
            movesLeft = self.getAvailableMoves()
            if (len(movesLeft) == 0):
                return True
            else: # No moves left
                return False


# Loops through the state and returns a list
# with the locations of all available moves
    def getAvailableMoves(self):
        moves = []
        for i in range(self.bHeight):
            for j in range(self.bLength):
                if (self.state[i][j].strip() == ''):
                    moves.append((i, j))
        return moves


# Prints the board to the command line
    def prettyPrint(self):
        print('\n'.join([''.join([str(cell) for cell in row])
                         for row in self.state]))
        print("{0}: {1}\n".format(self.user, self.uScore) +
              "Algie: {0}".format(self.aScore))
        return
