# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# node.py


class Node:
    def __init__(self, state, parent=None, zeroPos=-1, children=[], action="",
                 cost=0, totalCost=0):
        self.state = state
        self.parent = parent
        if (zeroPos == -1):
            self.zeroPos = self.findVal(0, state)
        else:
            self.zeroPos = zeroPos
        self.children = children
        self.action = action
        self.cost = cost
        self.totalCost = totalCost

    # Find the children nodes for each action
    def findChildren(self):
        if (len(self.children) == 0):
            newState = self.state.copy()
            self.children.append(self.up(newState, self.zeroPos))
            newState = self.state.copy()
            self.children.append(self.down(newState, self.zeroPos))
            newState = self.state.copy()
            self.children.append(self.left(newState, self.zeroPos))
            newState = self.state.copy()
            self.children.append(self.right(newState, self.zeroPos))
        else:
            return

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def up(self, state, zeroPos):
        if (zeroPos < 6):  # If tile can move up
            # print("up")
            state = self.swap(state, zeroPos, zeroPos + 3)
            cost = state[zeroPos]
            return Node(state, self, zeroPos + 3, [], "UP", cost,
                        self.totalCost + cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def down(self, state, zeroPos):
        if (zeroPos > 2):  # If tile can move down
            # print("down")
            state = self.swap(state, zeroPos, zeroPos - 3)
            cost = state[zeroPos]
            return Node(state, self, zeroPos - 3, [], "DOWN", cost,
                        self.totalCost + cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def left(self, state, zeroPos):
        if (zeroPos != 2 & zeroPos != 5 & zeroPos != 8):  # If tile can move left
            # print("left")
            state = self.swap(state, zeroPos, zeroPos + 1)
            cost = state[zeroPos]
            return Node(state, self, zeroPos + 1, [], "LEFT", cost,
                        self.totalCost + cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def right(self, state, zeroPos):
        if (zeroPos != 0 & zeroPos != 3 & zeroPos != 6):  # If tile can move right
            # print("right")
            state = self.swap(state, zeroPos, zeroPos - 1)
            cost = state[zeroPos]
            return Node(state, self, zeroPos - 1, [], "RIGHT", cost,
                        self.totalCost + cost)
        else:
            return None

    # Finds a given value in a given state and returns its position
    def findVal(self, val, state):
        for i in range(0, len(state)):
            if state[i] == val:
                return i

    # Swaps the values of two positions
    def swap(self, state, pos1, pos2):
        # print("Pos1: {0} val1: {1}, Pos2: {2} val2: {3}".format(
        #     pos1, state[pos1], pos2, state[pos2]))
        value = state[pos1]
        state[pos1] = state[pos2]
        state[pos2] = value
        return state

    # Prints the state as a string
    def toString(self):
        string = ''
        for val in self.state:
            string += ("{0}, ".format(val))
        string = string.strip(', ')
        return string
