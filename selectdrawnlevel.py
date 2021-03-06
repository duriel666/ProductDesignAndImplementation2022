from forestlevel import *
from beachlevel import *
from magicallevel import *

black = (0,  0,  0)
white = (180, 180, 180)

loading_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 50)
loading = 'Loading...'


def load_screen():
    window.fill(black)
    loading_font.render_to(
        window, (ww-270, wh-60), loading, (white))
    pygame.display.flip()


def fade_to_black():
    # fade to and from black for loading screen
    x = 0


def select_beach(score):
    load_screen()
    # background audio for the level
    pygame.mixer.music.load('sfx/beach-waves.wav')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game_beach(True, score)


def select_forest(score):
    load_screen()
    pygame.mixer.music.load('sfx/forest-birds.wav')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game_forest(True, score)


def select_magical(score):
    load_screen()
    pygame.mixer.music.load('sfx/magical-chimes.wav')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game_magical(True, score)
