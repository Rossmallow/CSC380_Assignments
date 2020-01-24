# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# DFS.py

from node import Node
import queue

# A list of states that have been visited already
visited = []


# Performs a DFS search on the start node until it's state equals the state of
# the end node
def search(start, goal):

    # Add state to list of visited states
    visited.append(start.toString())

    nodes = queue.LifoQueue()
    nodes.put(start)

    while (not nodes.empty()):
        current = nodes.get()
        string = current.toString()
        # if (current == start):
        #    print("{0}".format(string))
        # else:
        #    print("{1}, cost = {2}, total cost = {3}\n{0}".format(
        #        string, current.action, current.cost, current.totalCost))
        if (string == goal.toString()):
            print("Goal!")
            return
        current.findChildren()
        for child in current.children:
            if (child != None and child.toString() not in visited):
                visited.append(child.toString())
                nodes.put(child)
    return
