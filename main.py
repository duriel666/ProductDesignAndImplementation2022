import pygame
import time
from menu import *

pygame.init()

ww = 1600
wh = 900
fps = 120
acceleration = 0.2
friction = -0.04
black = (0,  0,  0)

time_start = time.time()

SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh), SURFACE)
pygame.display.set_caption("Drawn-testi 01")

if __name__ == "__main__":
    gamemenu()
