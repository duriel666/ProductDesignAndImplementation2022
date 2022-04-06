import pygame
from pygame.locals import *
from world import *  # import world data from another file
from pygame import mixer
from enemy import Enemy  # import enemy from another file

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))  # screen setup
pygame.display.set_caption('THE GAME')  # name of the game screen
gameover = 0

bg_img = pygame.image.load('kansio/bg2.png')  # background image
mixer.music.load('kansio/tuner.wav')  # game music
mixer.music.play(-1)


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line *
                         tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line *
                         tile_size, 0), (line * tile_size, screen_height))


class Player():
    def __init__(self, x, y):
        img = pygame.image.load('kansio/player.png')
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self, gameover):  # gameover here to access the gameover variable
        dx = 0
        dy = 0

        if gameover == 0:

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0

            self.vel_y += 1  # gravity
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            for tile in world.tile_list:
                # checks that the player cannot go throught blocks
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

            if pygame.sprite.spritecollide(self, enemy_group, False):
                gameover = -1

            if pygame.sprite.spritecollide(self, saw_group, False):
                gameover = -1

            self.rect.x += dx  # player coordinates
            self.rect.y += dy

        elif gameover == -1:
            if self.rect.y > 200:
                self.rect.y -= 5

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return gameover


class World():
    def __init__(self, data):
        self.tile_list = []
        dirt_img = pygame.image.load('kansio/dirt.png')  # image load
        grass_img = pygame.image.load('kansio/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:  # checks all the rows and columns for 1s and 2s
                if tile == 1:
                    img = pygame.transform.scale(
                        dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                        grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    # +15 is for the enemy, it is sitting on top of the block(no floating)
                    enemmy = Enemy(col_count * tile_size,
                                   row_count * tile_size + 15)
                    enemy_group.add(enemmy)
                if tile == 4:
                    saw = Saw(col_count * tile_size, row_count *
                              tile_size + (tile_size//2))
                    saw_group.add(saw)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Saw(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('kansio/saw.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player = Player(100, screen_height - 130)

enemy_group = pygame.sprite.Group()
saw_group = pygame.sprite.Group()
world = World(world_data)

run = True
while run:

    clock.tick(fps)
    screen.blit(bg_img, (0, 0))

    world.draw()  # draw the world

    enemy_group.update()
    enemy_group.draw(screen)  # draw the enemies
    saw_group.draw(screen)  # draw the saw
    gameover = player.update(gameover)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
