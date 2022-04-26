import pygame
from tilethings import import_folder

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.import_character()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.index = 0
        self.images = []
        for i in range(0, 72):
            self.images.append(pygame.image.load(
                'gfx/character/puolukka'+str(i+1)+'.png'))
        self.image = pygame.transform.scale(
            self.images[self.index].convert_alpha(), (60, 60))
        self.rect = self.image.get_rect(topleft=pos)
        self.score = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.4
        self.jumpspeed = -10
        self.speed = 8
        self.jumping = False

    def import_character(self):
        char_path = './kuvat'
        self.animations = {'run': []}
        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1
        else:
            self.direction.x = 0
        if keys[pygame.K_w]:
            self.jump()
        #self.image = self.index

    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if not self.jumping:
            self.direction.y = self.jumpspeed
            self.jumping = True

    def update(self):
        self.get_input()
