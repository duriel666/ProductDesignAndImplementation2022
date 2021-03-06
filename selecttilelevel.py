from tilegame import *

black = (0,  0,  0)
white = (180, 180, 180)

loading_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 50)
window = screen


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
