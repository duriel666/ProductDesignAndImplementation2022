from tkinter import EventType
import pygame, sys
from tilemap import * 
from tilelevel import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    screen.fill('pink')
    level.run()
    pygame.display.update()
    clock.tick(60)
