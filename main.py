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

    # select the center cell by default
    x, y = 4 * constants.SQUARE_SIZE, 4 * constants.SQUARE_SIZE

    board.draw()
    pygame.display.update()

    def click_selection():
        global x, y
        x, y = event.pos
        board.select(x, y)
        board.draw()

    def arrowkey_selection():
        global x, y
        if event.key == pygame.K_LEFT:
            x -= constants.SQUARE_SIZE
            board.select(x, y)
            board.draw()
        if event.key == pygame.K_RIGHT:
            x += constants.SQUARE_SIZE
            board.select(x, y)
            board.draw()
        if event.key == pygame.K_UP:
            y -= constants.SQUARE_SIZE
            board.select(x, y)
            board.draw()
        if event.key == pygame.K_DOWN:
            y += constants.SQUARE_SIZE
            board.select(x, y)
            board.draw()

    digits = [pygame.K_1,
              pygame.K_2,
              pygame.K_3,
              pygame.K_4,
              pygame.K_5,
              pygame.K_6,
              pygame.K_7,
              pygame.K_8,
              pygame.K_9]

    def sketch_value():
        for index, digit in enumerate(digits):
            value = index + 1
            if event.type == digit:
                board.sketch(index + 1)

    # runtime loop
    while True:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # detect mouse click to select a cell
            if event.type == pygame.MOUSEBUTTONUP:
                click_selection()

            if event.type == pygame.KEYDOWN:
                arrowkey_selection()

            pygame.display.update()