# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# heuristics.py

from node import Node


# Finds a heuristic value equal to the number of
# misplaced tiles compared to goal
def incorrectTiles(state, goal):
    heuristic = 0
    state = state.state
    goal = goal.state

    for i in range(0, len(state)):
        if (state[i] != goal[i]):
            heuristic += 1
    return heuristic


def manhattanDistance(state, goal):
    heuristic = 0
    state = state.state
    goalState = goal.state

    for i in range(0, len(state)):
        if (state[i] != goalState[i]):
            valPos = goal.findVal(state[i], goalState)
            heuristic += abs(i - valPos)
    return heuristic
