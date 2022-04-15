import pygame
from extra.world import *


class Saw(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        img = pygame.image.load('kansio/saw.png')
        self.image = pygame.transform.scale(img, tile_size, tile_size // 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
