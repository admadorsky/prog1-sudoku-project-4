# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/
import copy

import pygame, sys, constants
from sudoku import Sudoku
from cell import Cell
from sudokugenerator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells_list = []
        self.selected_cell_row = -1
        self.selected_cell_col = -1
        self.generated_sudoku = []
        self.solution = []

        def initialize_board():
            # N = 9
            # K = 40
            # create a sudoku board
            self.generated_sudoku = SudokuGenerator(constants.BOARD_ROWSCOLS)
            # copy the board with all values into solution list
            self.solution = copy.deepcopy(self.generated_sudoku.get_board())
            # remove cells to make a playable board
            self.generated_sudoku.remove_cells(difficulty)


            # print(generated_sudoku.get_board())  # for debugging purposes

            for i in range(constants.BOARD_ROWSCOLS):
                row = []
                for j in range(constants.BOARD_ROWSCOLS):
                    current_cell = Cell(self.generated_sudoku.get_board()[i][j], i, j, self.screen)
                    row.append(current_cell)
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
                        (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE, i * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH_THICK
                    )
                    # draw vertical lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (i * constants.SQUARE_SIZE, 0),
                        (i * constants.SQUARE_SIZE, constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH_THICK
                    )
                # draws thin lines for all other rows/cols
                else:
                    # draw horizontal lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (0, i * constants.SQUARE_SIZE),
                        (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE, i * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH
                    )
                    # draw vertical lines
                    pygame.draw.line(
                        self.screen,
                        constants.LINE_COLOR,
                        (i * constants.SQUARE_SIZE, 0),
                        (i * constants.SQUARE_SIZE, constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE),
                        constants.LINE_WIDTH
                    )

        draw_grid()
        for row, contents in enumerate(self.cells_list):
            for cell in self.cells_list[row]:
                cell.draw()

    def select(self, x, y):
        col, row = self.click(x, y)
        self.selected_cell_row = row
        self.selected_cell_col = col
        # Deselect all cells
        for row_count, contents in enumerate(self.cells_list):
            for index, cell in enumerate(self.cells_list[row_count]):
                self.cells_list[row_count][index].selected = False
        # Select clicked cell
        self.cells_list[row][col].selected = True

    def click(self, x, y):
        col = int((x // constants.SQUARE_SIZE) % constants.BOARD_ROWSCOLS)
        row = int((y // constants.SQUARE_SIZE) % constants.BOARD_ROWSCOLS)
        return col, row
    
    def clear(self):
        self.cells_list[self.selected_cell_row][self.selected_cell_col].value = 0      

    def sketch(self, value):
        sketched_cell = self.cells_list[self.selected_cell_row][self.selected_cell_col]
        if sketched_cell.value == 0:
            sketched_cell.set_sketched_value(value)

    def place_number(self, value):
        self.cells_list[self.selected_cell_row][self.selected_cell_col].value = value

    def reset_to_original(self):
        for i in range(len(self.cells_list[0])):
            for j in range(len(self.cells_list[0])):
                self.cells_list[i][j].value = self.solution[i][j]

    def is_full(self):
        for i in range(len(self.cells_list[0])):
            for j in range(len(self.cells_list[0])):
                if self.cells_list[i][j].value == 0:
                    return False              
        
        return True

    def update_board(self):
        Sudoku.printSudoku()

    def find_empty(self):
        for i in range(len(self.cells_list[0])):
            for j in range(len(self.cells_list[0])):
                if self.cells_list[i][j].value == 0:
                    return i, j

    def check_board(self):
        for row, list in enumerate(self.cells_list):
            for col, cell in enumerate(list):
                if cell != self.solution[col][row]:
                    # print(f"row: {row}, col: {col}, expected: {self.solution[col][row]}, found: {self.cells_list[col][row].value}")
                    return False
        return True

        # for i in range(len(self.cells_list[0])):
        #     for j in range(len(self.cells_list[0])):
        #         if self.cells_list[i][j] != self.solution[i][j]:
        #             return False
        # return True
