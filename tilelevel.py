import pygame
from tiletile import Tile
from tilemap import tile_size, ww
from tileplayer import *
from tileenemy import *


class Level:
    def __init__(self, level_data, surface):
        # the level setup
        self.display_surface = surface
        self.levelsetup(level_data)

        self.worldmove = 0

    def levelsetup(self, layout):
        self.tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
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
            self.worldmove = 8
            player.speed = 0
        elif player_x > ww - (ww / 4) and direction_x > 0:
            self.worldmove = -8
            player.speed = 0

        else:
            self.worldmove = 0
            player.speed = 8

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
        player.add_gravity()
        for sprite in self.tile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tile.update(self.worldmove)
        self.tile.draw(self.display_surface)
        # blob_group.draw(self.display_surface)
        self.enemy.update(self.worldmove)
        self.enemy.draw(self.display_surface)
        self.scroll_x()
        self.player.update()
        self.x_moving_coll()
        self.y_moving_coll()
        self.player.draw(self.display_surface)
