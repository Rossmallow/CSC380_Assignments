# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# path.py

from node import Node
import sys


def printPath(current, start, message=""):
    if (len(message) > 0):
        print(message)
    path = findPath(current, start)
    print("Path found. Printing path...\n")
    for node in path:
        print("{0}, cost = {1}, total cost = {2}\n{3}".format(
            node.action, node.cost, node.totalCost, node.toString()))
    print("Goal!")


def findPath(current, start):
    path = []
    while (current.toString() != start.toString()):
        path.append(current)
        current = current.parent
    path.append(start)
    return path[::-1]


"""
def findPath(current, start, path):
    if (current.parent == None):
        path.append(current)
    else:
        path.append(current)
        findPath(current.parent, start, path)
    return path[::-1]
"""
