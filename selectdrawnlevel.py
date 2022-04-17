import pygame
from forestlevel import *


def select_beach(score):
    pygame.mixer.music.load('sfx/beach-waves.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game(True, score)


def select_forest(score):
    pygame.mixer.music.load('sfx/forest-birds.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game(True, score)
