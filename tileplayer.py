import pygame
from tilethings import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = pygame.image.load('kuvat/mario.png')
        # self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)

        self.gravity = 1
        self.jumpspeed = -16
        self.speed = 8

    def import_character(self):
        char_path = './kuvat'
        self.animations = {'run': []}
        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()

    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jumpspeed

    def update(self):
        self.get_input()
