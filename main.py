# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/

from sudoku import Sudoku

# Driver code
if __name__ == "__main__":
    N = 9
    K = 40
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()

