import pygame
from tiletile import Tile
from tilemap import tile_size, screen_width
from tileplayer import *

class Enemy(pygame.sprite.Sprite): #pygame sprite has a buildin draw method
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
		
        self.image = pygame.image.load('gfx/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.moving_enemy = 1
        self.moving_count = 0

    def update(self, x_shift):
        self.rect.x += x_shift
        self.rect.x += self.moving_enemy
        self.moving_count += 1
        if abs(self.moving_count) > 50: #absolut value
            self.moving_enemy *= -1
            self.moving_count *= -1
                