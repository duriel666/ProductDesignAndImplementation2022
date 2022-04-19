import pygame
from forestlevel import *
from beachlevel import *


def select_beach(score):
    pygame.mixer.music.load('sfx/beach-waves.wav')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game_beach(True, score)


def select_forest(score):
    pygame.mixer.music.load('sfx/forest-birds.wav')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.0)
    return start_game_forest(True, score)
