# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/

from sudoku import Sudoku, math

# create the SudokuGenerator class here
class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        # row_length and removed_cells are equivalent to N and K; replaceable
        self.row_length = row_length
        self.removed_cells = removed_cells

        self.sudoku = Sudoku(row_length, removed_cells)

        # self.board = self.mat (below)
        # self.board = [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.sudoku.mat

    def valid_in_row(self, row, num):
        return self.sudoku.unUsedInRow(row, num)

    def valid_in_col(self, col, num):
        return self.sudoku.unUsedInCol(col, num)
        # return num not in [self.board[i][col] for i in range(self.N)]

    def valid_in_box(self, row_start, col_start, num):
        return self.sudoku.unUsedInBox(row_start, col_start, num)

    def is_valid(self, row, col, num):
        return self.sudoku.checkIfSafe(row, col, num)
        # uses checkIfSafe function instead

    def fill_values(self):
        return self.sudoku.fillValues()
