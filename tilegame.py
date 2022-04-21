import pygame
from pygame.locals import *
import sys
from pygame import mixer
from tilemap import *
from tilelevel import *

pygame.init()

screen = pygame.display.set_mode((ww, wh))
clock = pygame.time.Clock()
level = Level(level_map, screen)
score = 0


def start_game(run, score):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return score

        screen.fill('pink')
        level.run()
        pygame.display.update()
        clock.tick(60)
# start_game(True,0)
