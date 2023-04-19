import pygame, sys, constants
from sudoku import Sudoku

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.set_sketched_value = 0

    def set_cell_value(self, value):
        self.value = int(input())

    def set_sketched_value(self, value):
        self.sketched_value = int(input())

    def draw(self, x, y):
        cell_font = pygame.font.Font(None, constants.CELL_FONT)
        cell_value_surf = cell_font.render(str(self.value), 0, constants.NUMBER_COLOR)
        cell_value_rect = cell_value_surf.get_rect(center=(x, y))
