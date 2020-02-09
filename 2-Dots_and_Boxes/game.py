# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# game.py

import os
import re

from board import Board
from algorithm import minimax

user = ''
board = None


# Main loop which controls the game and returns when there has been a winner
def play(username, x, y, depth):
    global user
    global board
    user = username
    board = Board(x, y, user)

    printHelp('', False)
    userWon = False
    algWon = False
    while(not userWon and not algWon):
        board.prettyPrint()
        if (userTurn() == True):
            userWon = True
        else:
            board.prettyPrint()
            if (algTurn(depth) == True):
                algWon = True
    board.prettyPrint()
    if (userWon):
        print("Game Over, you win with a score of " +
              "{0}:{1} to A:{2}!".format(user[:1], board.uScore, board.aScore))
    else:
        print("Game Over. The final score was, " +
              "{0}:{1} to A:{2}. Good game!".format(user[:1], board.uScore, 
                                                    board.aScore))
    return


# Takes user input to determine the user's move and applies it.
def userTurn():
    user_input = input("It's your move, {0}.\n".format(user) +
                       "(Enter your move): ")
    if (user_input.lower() == 'h' or user_input.lower() == 'help'):
        return printHelp()
    elif (user_input.lower() == 'q' or user_input.lower() == 'quit'):
        print("Aww, I'm sorry to see you go, {0}. ".format(user) +
              "Thanks for playing, though!")
        os._exit(0)
    elif (re.match(r"[0-9],[0-9],[tblrTBLR]", user_input.replace(" ", ""))):
        move = user_input.upper().split(",")
        move[0] = int(move[0])
        move[1] = int(move[1])
        move[2] = move[2].strip()
        if (move[0] < 0 or move[0] > board.length - 1):
            printHelp("x position, '{0}' is out of range.".format(move[0]))
        elif (move[1] < 0 or move[1] > board.height - 1):
            printHelp("y position, '{0}' is out of range.".format(move[1]))
        else:
            update = board.updateBoard(move[0], move[1], move[2], user)
            if (update == "printHelp"):
                return printHelp("That line has already been drawn.\n" +
                                 "Choose another spot, {0}".format(user))
            else:
                return update
    else:
        printHelp("I'm sorry, I don't understand '{0}'.".format(user_input))
    return False



def algTurn(depth):
    print("I'll think I'll move here.")
    newBoardInfo = board.getInfo()
    newBoard = Board(newBoardInfo[0], newBoardInfo[1],newBoardInfo[2],
                     newBoardInfo[3], newBoardInfo[4], newBoardInfo[5],
                     newBoardInfo[6])
    move = minimax(newBoard, depth)[1]
    print("move: {0}".format(move))
    update = board.updateBoard(move[0], move[1], move[2], "Algie")
    return update


# Prints a help message and an optional message.
# Also optionally calls userTurn() and returns its output.
def printHelp(message='', getUserInput=True):
    if (message != ''):
        print("{0}\n".format(message))
    print("To enter a move, use the following format: 'x, y, D'\n" +
          "x and y are the coordinates of the box you want to select, \n" +
          "and D is the first letter of the direction you want to fill.\n" +
          "e.g. '0, 0, T' will fill in the TOP side of the box in the top\n" +
          "left corner.\n" +
          "All possible directions are: [T]op, [B]ottom, [L]eft, [R]ight\n" +
          "\nPlease enter 'help' at any time to see this message again.\n")
    if (getUserInput):
        board.prettyPrint()
        return userTurn()
    return
