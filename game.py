import pygame
import sys

pygame.init()
pygame.font.init()

ww = 900
wh = 600
fps = 120

black = (0,  0,  0)

speed = 2
jump = False
jumpHeight = -20


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
    def __init__(self, player_image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = x/2
        self.rect.top = y/2
        self.down = False
        self.up = False
        self.left = False
        self.right = False

    def update(self):
        window.blit(self.image, self.rect)
        if self.up:
            self.rect.top -= speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.top += speed
        if self.down:
            self.rect.bottom += speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.bottom -= speed
        if self.left:
            self.rect.left -= speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.top -= 1
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    self.rect.left += speed
                    self.rect.top += 1

        if self.right:
            self.rect.right += speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.top -= 1
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    self.rect.right -= speed
                    self.rect.top += 1


SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh), SURFACE)
pygame.display.set_caption("Testi 01")


alusta_col = Alusta_col('level-alpha-test.png')
alusta = Alusta('alusta.png')
player = Player("mario.png", 100, 100)
eteen = Eteen('eteen.png')

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
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    player.up = False
                else:
                    player.up = True
            elif event.key == pygame.K_s:
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    player.down = False
                else:
                    player.down = True
            elif event.key == pygame.K_a:
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    player.left = False
                else:
                    player.left = True
            elif event.key == pygame.K_d:
                if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                    player.right = False
                else:
                    player.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.up = False
            elif event.key == pygame.K_s:
                player.down = False
            elif event.key == pygame.K_a:
                player.left = False
            elif event.key == pygame.K_d:
                player.right = False

    background = black
    sprite_group.update()
    player.update()
    window.fill(background)
    sprite_group.draw(window)
    pygame.display.flip()
    clock.tick_busy_loop(fps)
