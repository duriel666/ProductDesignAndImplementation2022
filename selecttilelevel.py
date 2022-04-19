import pygame
from pygame.locals import *
from tilegame import *

ww = screen.get_width()
wh = screen.get_height()

black = (0,  0,  0)
white = (180, 180, 180)

loading_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 50)

window = pygame.display.set_mode((ww, wh))


def load_screen():
    window.fill(black)
    loading_font.render_to(window, (ww-270, wh-60), 'Loading...', (white))
    pygame.display.flip()


def select_beach_tile(score):
    load_screen()
    return start_game(True, score)


def select_forest_tile(score):
    load_screen()
    return start_game(True, score)
