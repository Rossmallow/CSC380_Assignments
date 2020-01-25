# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# path.py

from node import Node
import sys


# Iterates through the path and prints each node's action, cost, state,
# and the current total cost of the solution.
def printPath(current, start, time, space, message=""):
    length = 0
    cost = current.totalCost

    # Prints an optional message
    if (len(message) > 0):
        print(message)
    path = findPath(current, start)
    print("Path found. Printing path...\n")
    for node in path:
        length += 1
        print("{0}, cost = {1}, total cost = {2}\n{3}".format(
            node.action, node.cost, node.totalCost, node.toString()))
    print("Goal!")
    print("Length: {0}, Cost: {1}, Time: {2}, Space: {3}".format(
        length, cost, time, space))


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
