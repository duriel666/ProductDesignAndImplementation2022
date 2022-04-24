from map import *
from help import *
from options import *

pygame.init()
pygame.font.init()

game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 60)
game_font2 = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 30)

black = (0,  0,  0)
white = (180, 180, 180)
white2 = (230, 230, 230)
select = (255, 255, 255, 50)
background = (50, 150, 50)
shadow = (10, 10, 10, 150)
shadow2 = (10, 10, 10, 150)

# window dimension defined in tilemap.py
ww = screen.get_width()
wh = screen.get_height()

menu_bg = pygame.image.load('gfx/menu-bg.png')
menu_bg = pygame.transform.scale(menu_bg, (ww, wh))


def rect_a(surface, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surface.blit(shape, rect)


def gamemenu(run):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return player.score
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 185 <= mouse[1] <= 260:
                    start_game(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 285 <= mouse[1] <= 360:
                    gamehelp(run)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 385 <= mouse[1] <= 460:
                    gameoptions(run)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 485 <= mouse[1] <= 560:
                    run = False
                    return player.score
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((background))
        window.blit(menu_bg, (0, 0))
        mouse = pygame.mouse.get_pos()

        if 175 <= mouse[0] <= 575 and 185 <= mouse[1] <= 260:
            rect_a(window, select, (175, 185, 400, 75))
            game_font.render_to(window, (197, 203), 'START', (shadow2))
            game_font.render_to(window, (200, 200), 'START', (white2))
        else:
            game_font.render_to(window, (197, 203), 'START', (shadow))
            game_font.render_to(window, (200, 200), 'START', (white))

        if 175 <= mouse[0] <= 575 and 285 <= mouse[1] <= 360:
            rect_a(window, select, (175, 285, 400, 75))
            game_font.render_to(window, (197, 303), 'HELP', (shadow2))
            game_font.render_to(window, (200, 300), 'HELP', (white2))
        else:
            game_font.render_to(window, (197, 303), 'HELP', (shadow))
            game_font.render_to(window, (200, 300), 'HELP', (white))

        if 175 <= mouse[0] <= 575 and 385 <= mouse[1] <= 460:
            rect_a(window, select, (175, 385, 400, 75))
            game_font.render_to(window, (197, 403), 'OPTIONS', (shadow2))
            game_font.render_to(window, (200, 400), 'OPTIONS', (white2))
        else:
            game_font.render_to(window, (197, 403), 'OPTIONS', (shadow))
            game_font.render_to(window, (200, 400), 'OPTIONS', (white))

        if 175 <= mouse[0] <= 575 and 485 <= mouse[1] <= 560:
            rect_a(window, select, (175, 485, 400, 75))
            game_font.render_to(window, (197, 503), 'QUIT', (shadow2))
            game_font.render_to(window, (200, 500), 'QUIT', (white2))
        else:
            game_font.render_to(window, (197, 503), 'QUIT', (shadow))
            game_font.render_to(window, (200, 500), 'QUIT', (white))

        pygame.display.update()
