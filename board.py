import pygame, sys, constants

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        # fill the window with white
        self.screen.fill(constants.BG_COLOR)
        def draw_grid():
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

