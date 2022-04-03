import pygame
import sys

pygame.init()
pygame.font.init()

ww = 900
wh = 600
FPS = 120

INKY_BLACK = (0,  0,  0)
FIREY_RED = (203, 49,  7)

speed = 5
jump = False
jumpHeight = -20


class Alusta(pygame.sprite.Sprite):
    def __init__(self, maze_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(maze_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Eteen(pygame.sprite.Sprite):
    def __init__(self, maze_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(maze_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Alusta_col(pygame.sprite.Sprite):
    def __init__(self, maze_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(maze_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, x=50, y=50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.top = 50
        self.down = False
        self.up = False
        self.left = False
        self.right = False

    def update(self):
        window.blit(self.image, self.rect)
        if self.up:
            self.rect.top -= speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.bottom +=speed
        if self.down:
            self.rect.bottom += speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.bottom -=speed
        if self.left:
            self.rect.left -= speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.bottom +=speed
        if self.right:
            self.rect.right += speed
            if (pygame.sprite.spritecollide(alusta_col, player_group, False, collided=pygame.sprite.collide_mask)):
                self.rect.bottom -=speed


SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((ww, wh), SURFACE)
pygame.display.set_caption("Testi 01")


# Make some sprites to hold the Maze background and Player's Alien
alusta_col = Alusta_col('level-alpha-test.png')
alusta = Alusta('alusta.png')
player = Player("mario.png", 100, 100)
eteen = Eteen('eteen.png')

# All sprites for updating and drawing
sprite_group = pygame.sprite.Group()
sprite_group.add(alusta_col)
sprite_group.add(alusta)
sprite_group.add(player)
player_group = pygame.sprite.GroupSingle()   # Just for the player collisions
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

    background = INKY_BLACK

    sprite_group.update()
    player.update()
    window.fill(background)
    sprite_group.draw(window)
    pygame.display.flip()
    clock.tick_busy_loop(FPS)
