import pygame
from pygame.locals import *
from map import *
import sys

pygame.init()
pygame.font.init()

game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 60)

res = (720, 720)


black = (0,  0,  0)
white = (200, 200, 200)
grey = (50, 50, 50)
ww = screen.get_width()
wh = screen.get_height()
text = game_font.render('quit', True, grey)


def gamemenu(run):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ww/2-625 <= mouse[0] <= ww/2-325 and wh/2-265 <= mouse[1] <= wh/2-190:
                    start_game(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ww/2-625 <= mouse[0] <= ww/2-325 and wh/2-165 <= mouse[1] <= wh/2-90:
                    pygame.quit()
                    run = False
        screen.fill((black))
        mouse = pygame.mouse.get_pos()
        if ww/2-625 <= mouse[0] <= ww/2-325 and wh/2-265 <= mouse[1] <= wh/2-190:
            pygame.draw.rect(screen, grey, [ww/2-625, wh/2-265, 300, 75])
        if ww/2-625 <= mouse[0] <= ww/2-325 and wh/2-165 <= mouse[1] <= wh/2-90:
            pygame.draw.rect(screen, grey, [ww/2-625, wh/2-165, 300, 75])
        game_font.render_to(window, (ww/2-600, wh/2-250), 'START', (white))
        game_font.render_to(window, (ww/2-600, wh/2-150), 'QUIT', (white))
        pygame.display.update()
