# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# node.py

class Node:
    def __init__ (self, state, parent = None, zeroPos = -1, children = []):
        self.state = state
        self.parent = parent
        if (zeroPos == -1):
            self.zeroPos = self.findVal(0, state)
        else:
            self.zeroPos = zeroPos
        if (len(children) == 0):
            self.children = self.findChildren(state, zeroPos)
        else:
            self.children = children

    # Find the children nodes for each action
    def findChildren (self, state, zeroPos):
            children = []
            children.append(self.up(state, zeroPos))
            children.append(self.down(state, zeroPos))
            children.append(self.left(state, zeroPos))
            children.append(self.right(state, zeroPos))
            return children

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def up (self, state, zeroPos):
        newState = state
        if (zeroPos >= 7): # If tile can move up
            print("up")
            newState = self.swap(newState, zeroPos, zeroPos - 3)
            return Node(newState, self, zeroPos - 3)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def down (self, state, zeroPos):
        newState = state
        if (zeroPos <= 2): # If tile can move down
            print("down")
            newState = self.swap(newState, zeroPos, zeroPos + 3)
            return Node(newState, self, zeroPos + 3)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def left (self, state, zeroPos):
        newState = state
        if (zeroPos != 3 & zeroPos != 6 & zeroPos != 9): # If tile can move left
            print("left")
            newState = self.swap(newState, zeroPos, zeroPos + 1)
            return Node(newState, self, zeroPos + 1)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def right (self, state, zeroPos):
        newState = state
        if (zeroPos != 0 & zeroPos != 4 & zeroPos != 7): # If tile can move right
            print("right")
            newState = self.swap(newState, zeroPos, zeroPos - 1)
            return Node(newState, self, zeroPos - 1)
        else:
            return None 

    # Finds a given value in a given state and returns its position
    def findVal (self, val, state):
        for i in range (0, len(state)):
            if state[i] == val:
                return i
    
    # Swaps the values of two positions
    def swap (self, state, pos1, pos2):
        value = state[pos1]
        state[pos1] = state[pos2]
        state[pos2] = value
        print ("Pos1: {0}, Pos2: {1}".format(state[pos1], state[pos2]))
        return state

            