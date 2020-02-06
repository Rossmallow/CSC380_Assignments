# Ross Nelson CSC380 Assignment 2: Dots and Boxes
# February 9th, 2020
# game.py

from board import Board


def play (user, x, y):
    board = Board(x, y)
    board.prettyPrint()
    print("Game Over")
    return
