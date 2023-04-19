import pygame, sys, constants
from sudoku import Sudoku
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):cells_list = []

        def initialize_board():
            N = 9
            K = 40
            sudoku = Sudoku(N, K)
            sudoku.fillValues()

            for i in range(N):
                for j in range(N):
                    current_cell = Cell(sudoku[i][j], i, j, self.screen)
                    global cells_list
                    cells_list.append(current_cell)

        def draw_grid():
            self.screen.fill(constants.BG_COLOR)
            for i in range(1, constants.BOARD_ROWSCOLS):
                # draws thick lines for every third row/col
                if i % 3 == 0:
                    # draw horizontal lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (0, i * constants.SQUARE_SIZE),
                        (self.width, i * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH_THICK
                    )
                    # draw vertical lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (i * constants.SQUARE_SIZE, 0),
                        (i * constants.SQUARE_SIZE, self.height),
                        constants.LINE_WIDTH_THICK
                    )
                # draws thin lines for all other rows/cols
                else:
                    # draw horizontal lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (0, i * constants.SQUARE_SIZE),
                        (self.width, i * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH
                    )
                    # draw vertical lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (i * constants.SQUARE_SIZE, 0),
                        (i * constants.SQUARE_SIZE, self.height),
                        constants.LINE_WIDTH
                    )

        initialize_board()
        draw_grid()

