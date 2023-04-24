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
    game_over_font = pygame.font.Font(None, constants.GAME_OVER_FONT)

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

    menu_running = True    
    while menu_running:
        main_menu()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if (pygame.mouse.get_pos()[0] >= 65 and pygame.mouse.get_pos()[0] <= 135) and (pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                    difficulty = 30
                    print("easy")
                    menu_running = False
                elif (pygame.mouse.get_pos()[0] >= 185 and pygame.mouse.get_pos()[0] <= 255) and (pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                    difficulty = 40
                    print("medium")
                    menu_running = False
                elif (pygame.mouse.get_pos()[0] >= 305 and pygame.mouse.get_pos()[0] <= 375) and (pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 340):
                    difficulty = 50
                    print("hard")
                    menu_running = False
    
    
    # create a sudoku board object
    board = Board(constants.WIDTH, constants.HEIGHT, screen, difficulty)

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

    def draw_game_over():
        screen.fill(constants.BG_COLOR)

        end_text = 'Game Over!'
        end_surf = game_over_font.render(end_text, True, constants.LINE_COLOR)
        end_rect = end_surf.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
        screen.blit(end_surf, end_rect)

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

            if game_over:
                pygame.display.update()
                pygame.time.delay(1000)
                draw_game_over()

            pygame.display.update()
