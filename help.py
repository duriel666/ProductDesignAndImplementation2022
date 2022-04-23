from map import *

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


def gamehelp(run):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 575 and 285 <= mouse[1] <= 360:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((background))
        window.blit(menu_bg, (0, 0))
        mouse = pygame.mouse.get_pos()
        game_font.render_to(window, (197, 203), 'START', (shadow))
        game_font.render_to(window, (200, 200), 'START', (white3))
        if 175 <= mouse[0] <= 575 and 285 <= mouse[1] <= 360:
            rect_a(window, select, (175, 285, 400, 75))
            game_font.render_to(window, (197, 303), 'BACK', (shadow))
            game_font.render_to(window, (200, 300), 'BACK', (white2))
        else:
            game_font.render_to(window, (197, 303), 'BACK', (shadow))
            game_font.render_to(window, (200, 300), 'BACK', (white))
        game_font.render_to(window, (197, 403), 'QUIT', (shadow))
        game_font.render_to(window, (200, 400), 'QUIT', (white3))

        rect_a(window, select, (690, 185, 320, 135))
        game_font2.render_to(
            window, (708, 202), 'Map:', (shadow))
        game_font2.render_to(
            window, (708, 242), 'W, A, S, D  - to move', (shadow))
        game_font2.render_to(
            window, (708, 282), 'E  - to use', (shadow))
        game_font2.render_to(
            window, (710, 200), 'Map:', (white2))
        game_font2.render_to(
            window, (710, 240), 'W, A, S, D  - to move', (white2))
        game_font2.render_to(
            window, (710, 280), 'E  - to use', (white2))

        rect_a(window, select, (690, 385, 320, 175))
        game_font2.render_to(
            window, (708, 402), 'Level:', (shadow))
        game_font2.render_to(
            window, (708, 442), 'A, D  - to move', (shadow))
        game_font2.render_to(
            window, (708, 482), 'W  - to jump', (shadow))
        game_font2.render_to(
            window, (708, 522), 'E  - to use', (shadow))
        game_font2.render_to(
            window, (710, 400), 'Level:', (white2))
        game_font2.render_to(
            window, (710, 440), 'A, D  - to move', (white2))
        game_font2.render_to(
            window, (710, 480), 'W  - to jump', (white2))
        game_font2.render_to(
            window, (710, 520), 'E  - to use', (white2))
        pygame.display.update()
