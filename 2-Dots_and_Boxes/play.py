# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# play.py

import sys
import os
import getopt

from box import Box
import game

args = sys.argv
args_len = len(sys.argv)
size = [0, 0]
player = ""

# Prints a help message along with an optional message
def printHelp(message=""):
    if (len(message) > 0):
        print(message)
    print("Please use the following format:\n" +
          "play.py -s <size | [x] [y]>\n"+
          "e.g. 'play.py -s 2 2'")
    os._exit(0)

# Prints help message if there are too many or too few arguments
if (args_len < 4 or args_len > 4):
    printHelp("Invalid number of arguments.")

# Loops through command line arguments and sets size
i = 1
while (i < args_len):        
    if (args[i] == '-s'):
        size[0] = int(args[i + 1])
        size[1] = int(args[i + 2])
    i += 1

print("Board size is {0} by {1}.".format(size[0], size[1]))

# Loops until user is satisfied with their inputted name
loop = True
while(loop):
    user_input = input("Please enter your name: ")
    player = user_input
    user_input = input("Your name is {0}. Is this correct?\n".format(player) + 
                           "(Y/n): ")
    if  (user_input.lower() == 'n' or user_input.lower() == 'no'):
        loop = True
    elif (user_input.lower() == 'y' or user_input.lower() == 'yes'):
        loop = False
    else:
        print("Unknown value: {0}.".format(user_input))

# Start game