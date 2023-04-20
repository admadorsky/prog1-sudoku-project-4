import pygame, sys, constants
from sudoku import Sudoku
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells_list = []
        self.selected_cell_row = -1
        self.selected_cell_col = -1

        def initialize_board():
            N = 9
            K = 40
            sudoku = Sudoku(N, K)
            sudoku.fillValues()

            for i in range(N):
                row = []
                for j in range(N):
                    current_cell = Cell(sudoku.mat[i][j], i, j, self.screen)
                    row.append(current_cell)
                    # global cells_list
                self.cells_list.append(row)
        initialize_board()

    def draw(self):

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

        draw_grid()
        for row, contents in enumerate(self.cells_list):
            for cell in self.cells_list[row]:
                cell.draw()

    def select(self, x, y):
        row, col = self.click(x, y)
        self.selected_cell_row = row
        self.selected_cell_col = col
        # Deselct all cells
        for row_count, contents in enumerate(self.cells_list):
            for index, cell in enumerate(self.cells_list[row_count]):
                self.cells_list[row_count][index].selected = False
        # Select clicked cell
        self.cells_list[row][col].selected = True

    def click(self, x, y):
        row = x // constants.SQUARE_SIZE
        col = y // constants.SQUARE_SIZE
        return row, col
