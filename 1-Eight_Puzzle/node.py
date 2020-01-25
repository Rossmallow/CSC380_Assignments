# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# node.py


# Node class contains variables for state, parent node,
# the position of the empty tile within the state, the children nodes,
# the action used to reach the node, the cost used to reach the node,
# and the total cost of the current path
class Node:
    def __init__(self, state, parent=None, zeroPos=-1, children=[],
                 action="START", cost=0, totalCost=0, heuristic=0):
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
        self.heuristic = cost  # Equal to cost by default

    # The following functions say to compare nodes by their heuristic values
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __gt__(self, other):
        return self.heuristic > other.heuristic

    def __eq__(self, other):
        return self.heuristic == other.heuristic

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
        # If tile can move up
        if (zeroPos < 6):
            state = self.swap(state, zeroPos, zeroPos + 3)
            cost = state[zeroPos]
            return Node(state, self, zeroPos + 3, [], "UP", cost,
                        self.totalCost + cost, cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def down(self, state, zeroPos):
        # If tile can move down
        if (zeroPos > 2):
            state = self.swap(state, zeroPos, zeroPos - 3)
            cost = state[zeroPos]
            return Node(state, self, zeroPos - 3, [], "DOWN", cost,
                        self.totalCost + cost, cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def left(self, state, zeroPos):
        # If tile can move left
        if (zeroPos != 2 and zeroPos != 5 and zeroPos != 8):
            state = self.swap(state, zeroPos, zeroPos + 1)
            cost = state[zeroPos]
            return Node(state, self, zeroPos + 1, [], "LEFT", cost,
                        self.totalCost + cost, cost)
        else:
            return None

    # Creates and returns a node with an updated state after a move
    # If the move is impossible, return None
    def right(self, state, zeroPos):
        # If tile can move right
        if (zeroPos != 0 and zeroPos != 3 and zeroPos != 6):
            state = self.swap(state, zeroPos, zeroPos - 1)
            cost = state[zeroPos]
            return Node(state, self, zeroPos - 1, [], "RIGHT", cost,
                        self.totalCost + cost, cost)
        else:
            return None

    # Finds a given value in a given state and returns its position
    def findVal(self, val, state):
        for i in range(0, len(state)):
            if state[i] == val:
                return i

    # Swaps the values of two positions
    def swap(self, state, pos1, pos2):
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

    # Sets the node's heuristic value
    def setHeuristic(self, heuristic):
        self.heuristic = heuristic
        return
