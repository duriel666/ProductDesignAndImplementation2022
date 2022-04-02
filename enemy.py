import pygame

class Enemy(pygame.sprite.Sprite): #pygame sprite has a buildin draw method
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
		
        self.image = pygame.image.load('kansio/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moving_enemy = 1
        self.moving_count = 0

    def update(self):
        self.rect.x += self.moving_enemy
        self.moving_count += 1
        if abs(self.moving_count) > 50: #absolut value
            self.moving_enemy *= -1
            self.moving_count *= -1
