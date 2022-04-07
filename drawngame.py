import pygame
from pygame.locals import *
import sys
import time

pygame.init()
pygame.font.init()
vec = pygame.math.Vector2

ww = 900
wh = 600
fps = 240
acceleration = 0.08
friction = -0.04
black = (0,  0,  0)


class Alusta(pygame.sprite.Sprite):
    def __init__(self, alusta):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(alusta).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Eteen(pygame.sprite.Sprite):
    def __init__(self, eteen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(eteen).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Alusta_col(pygame.sprite.Sprite):
    def __init__(self, alusta_col):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(alusta_col).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image):
        super().__init__()
        self.image = pygame.image.load(player_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.pos = vec((500, 500))
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
                self.pos.y -= 1
                if(pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                    self.pos.y -= 1
                    self.acc.x = 0
                    self.pos.x += 1
        if pressed_keys[K_d]:
            self.acc.x = acceleration
            if (pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                self.pos.y -= 1
                if(pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                    self.pos.y -= 1
                    self.acc.x = 0
                    self.pos.x -= 1
        if self.acc.y < 0:
            if (pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)):
                self.pos.y += 1
                self.acc.y = 0

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + acceleration * self.acc

        if self.pos.x > ww:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = ww

        self.rect.midbottom = self.pos

    def jump(self):
        #hits=pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)
        if not self.jumping:
            self.jumping = True
            self.vel.y = -8

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


SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh), SURFACE)
pygame.display.set_caption("Drawn-testi 01")


alusta_col = Alusta_col('drawn-level-alpha-test.png')
alusta = Alusta('drawn-alusta.png')
player = Player('drawn-mario.png')
eteen = Eteen('drawn-eteen.png')

col_group = pygame.sprite.Group()
col_group.add(alusta_col)
sprite_group = pygame.sprite.Group()
sprite_group.add(alusta_col)
sprite_group.add(alusta)
sprite_group.add(player)
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
sprite_group.add(eteen)


clock = pygame.time.Clock()

run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.cancel_jump()
        if event.type == pygame.QUIT:
            run = False

    sprite_group.update()
    col_group.update()
    player.update()
    window.fill(black)
    sprite_group.draw(window)
    player.move()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()