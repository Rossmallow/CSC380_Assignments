# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# box.py

from random import randrange


# Box class contains variables for value, owner,
# and booleans for each side of the box
class Box:
    def __init__(self, value=0, owner="", pos=[-1, -1], top=False, bottom=False, left=False,
                 right=False):
        if (value == 0):
            self.value = randrange(1, 6)  # Sets a random value [1, 2, 3, 4, 5]
        else:
            self.value = value
        if (owner == ""):
            self.setOwner(str(self.value))
        else:
            self.owner = owner
        self.pos = pos
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    # Defines how to represent a box
    def __repr__(self):
        return self.toString()

    # Sets the value of top to be the inverse of the current value
    def toggleTop(self):
        self.top = not self.top

    # Sets the value of bottom to be the inverse of the current value
    def toggleBottom(self):
        self.bottom = not self.bottom

    # Sets the value of left to be the inverse of the current value
    def toggleLeft(self):
        self.left = not self.left

    # Sets the value of right to be the inverse of the current value
    def toggleRight(self):
        self.right = not self.right

    # Checks if the booleans for each side is true. If they are, set the box's
    # owner to the passed value, and return the value of the box.
    # Otherwise, return 0.
    def checkComplete(self, owner):
        if (self.top and self.bottom and self.left and self.right):
            self.owner = owner
            return self.value
        else:
            return 0

    # Sets the box's owner
    def setOwner(self, owner):
        self.owner = owner

    # Sets the box's position
    def setPos(self, pos):
        self.pos = pos

    # Returns a string representation of a box
    def toString(self):
        string = "{0}".format(self.owner)
        return string
