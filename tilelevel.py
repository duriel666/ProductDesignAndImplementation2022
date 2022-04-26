import pygame
from tiletile import Tile
from tilemap import *
from tileplayer import *
from tileenemy import *
from pygame import mixer

vec = pygame.math.Vector2


class Level:
    def __init__(self, level_data, surface):
        # the level setup
        self.display_surface = surface
        self.levelsetup(level_data)

        self.worldmove = vec(0, 0)

    def levelsetup(self, layout):
        self.tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == '1':
                    tile = Tile((x, y), tile_size,'gfx/1.png')
                    self.tile.add(tile)
                if cell == '2':
                    tile = Tile((x, y), tile_size,'gfx/2.png')
                    self.tile.add(tile)
                if cell == '3':
                    tile = Tile((x, y), tile_size,'gfx/3.png')
                    self.tile.add(tile)
                if cell == '4':
                    tile = Tile((x, y), tile_size,'gfx/4.png')
                    self.tile.add(tile)
                if cell == '5':
                    tile = Tile((x, y), tile_size,'gfx/5.png')
                    self.tile.add(tile)
                if cell == '6':
                    tile = Tile((x, y), tile_size,'gfx/6.png')
                    self.tile.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'E':
                    enemy_sprite = Enemy((x-25, y))
                    self.enemy.add(enemy_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < ww / 4 and direction_x < 0:
            self.worldmove.x = 8
            player.speed = 0
        elif player_x > ww - (ww / 4) and direction_x > 0:
            self.worldmove.x = -8
            player.speed = 0
        else:
            self.worldmove.x = 0
            player.speed = 8

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.top
        direction_y = player.direction.y
        if player_y < wh / 4 and direction_y < 0:
            self.worldmove.y = -direction_y
            direction_y = 0
        elif player_y > wh - (wh / 4) and direction_y > 0:
            self.worldmove.y = -direction_y
            direction_y = 0
        else:
            player.direction.y = -self.worldmove.y
            self.worldmove.y = 0

    def x_moving_coll(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def y_moving_coll(self):
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.add_gravity()
        for sprite in self.tile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False
                    self.player.sprite.direction.y = -3
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.jumping = False
                    self.player.sprite.direction.y = -3

    def enemy_coll(self):
        hitSound = pygame.mixer.Sound('kansio/clang.wav')
        enemy_collision = pygame.sprite.spritecollide(
            self.player.sprite, self.enemy, False)
        if enemy_collision:
            for enemy in enemy_collision:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -4
                    hitSound.play()
                    enemy.kill()
                    self.player.jumping = False

    def run(self):
        self.tile.update(self.worldmove.x, self.worldmove.y)
        self.tile.draw(self.display_surface)
        # blob_group.draw(self.display_surface)
        self.enemy.update(self.worldmove.x, self.worldmove.y)
        self.enemy.draw(self.display_surface)
        self.scroll_x()
        # self.scroll_y()
        self.player.update()
        self.x_moving_coll()
        self.y_moving_coll()
        self.enemy_coll()
        self.player.draw(self.display_surface)
