# Ross Nelson CSC380 Assignment 1: Eight Puzzle
# January 26th, 2020
# puzzle.py

import sys
import os
import getopt

from node import Node
import BFS
import DFS
import GBF
import A1
import A2

goal = Node([1, 2, 3, 8, 0, 4, 7, 6, 5])

easy = ["EASY", Node([1, 3, 4, 8, 6, 2, 7, 0, 5])]
medium = ["MEDIUM", Node([2, 8, 1, 0, 4, 3, 7, 6, 5])]
hard = ["HARD", Node([5, 6, 7, 4, 0, 8, 3, 2, 1])]

args = sys.argv
args_len = len(sys.argv)
difficulty = [None]
search = "None"


def printHelp(message=""):
    if (len(message) > 0):
        print(message)
    print("Please use the following format:\n" +
          "puzzle.py -d <difficulty | [e]asy | [m]edium | [h]ard> " +
          "-s <search | bfs | dfs | gbf | a1 | a2>")
    os._exit(0)


if (args_len < 5 or args_len > 5):
    if (args[1] == '-h' or args[1] == '-help'):
        printHelp("Help:")
    printHelp("Invalid number of arguments.")

i = 1
while (i < args_len):
    if (args[i] == '-d'):
        if (args[i + 1].lower() == 'e' or args[i + 1].lower() == 'easy'):
            difficulty = easy
        elif (args[i + 1].lower() == 'm' or args[i + 1].lower() == 'medium'):
            difficulty = medium
        elif (args[i + 1].lower() == 'h' or args[i + 1].lower() == 'hard'):
            difficulty = hard
        else:
            printHelp("Invalid argument '{0}'.".format(args[i + 1]))
    elif (args[i] == '-s'):
        s = args[i + 1].upper()
        if (s == "BFS" or s == "DFS" or s == "GBF" or s == "A1" or s == "A2"):
            search = s
        else:
            printHelp("Invalid argument '{0}'.".format(s))
    i += 1

if (search == "BFS"):
    print("\n=== {0} BREADTH FIRST SEARCH ===".format(difficulty[0]))
    BFS.search(difficulty[1], goal)
elif (search == "DFS"):
    print("\n=== {0} DEPTH FIRST SEARCH ===".format(difficulty[0]))
    DFS.search(difficulty[1], goal)
elif (search == "GBF"):
    print("\n=== {0} GREEDY BEST-FIRST ===".format(difficulty[0]))
    GBF.search(difficulty[1], goal)
elif (search == "A1"):
    print("\n=== {0} A*1 ===".format(difficulty[0]))
    A1.search(difficulty[1], goal)
elif (search == "A2"):
    print("\n=== {0} A*2 ===".format(difficulty[0]))
    A2.search(difficulty[1], goal)
