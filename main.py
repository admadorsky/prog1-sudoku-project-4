# Project 4: Sudoku by Anthony Madorsky, Muhammad Ali, Alexander Hennecke, and Joshua Park.
# Sudoku board generating code adapted from a GeeksforGeeks article "Program for Sudoku Generator"
# by Aarti_Rathi and Ankur Trisal https://www.geeksforgeeks.org/program-sudoku-generator/

from sudoku import Sudoku
from cell import Cell
from board import Board
from sudokugenerator import SudokuGenerator
import pygame, sys, constants

# driver code
if __name__ == "__main__":

    # initialize variables for a sudoku board
    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT + 50))
    pygame.display.set_caption("Sudoku")
    game_over_font = pygame.font.Font(None, constants.GAME_OVER_FONT)
    game_over = False
    sudoku_generator = SudokuGenerator(constants.BOARD_ROWSCOLS)

    def main_menu():
        screen.fill(constants.BG_COLOR)
        # text   
        welcome = pygame.font.Font('freesansbold.ttf', 32).render('Welcome to Sudoku', True, 'black')
        screen.blit(welcome, (65, 100))
        difficulty_selection = pygame.font.Font('freesansbold.ttf', 26).render('Select Game Mode:', True, 'black')
        screen.blit(difficulty_selection, (100, 230))

        # easy button
        pygame.draw.rect(screen, 'orange', [65, 300, 70, 40])
        easy = pygame.font.Font('freesansbold.ttf', 18).render('EASY', True, 'white')
        screen.blit(easy, (75, 310))

        # medium button
        pygame.draw.rect(screen, 'orange', [185, 300, 70, 40])
        medium = pygame.font.Font('freesansbold.ttf', 17).render('MEDIUM', True, 'white')
        screen.blit(medium, (185, 310))

        # hard button
        easy_button = pygame.draw.rect(screen, 'orange', [305, 300, 70, 40])
        hard = pygame.font.Font('freesansbold.ttf', 18).render('HARD', True, 'white')
        screen.blit(hard, (315, 310))

    def in_progress_menu():
        # reset button
        pygame.draw.rect(screen, 'orange', [65, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5), 80, 40])
        reset = pygame.font.Font('freesansbold.ttf', 18).render('RESET', True, 'white')
        screen.blit(reset, (75, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE) + 15))

        # restart button
        pygame.draw.rect(screen, 'orange', [175, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5), 100, 40])
        restart = pygame.font.Font('freesansbold.ttf', 18).render('RESTART', True, 'white')
        screen.blit(restart, (185, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE) + 15))

        # exit button
        pygame.draw.rect(screen, 'orange', [305, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5), 70, 40])
        restart = pygame.font.Font('freesansbold.ttf', 18).render('EXIT', True, 'white')
        screen.blit(restart, (315, (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE) + 15))

    def click_selection():
        global x, y
        x, y = event.pos
        if x <= constants.WIDTH and y <= constants.HEIGHT:
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

    def sketch_value():
        digits = [pygame.K_1,
                  pygame.K_2,
                  pygame.K_3,
                  pygame.K_4,
                  pygame.K_5,
                  pygame.K_6,
                  pygame.K_7,
                  pygame.K_8,
                  pygame.K_9]

        for index, digit in enumerate(digits):
            value = index + 1
            if event.key == digit:
                board.sketch(value)
                board.draw()

    def fill_value():
        if event.key == pygame.K_RETURN:
            selected_cell = board.cells_list[board.selected_cell_row][board.selected_cell_col]
            sketched_value = selected_cell.sketched_value
            if sketched_value != 0:
                selected_cell.set_cell_value(sketched_value)
                board.draw()

    def evaluate_board():
        for i in range(constants.BOARD_ROWSCOLS):
            for j in range(constants.BOARD_ROWSCOLS):
                num = board.cells_list[i][j].value
                if board.check_board():
                    return True
                if SudokuGenerator(constants.BOARD_ROWSCOLS).is_valid(i, j, num):
                    return True

    def draw_game_over():
        screen.fill(constants.BG_COLOR)

        end_text = 'Game Over!'
        end_surf = game_over_font.render(end_text, True, constants.LINE_COLOR)
        end_rect = end_surf.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
        screen.blit(end_surf, end_rect)

    while True:

        game_running = False
        menu_running = True

        while menu_running:
            main_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if (pygame.mouse.get_pos()[0] >= 65 and pygame.mouse.get_pos()[0] <= 135) and (
                            pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                        difficulty = 30
                        # print("easy")
                        menu_running = False
                        game_running = True
                    elif (pygame.mouse.get_pos()[0] >= 185 and pygame.mouse.get_pos()[0] <= 255) and (
                            pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                        difficulty = 40
                        # print("medium")
                        menu_running = False
                        game_running = True
                    elif (pygame.mouse.get_pos()[0] >= 305 and pygame.mouse.get_pos()[0] <= 375) and (
                            pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                        difficulty = 50
                        # print("hard")
                        menu_running = False
                        game_running = True

        # create a sudoku board object
        board = Board(constants.WIDTH, constants.HEIGHT, screen, difficulty)

        # select the center cell by default
        x, y = 4 * constants.SQUARE_SIZE, 4 * constants.SQUARE_SIZE

        board.draw()
        pygame.display.update()

        # runtime loop
        while game_running:

            in_progress_menu()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # detect mouse click
                if event.type == pygame.MOUSEBUTTONUP:
                    click_selection()
                    in_progress_menu()

                    # reset button
                    if (
                            pygame.mouse.get_pos()[0] >= 65 and
                            pygame.mouse.get_pos()[0] <= 135 and
                            pygame.mouse.get_pos()[1] >= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5) and
                            pygame.mouse.get_pos()[1] <= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 45)
                    ):
                        for row, list in enumerate(board.cells_list):
                            for col, cell in enumerate(board.cells_list[row]):
                                if board.cells_list[row][col].sketched_value != 0:
                                    board.cells_list[row][col].sketched_value = 0
                                    board.cells_list[row][col].value = 0
                        board.draw()
                        in_progress_menu()
                        print("reset")

                    # restart button
                    if (
                            pygame.mouse.get_pos()[0] >= 175 and
                            pygame.mouse.get_pos()[0] <= 275 and
                            pygame.mouse.get_pos()[1] >= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5) and
                            pygame.mouse.get_pos()[1] <= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 45)
                    ):
                        menu_running = True
                        print("restart")
                        game_running = False

                    # exit button
                    if (
                            pygame.mouse.get_pos()[0] >= 305 and
                            pygame.mouse.get_pos()[0] <= 375 and
                            pygame.mouse.get_pos()[1] >= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 5) and
                            pygame.mouse.get_pos()[1] <= (constants.BOARD_ROWSCOLS * constants.SQUARE_SIZE + 45)
                    ):
                        print("exit")
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    arrowkey_selection()
                    sketch_value()
                    in_progress_menu()
                    if event.key == pygame.K_RETURN:
                        fill_value()
                        in_progress_menu()

                if game_over == True:
                    pygame.display.update()
                    pygame.time.delay(1000)
                    draw_game_over()

                if board.is_full():
                    # evaluates whether board is solved correctly
                    board.check_board()
                    game_over = True
                    game_running = False

                pygame.display.update()


