import pygame
from forestlevel import *


def select_forest(score):
    pygame.mixer.music.load('audio/forest-birds.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.0)
    return start_game(True, score)
