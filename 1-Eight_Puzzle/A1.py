# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# A1.py

from node import Node
from path import findPath, printPath
import queue


# Performs a BFS search on the start node until it's state equals the state of
# the end node
def search(start, goal):
    visited = set()
    nodes = queue.PriorityQueue()

    visited.add(start.toString())
    nodes.put(start)

    print("Finding the goal state...")
    while (not nodes.empty()):
        current = nodes.get()
        string = current.toString()
        # Uncomment below to print nodes as they are explored
        """
        if (current == start):
            print("{0}".format(string))
        else:
            print("{1}, cost = {2}, total cost = {3}\n{0}".format(
                string, current.action, current.cost, current.totalCost))
        """
        if (string == goal.toString()):
            printPath(current, start, "Goal state found. Finding path...")
            return
        current.findChildren()
        for child in current.children:
            if (child is not None and child.toString() not in visited):
                visited.add(child.toString())
                child.setHeuristic(
                    child.cost + heuristicValue(child.state, goal.state))
                nodes.put(child)
    return


# Finds a heuristic value equal to the number of
# misplaced tiles compared to goal
def heuristicValue(state, goal):
    heuristic = 0

    i = 0
    while (i < len(state)):
        if (state[i] != goal[i]):
            heuristic += 1
        i += 1
    return heuristic
