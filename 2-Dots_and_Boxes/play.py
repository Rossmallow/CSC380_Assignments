# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# play.py

import sys
import os

from game import play

args = sys.argv
args_len = len(sys.argv)


# Prints a help message along with an optional message
def printHelp(message=""):
    if (len(message) > 0):
        print(message)
    print("Please use the following format:\n" +
          "play.py -s <size | [x] [y]> -d <depth | [1-9]>\n" +
          "e.g. 'play.py -s 2 2 -d 2'")
    os._exit(0)

# Checks if the command line arguments are valid


def checkArgs(size=[None, None]):
    # Prints help message if there are too many or too few arguments
    if (args_len < 6 or args_len > 6):
        printHelp("Invalid number of arguments.")

    # Loops through command line arguments and sets size
    for i in range(args_len):
        if (args[i] == '-s'):
            try:
                size[0] = int(args[i + 1])
                size[1] = int(args[i + 2])
            except ValueError:
                printHelp("Invalid input. " +
                          "'{0}' or '{1}' is not a number.".format(args[i + 1],
                                                                   args[i + 2]))
        if (args[i] == '-d'):
            try:
                depth = int(args[i + 1])
            except ValueError:
                printHelp("Invalid input. " +
                          "'{0}' is not a number.".format(args[i + 1]))
    print("Board size is {0} by {1}.\n".format(size[0], size[1]) +
          "Minimax depth is {0}.\n".format(depth))
    return size, depth


# Loops until user is satisfied with their inputted name
def setName():
    loop = True
    print("Hi, I'm Algernon Rhythm, but you can call me Algie!")
    while(loop):
        user_input = input("What's your name?\n" +
                           "(Enter your name): ")
        player = user_input
        user_input = input("Is your name {0}? ".format(player) +
                           "Did I get that right?\n" +
                           "(Y/n): ")
        if (user_input.lower() == 'y' or user_input.lower() == 'yes'):
            loop = False
        elif (user_input.lower() == 'n' or user_input.lower() == 'no'):
            loop = True
        else: # user_input isn't 'y', 'yes', 'n', or 'no'
            print("I'm sorry, I don't understand '{0}'.".format(user_input))

    print("\nIt's nice to meet you, {0}! ".format(player) +
          "Let's play Dots and Boxes!\n")
    return player


# Loops until the player doesn't want to play anymore
def playGame(player, size, depth):
    loop = True
    while(loop):
        play(player, size[0], size[1], depth)
        user_input = input("That was fun {0}! ".format(player) +
                           "Do you want to play again?\n"
                           + "(Y/n): ")
        if (user_input.lower() == 'y' or user_input.lower() == 'yes'):
            print("Let's play!")
            loop = True
        elif (user_input.lower() == 'n' or user_input.lower() == 'no'):
            loop = False
        else: # user_input isn't 'y', 'yes', 'n', or 'no'
            print("I'm sorry, I don't understand '{0}'.".format(user_input))

    print("Thanks for playing with me, {0}. See you later!".format(player))


# Call functions
size, depth = checkArgs()
player = setName()
playGame(player, size, depth)
os._exit(0)
