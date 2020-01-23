# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# BFS.py

from node import Node
import queue

# A list of states that have been visited already
visited = []


# Performs a BFS search on the start node until it's state equals the state of
# the end node
def search(start, goal):
    # Add state to list of visited states
    visited.append(start.toString())

    nodes = queue.Queue()
    nodes.put(start)

    while (not nodes.empty()):
        current = nodes.get()
        string = current.toString()
        if (current == start):
            print("{0}".format(string))
        else:
            print("{1}, cost = {2}, total cost = {3}\n{0}".format(
                string, current.action, current.cost, current.totalCost))
        if (string == goal.toString()):
            print("FOUND IT!!!")
            return
        current.findChildren()
        for child in current.children:
            if (child != None):
                childVisited = False
                for state in visited:
                    childString = child.toString()
                    if (childString == state):
                        childVisited = True
                if (childVisited == False):
                    visited.append(childString)
                    nodes.put(child)
    return
