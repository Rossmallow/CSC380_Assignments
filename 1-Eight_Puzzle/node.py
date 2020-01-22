# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# node.py

class Node:
    def __init__ (self, state, parent = None, zeroPos = 0, children = []):
        self.state = state
        self.parent = parent
        self.zeroPos = self.findVal(0, state)
        self.children = self.findChildren(state, zeroPos)

    # Find the children nodes for each action
    def getChildren (state, zeroPos):
            children = []
            children.append(state.up(state, zeroPos))
            children.append(state.down(state, zeroPos))
            children.append(state.left(state, zeroPos))
            children.append(state.right(state, zeroPos))
            return children

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def up (state, zeroPos):
        newState = state
        if (zeroPos != 7 & zeroPos != 8 & zeroPos != 9): # If tile can move up
            newState = self.swap(newState, zeroPos, zeroPos - 3)
            return Node(newState, self, zeroPos)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def down (state, zeroPos):
        newState = state
        if (zeroPos != 0 & zeroPos != 1 & zeroPos != 2): # If tile can move down
            newState = self.swap(newState, zeroPos, zeroPos + 3)
            return Node(newState, self, zeroPos)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def left (state, zeroPos):
        newState = state
        if (zeroPos != 3 & zeroPos != 6 & zeroPos != 9): # If tile can move left
            newState = self.swap(newState, zeroPos, zeroPos + 1)
            return Node(newState, self, zeroPos)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def right (state, zeroPos):
        newState = state
        if (zeroPos != 0 & zeroPos != 4 & zeroPos != 7): # If tile can move right
            newState = self.swap(newState, zeroPos, zeroPos - 1)
            return Node(newState, self, zeroPos)
        else:
            return None 

    # Finds a given value in a given state and returns its position
    def findVal (self, val, state):
        for i in range (0, len(state)):
            if state[i] == val:
                return i
    
    # Swaps the values of two positions
    def swap (pos1, pos2, state):
        value = state[pos1]
        state[pos1] = state[pos2]
        state[pos2] = value
        return state

            