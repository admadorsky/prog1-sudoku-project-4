# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/

import pygame, sys, constants
from sudoku import Sudoku

class Cell:
    def __init__(self, value, row, col, screen):

        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.set_sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = int(input())

    def set_sketched_value(self, value):
        self.sketched_value = int(input())

    def draw(self):
        cell_font = pygame.font.Font(None, constants.CELL_FONT)

        # empty any cells containing 0
        if self.value == 0:
            printed_value = ""
        else:
            printed_value = self.value

        # initialize each cell's surface and rectangle objects
        cell_value_surf = cell_font.render(str(printed_value), 0, constants.NUMBER_COLOR)
        cell_value_rect = cell_value_surf.get_rect(center=((self.row * constants.SQUARE_SIZE) + (constants.SQUARE_SIZE // 2),
                                                           (self.col * constants.SQUARE_SIZE) + (constants.SQUARE_SIZE // 2)))
        # draw the cell
        self.screen.blit(cell_value_surf, cell_value_rect)

        def draw_outline():
            # draw top outline
            pygame.draw.line(
                self.screen,
                constants.SELECTED_COLOR,
                ((self.row * constants.SQUARE_SIZE), (self.col * constants.SQUARE_SIZE)),
                (((self.row + 1) * constants.SQUARE_SIZE), ((self.col) * constants.SQUARE_SIZE)),
                constants.LINE_WIDTH_THICK
            )
            # draw bottom outline
            pygame.draw.line(
                self.screen,
                constants.SELECTED_COLOR,
                ((self.row * constants.SQUARE_SIZE), ((self.col + 1) * constants.SQUARE_SIZE)),
                (((self.row + 1) * constants.SQUARE_SIZE), ((self.col + 1) * constants.SQUARE_SIZE)),
                constants.LINE_WIDTH_THICK
            )
            # draw right outline
            pygame.draw.line(
                self.screen,
                constants.SELECTED_COLOR,
                (((self.row + 1) * constants.SQUARE_SIZE), (self.col * constants.SQUARE_SIZE)),
                (((self.row + 1) * constants.SQUARE_SIZE), ((self.col + 1) * constants.SQUARE_SIZE)),
                constants.LINE_WIDTH_THICK
            )
            # draw left outline
            pygame.draw.line(
                self.screen,
                constants.SELECTED_COLOR,
                ((self.row * constants.SQUARE_SIZE), ((self.col) * constants.SQUARE_SIZE)),
                (((self.row) * constants.SQUARE_SIZE), ((self.col + 1) * constants.SQUARE_SIZE)),
                constants.LINE_WIDTH_THICK
            )

        # outline selection
        if self.selected == True:
            draw_outline()

