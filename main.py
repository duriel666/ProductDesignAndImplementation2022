import pygame
import time
from menu import *

pygame.init()

pygame.display.set_caption("Game - 0.2")

ww = 1600  # window width
wh = 900  # window height

black = (0,  0,  0)
white = (255, 255, 255)

time_start = time.time()

if __name__ == "__main__":
    gamemenu(True)
