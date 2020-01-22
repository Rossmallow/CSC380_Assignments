# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# puzzle.py

from node import Node
import BFS, DFS, GBF, A1, A2

goal = Node([1, 2, 3, 8, 0, 4, 7, 6, 5])

easy = Node([1, 3, 4, 8, 6, 2, 7, 0, 5])
medium = Node([2, 8, 1, 0, 4, 3, 7, 6, 5])
hard = Node([5, 6, 7, 4, 0, 8, 3, 2, 1])

initialStates = [
    ["EASY", easy],
    ["MEDIUM", medium],
    ["HARD", hard]
]

for node in initialStates:
    print ("\n=== {0} BREADTH FIRST SEARCH ===".format(node[0]))
    BFS.search(node[1].state, goal)
    print ("\n=== {0} DEPTH FIRST SEARCH ===".format(node[0]))
    DFS.search(node[1].state, goal)
    print ("\n=== {0} GREEDY BEST-FIRST ===".format(node[0]))
    GBF.search(node[1].state, goal)
    print ("\n=== {0} A*1 ===".format(node[0]))
    A1.search(node[1].state, goal)
    print ("\n=== {0} A*2 ===".format(node[0]))
    A2.search(node[1].state, goal)