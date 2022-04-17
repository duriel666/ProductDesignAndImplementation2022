import pygame
from pygame.locals import *
from selecttilelevel import *
import sys
import time

pygame.init()
pygame.font.init()

vec = pygame.math.Vector2

ww = screen.get_width()
wh = screen.get_height()
gw = 4961  # game world width
gh = 3508  # game world height
fps = 120
acceleration = 0.2
friction = -0.04
black = (0,  0,  0)
white = (255, 255, 255)

game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 30)

volume_up, timer = pygame.USEREVENT+1, 200
bounce = pygame.mixer.Sound('sfx/ball-on-grass.mp3')
point_get = pygame.mixer.Sound('sfx/beach-point.mp3')
point_get.set_volume(0.4)

pygame.time.set_timer(volume_up, timer)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos, level, door_image):
        super().__init__()
        self.image = pygame.image.load(door_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.level = level

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed

    def select(self):
        if self.level == 'map':
            return 'map'
        if self.level == 'tile':
            return select_forest_tile(player.score)


class Point(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('gfx/forest-point.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed


class World(pygame.sprite.Sprite):
    def __init__(self, world_image):
        super().__init__()
        self.image = pygame.image.load(world_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(0, -gh+wh)
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.images = []
        for i in range(0, 72):
            self.images.append(pygame.image.load(
                f'gfx/puolukka{str(i+1)}.png'))
        self.image = self.images[self.index].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(ww/8, wh-wh/8)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.score = 0
        self.keys = 0

    def move(self):
        self.acc = vec(0, acceleration)
        sound_volume = 0
        key = pygame.key.get_pressed()
        hits = pygame.sprite.spritecollide(
            self, col_group, False, collided=pygame.sprite.collide_mask)
        hits_wall = pygame.sprite.spritecollide(
            self, col_group_wall, False, collided=pygame.sprite.collide_mask)

        if key[K_a]:
            self.acc.x = -acceleration
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1
        if hits and self.vel.y >= -4:
            self.vel.y -= 1
        if self.vel.x < 0:
            if hits_wall:
                self.vel.x = 2
        if key[K_d]:
            self.acc.x = acceleration
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        if hits and self.vel.y >= -4:
            self.vel.y -= 1
        if self.vel.x > 0:
            if hits_wall:
                self.vel.x = -2
        if self.vel.y < 0:
            if hits_wall:
                self.vel.y = -self.vel.y
            if hits and hits_wall:
                self.vel.y = -3

        self.image = self.images[self.index]

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + acceleration * self.acc

        self.rect.midbottom = self.pos

        if self.vel.y > 0:
            if hits and hits_wall:
                if self.vel.y >= 0.6:
                    self.vel.y = -self.vel.y*.6
                else:
                    self.vel.y = -0.6
                self.jumping = False
            elif hits:
                if self.vel.y >= 0.6:
                    self.vel.y = -self.vel.y*.6
                else:
                    self.vel.y = -0.6
                self.jumping = False
        sound_volume = -self.vel.y/40
        if sound_volume > 1:
            sound_volume = 1

        if hits or hits_wall and sound_volume > 0.3:
            bounce.set_volume(sound_volume)
            bounce.play()

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


window = pygame.display.set_mode((ww, wh))

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

#collision = World('gfx/forest-col.png')
collision_wall = World('gfx/forest-col-wall.png')
collision_floor = World('gfx/forest-col-floor.png')
taakse = World(f'gfx/forest-bg.png')
eteen = World('gfx/forest-fg.png')

points = []
points.append(Point((150, 450)))
points.append(Point((800, 500)))
points.append(Point((1500, 400)))
points.append(Point((1920, 550)))
points.append(Point((2500, -200)))
points_found = []
point_group = pygame.sprite.Group()
for point in points:
    point_group.add(point)

doors = []
doors.append(Door((200, 770), 'map', 'gfx/drawn-mario.png'))
doors.append(Door((4650, -1808), 'tile', 'gfx/drawn-mario.png'))
door_group = pygame.sprite.Group()
for door in doors:
    door_group.add(door)

score_count = int(len(points))

col_group = pygame.sprite.Group()
col_group.add(collision_floor)
col_group_wall = pygame.sprite.Group()
col_group_wall.add(collision_wall)
sprite_group = pygame.sprite.Group()
sprite_group.add(taakse)
sprite_group.add(player)
sprite_group.add(eteen)

world_list = [eteen, taakse, collision_wall, collision_floor]
for point in points:
    world_list.append(point)
for door in doors:
    world_list.append(door)

clock = pygame.time.Clock()


def start_game(run, score):
    player.score = score
    music_volume = 0
    while run:
        for event in pygame.event.get():
            if event.type == volume_up:
                if music_volume < 0.3:
                    music_volume += 0.001
                    pygame.mixer.music.set_volume(music_volume)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    run = False
                    return player.score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.cancel_jump()
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                run = False
                return player.score
            for door in doors:
                if pygame.sprite.spritecollide(door, player_group, False, collided=pygame.sprite.collide_mask):
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            pygame.mixer.music.stop()
                            if door.select() == 'map':
                                run = False
                                return player.score
                            else:
                                door.select()

        speed_x = player.vel.x
        speed_y = player.vel.y
        if player.pos.x < 400 and player.vel.x < 0 and collision_floor.pos.x < 0:
            for world in world_list:
                world.scroll_x(-(speed_x))
            player.vel.x = 0
            player.pos.x -= speed_x
        elif player.pos.x > ww-400 and player.vel.x > 0 and collision_floor.pos.x > (-gw+ww):
            for world in world_list:
                world.scroll_x(-(speed_x))
            player.vel.x = 0
            player.pos.x -= speed_x
        if player.pos.y < 300 and player.vel.y < 0 and collision_floor.pos.y < 0:
            for world in world_list:
                world.scroll_y(-(speed_y))
            player.vel.y = 0
            player.pos.y -= speed_y
        elif player.pos.y > wh-300 and player.vel.y > 0 and collision_floor.pos.y > (-gh+wh):
            for world in world_list:
                world.scroll_y(-(speed_y))
            player.vel.y = 0
            player.pos.y -= speed_y
        else:
            for world in world_list:
                world.scroll_x(0)
                world.scroll_y(0)
            player.vel.x = speed_x
            player.vel.y = speed_y
        player.vel.x = speed_x
        player.vel.y = speed_y

        for point in points:
            if (pygame.sprite.spritecollide(point, player_group, False, collided=pygame.sprite.collide_mask)):
                point.kill()
                points_found.append(point)
                points.remove(point)
                point_get.play()
        player.score = -int(len(points))+int(score_count)

        sprite_group.update()
        col_group.update()
        player_group.update()
        point_group.update()
        window.fill(white)
        door_group.draw(window)
        sprite_group.draw(window)
        point_group.draw(window)
        player.move()

        game_font.render_to(
            window, (0, 0), f'player.vel.x - {player.vel.x:,.3f}', (black))
        game_font.render_to(
            window, (0, 30), f'player.vel.y - {player.vel.y:,.3f}', (black))
        game_font.render_to(
            window, (0, 60), f'player.score - {player.score}', (black))
        game_font.render_to(
            window, (0, 90), f'player.pos.x - {player.pos[0]:,.2f}', (black))
        game_font.render_to(
            window, (0, 120), f'player.pos.x - {player.pos[1]:,.2f}', (black))

        pygame.display.flip()
        clock.tick(fps)
