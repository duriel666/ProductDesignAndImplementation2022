import pygame
from tiletile import Tile
from tilemap import tile_size
from tileplayer import *


class Enemy(pygame.sprite.Sprite):  # pygame sprite has a buildin draw method
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('gfx/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.moving_enemy = vec(0, 0)
        self.speed = 1
        self.moving_count = 0

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
        self.rect.x += self.moving_enemy.x
        self.rect.y += self.moving_enemy.y
        self.moving_count += 1
        if abs(self.moving_count) > 50:  # absolut value
            self.moving_enemy.x *= -1
            self.moving_enemy.y *= -1
            self.moving_count *= -1
