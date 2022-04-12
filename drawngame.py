import pygame
from pygame.locals import *
import sys
import time

pygame.init()
pygame.font.init()
vec = pygame.math.Vector2

#ww = 1504
#wh = 846
ww = 1600
wh = 900
gw = 4961 #game width
gh = 3508
fps = 120
acceleration = 0.2
friction = -0.04
black = (0,  0,  0)


class World(pygame.sprite.Sprite):
    def __init__(self, world_image):
        super().__init__()
        self.image = pygame.image.load(world_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec((0, 0))
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image):
        super().__init__()
        self.image = pygame.transform.scale2x(
            pygame.image.load(player_image).convert_alpha())
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec((ww/2, wh/2))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0, acceleration)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.acc.x = -acceleration
            if (pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                self.vel.y -= 1
        if pressed_keys[K_d]:
            self.acc.x = acceleration
            if (pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                self.vel.y -= 1
        if self.acc.y < 0:
            if (pygame.sprite.spritecollide(self.overlap(), col_group, False, collided=pygame.sprite.collide_mask)) and (pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                self.vel.y -= -1

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + acceleration * self.acc

        self.rect.midbottom = self.pos

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self):
        hits = pygame.sprite.spritecollide(
            self, col_group, False, collided=pygame.sprite.collide_mask)
        if self.vel.y > 0:
            if hits:
                self.pos.y -= 1
                self.vel.y = 0
                self.jumping = False


#SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh))
pygame.display.set_caption("Drawn-testi 01")

player = Player('drawn-mario.png')
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

#collision = World('drawn-level-alpha-test.png')
collision = World('drawn-level-alpha-test-2.png')
#taakse = World('drawn-alusta.png')
taakse = World('drawn-level-alpha-test-2.png')
eteen = World('drawn-eteen.png')

col_group = pygame.sprite.Group()
col_group.add(collision)
sprite_group = pygame.sprite.Group()
# sprite_group.add(collision)
sprite_group.add(taakse)
sprite_group.add(eteen)
world_list = [eteen, taakse, collision]

clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.cancel_jump()
        if event.type == pygame.QUIT:
            run = False

    speed_x = player.vel.x
    speed_y = player.vel.y
    if player.pos.x < ww/4 and player.vel.x < 0 and collision.pos.x<0:
        for world in world_list:
            world.scroll_x(-(speed_x))
        player.vel.x = 0
        player.pos.x -= speed_x
    elif player.pos.x > ww-(ww/4) and player.vel.x > 0 and collision.pos.x>(-gh+ww):
        for world in world_list:
            world.scroll_x(-(speed_x))
        player.vel.x = 0
        player.pos.x -= speed_x
    if player.pos.y < wh/3 and player.vel.y < 0 and collision.pos.y<0:
        for world in world_list:
            world.scroll_y(-(speed_y))
        player.vel.y = 0
        player.pos.y -= speed_y
    elif player.pos.y > wh-(wh/3) and player.vel.y > 0 and collision.pos.y>(-gw+wh):
        for world in world_list:
            world.scroll_y(-(speed_y))
        player.vel.y = 0
        player.pos.y -= speed_y
    else:
        for world in world_list:
            world.scroll_x(0)
            world.scroll_y(0)
        player.vel.x = speed_x
        player.vel.y = speed_y
    player.vel.x = speed_x
    player.vel.y = speed_y

    sprite_group.update()
    col_group.update()
    player_group.update()
    player.update()
    window.fill(black)
    sprite_group.draw(window)
    player_group.draw(window)
    player.move()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
