# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/

from sudoku import Sudoku
from cell import Cell
from board import Board
import pygame, sys, constants

# driver code
if __name__ == "__main__":

    # initialize variables for a sudoku board

    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Sudoku")

    # create a sudoku board object
    board = Board(constants.WIDTH, constants.HEIGHT, screen, 0)

    board.draw()
    pygame.display.update()

    # runtime loop
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                board.select(x, y)
                board.draw()

            pygame.display.update()