# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# game.py

from board import Board


# Main loop which controls the game and returns when there has been a winner
def play(user, x, y):
    board = Board(x, y)
    printHelp(user, False)
    winner = False
    while(winner == False):
        board.prettyPrint()
        winner = userTurn(user)
        board.prettyPrint()
        winner = algTurn(user)
    print("Game Over")
    return


# Takes user input to determine the user's move and applies it.
def userTurn(user):
    user_input = input("It's your move, {0}.\n".format(user) +
                       "(Enter your move): ")
    print(user_input)
    if (user_input.lower == 'h' or user_input.lower == 'help'):
        user_input = printHelp(user)
    elif (user_input.lower == 'q' or user_input.lower == 'quit'):
        print("Aww, I'm sorry to see you go, {0}. " +
              "Thanks for playing, though!".format(user))
        return True
    return False


def algTurn(user):
    print("I'll think I'll move here.")
    return False


# Prints a help message
def printHelp(user, getUserInput=True):
    print("To enter a move, use the following format:\n" +
          "'x, y, [D]irection' x and y are the coordinates of the box you " +
          "want to select, and D is the first letter of the direction you " +
          "want to fill.\n" +
          "e.g. '0, 0, T' will fill in the top of the box in position (0, 0).\n"
          "\n Please enter 'help' at any time to see this message again.")
    if (getUserInput):
        user_input = input("It's your move, {0}.\n".format(user) +
                           "(Enter your move): ")
        return user_input
    return
