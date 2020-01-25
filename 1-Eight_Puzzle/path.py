# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# path.py

from node import Node
import sys


# Iterates through the path and prints each node's action, cost, state,
# and the current total cost of the solution.
def printPath(current, start, message=""):
    # Prints an optional message
    if (len(message) > 0):
        print(message)
    path = findPath(current, start)
    print("Path found. Printing path...\n")
    for node in path:
        print("{0}, cost = {1}, total cost = {2}\n{3}".format(
            node.action, node.cost, node.totalCost, node.toString()))
    print("Goal!")


# Starting with the current node, add it to a list, then add its parent,
# and so on until the start node has been found.
def findPath(current, start):
    path = []
    while (current.toString() != start.toString()):
        path.append(current)
        current = current.parent
    path.append(start)
    # Return the reversed list
    return path[::-1]
