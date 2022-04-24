from map import *
from tilemap import *

pygame.init()
pygame.font.init()

game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 60)
game_font2 = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 30)

black = (0,  0,  0)
white = (180, 180, 180)
white2 = (230, 230, 230)
white3 = (100, 100, 100)
select = (255, 255, 255, 100)
background = (50, 150, 50)
shadow = (10, 10, 10, 150)
ww = screen.get_width()
wh = screen.get_height()

menu_bg = pygame.image.load('gfx/menu-bg.png')
menu_bg = pygame.transform.scale(menu_bg, (ww, wh))


def rect_a(surface, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surface.blit(shape, rect)

# resolution change not working


def gameoptions(run):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 700 <= mouse[0] <= 1000 and 240 <= mouse[1] <= 285:
                    game_res.set_resolution_x(1280)
                    game_res.set_resolution_y(720)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 700 <= mouse[0] <= 1000 and 290 <= mouse[1] <= 335:
                    game_res.set_resolution_x(1600)
                    game_res.set_resolution_y(900)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 385 <= mouse[1] <= 460:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((background))
        window.blit(menu_bg, (0, 0))
        mouse = pygame.mouse.get_pos()
        game_font.render_to(window, (197, 203), 'START', (shadow))
        game_font.render_to(window, (200, 200), 'START', (white3))
        game_font.render_to(window, (197, 303), 'HELP', (shadow))
        game_font.render_to(window, (200, 300), 'HELP', (white3))
        if 175 <= mouse[0] <= 575 and 385 <= mouse[1] <= 460:
            rect_a(window, select, (175, 385, 400, 75))
            game_font.render_to(window, (197, 403), 'BACK', (shadow))
            game_font.render_to(window, (200, 400), 'BACK', (white2))
        else:
            game_font.render_to(window, (197, 403), 'BACK', (shadow))
            game_font.render_to(window, (200, 400), 'BACK', (white))
        game_font.render_to(window, (197, 503), 'QUIT', (shadow))
        game_font.render_to(window, (200, 500), 'QUIT', (white3))

        if 700 <= mouse[0] <= 1000 and 240 <= mouse[1] <= 285:
            rect_a(window, select, (690, 240, 320, 45))
        if 700 <= mouse[0] <= 1000 and 290 <= mouse[1] <= 335:
            rect_a(window, select, (690, 290, 320, 45))
        game_font2.render_to(
            window, (708, 202), 'Resolution:', (shadow))
        game_font2.render_to(
            window, (708, 252), '1280 x 720', (shadow))
        game_font2.render_to(
            window, (708, 302), '1600 x 900', (shadow))
        game_font2.render_to(
            window, (710, 200), 'Resolution:', (white2))
        game_font2.render_to(
            window, (710, 250), '1280 x 720', (white2))
        game_font2.render_to(
            window, (710, 300), '1600 x 900', (white2))

        pygame.display.update()
