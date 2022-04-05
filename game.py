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
   
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0 
 
    def move(self):
        self.acc = vec(0,acceleration)
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -acceleration
        if pressed_keys[K_RIGHT]:
            self.acc.x = acceleration
                 
        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + acceleration * self.acc
         
        if self.pos.x > ww:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = ww
             
        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits=pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)
        if not self.jumping:
           self.jumping = True
           self.vel.y = -8
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):
        hits=pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask)
        if self.vel.y > 0:        
            if hits:
                self.pos.y -=1
                self.vel.y =0
                self.jumping = False


SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh), SURFACE)
pygame.display.set_caption("Testi 01")


alusta_col = Alusta_col('level-alpha-test.png')
alusta = Alusta('alusta.png')
player = Player("mario.png")
eteen = Eteen('eteen.png')

col_group=pygame.sprite.Group()
col_group.add(alusta_col)
sprite_group = pygame.sprite.Group()
sprite_group.add(alusta_col)
sprite_group.add(alusta)
sprite_group.add(player)
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
sprite_group.add(eteen)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                player.cancel_jump()

    background = black
    sprite_group.update()
    col_group.update()
    player.update()
    window.fill(background)
    sprite_group.draw(window)
    player.move()
    pygame.display.flip()
    clock.tick(fps)
