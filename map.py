from selectdrawnlevel import *

gw = 4961  # game world width
gh = 3508  # game world height
fps = 60
friction = -0.08
black = (0,  0,  0)
white = (255, 255, 255)
game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 30)

class Point(pygame.sprite.Sprite):
    def __init__(self, pos, level, level_image):
        super().__init__()
        self.image = pygame.image.load(level_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.level = level

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x = speed

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y = speed

    def select(self):
        if self.level == 'forest':
            return select_forest(player.score)
        if self.level == 'beach':
            return select_beach(player.score)


class World(pygame.sprite.Sprite):
    def __init__(self, world_image):
        super().__init__()
        self.image = pygame.image.load(world_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x = speed*((self.width-ww)/(gw-ww))

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y = speed*((self.height-wh)/(gh-wh))


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
        self.pos = vec(ww/2, wh/2)
        self.pos_virtual = vec(0, gh-wh)
        self.shadow_pos = vec(self.pos.x-20, self.pos.y-20)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.score = 0
        self.acceleration = 0.4

    def move(self):
        self.acc = vec(0, 0)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a] and pressed_keys[K_w]:
            self.acc.x = -self.acceleration*0.707
            self.acc.y = -self.acceleration*0.707
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1

        elif pressed_keys[K_a] and pressed_keys[K_s]:
            self.acc.x = -self.acceleration*0.707
            self.acc.y = self.acceleration*0.707
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1

        elif pressed_keys[K_d] and pressed_keys[K_w]:
            self.acc.x = self.acceleration*0.707
            self.acc.y = -self.acceleration*0.707
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        elif pressed_keys[K_d] and pressed_keys[K_s]:
            self.acc.x = self.acceleration*0.707
            self.acc.y = self.acceleration*0.707
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        elif pressed_keys[K_a]:
            self.acc.x = -self.acceleration
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1

        elif pressed_keys[K_d]:
            self.acc.x = self.acceleration
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        elif pressed_keys[K_w]:
            self.acc.y = -self.acceleration
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1

        elif pressed_keys[K_s]:
            self.acc.y = self.acceleration
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        if pygame.sprite.spritecollide(self, col_group, False, collided=pygame.sprite.collide_mask) and self.vel != 0:
            if self.vel.x < 0 and self.vel.y < 0:
                self.pos_virtual.x += 2
                self.pos_virtual.y += 2
                self.vel.x=0
                self.vel.y=0
            elif self.vel.x < 0 and self.vel.y > 0:
                self.pos_virtual.x += 2
                self.pos_virtual.y += -2
                self.vel.x=0
                self.vel.y=0
            elif self.vel.x > 0 and self.vel.y < 0:
                self.pos_virtual.x += -2
                self.pos_virtual.y += 2
                self.vel.x=0
                self.vel.y=0
            elif self.vel.x > 0 and self.vel.y > 0:
                self.pos_virtual.x += -2
                self.pos_virtual.y += -2
                self.vel.x=0
                self.vel.y=0
            elif self.vel.x < 0:
                self.pos_virtual.x += 2
                self.vel.x=0
            elif self.vel.x > 0:
                self.pos_virtual.x += -2
                self.vel.x=0
            elif self.vel.y < 0:
                self.pos_virtual.y += 2
                self.vel.y=0
            elif self.vel.y > 0:
                self.pos_virtual.y += -2
                self.vel.y=0

        self.image = self.images[self.index]
        self.rect.midbottom = self.pos

        self.acc += self.vel * friction
        self.vel += self.acc
        self.pos_virtual += self.vel + self.acceleration * self.acc


class Shadow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'gfx/puolukka-shadow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec((ww/2, wh-wh/2))

    def update(self):
        self.pos = player.pos
        self.rect.midbottom = self.pos + (0, 30)


window = pygame.display.set_mode((ww, wh))

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

shadow = Shadow()
shadow_group = pygame.sprite.GroupSingle()
shadow_group.add(shadow)

collision = World('gfx/map-col.png')
taakse = World('gfx/map.png')
cloud_shadows = World('gfx/map-clouds-shadows.png')
clouds = World('gfx/map-clouds.png')
clouds2 = World('gfx/map-clouds2.png')

points = []
points.append(Point((1500, -50), 'forest', 'gfx/forest-entrance.png'))
points.append(Point((1000, -850), 'level2', 'gfx/drawn-mario.png'))
points.append(Point((800, 550), 'beach', 'gfx/drawn-mario.png'))

points_found = []

score_count = int(len(points))

col_group = pygame.sprite.Group()
col_group.add(collision)
sprite_group = pygame.sprite.Group()
# sprite_group.add(collision)
sprite_group.add(taakse)
sprite_group.add(shadow)
for point in points:
    sprite_group.add(point)
sprite_group.add(player)
sprite_group.add(cloud_shadows)
sprite_group.add(clouds2)
sprite_group.add(clouds)

world_list = [clouds2, clouds, cloud_shadows, taakse, collision]
for point in points:
    world_list.append(point)

clock = pygame.time.Clock()


def start_game(run):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return player.score
            if event.type == pygame.QUIT:
                run = False
                return player.score
            for point in points:
                if pygame.sprite.spritecollide(point, player_group, False, collided=pygame.sprite.collide_mask):
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            point.select()

        '''speed_x = player.vel.x
        speed_y = player.vel.y
        for world in world_list:
            world.scroll_x(-speed_x)
            world.scroll_y(-speed_y)'''
        for world in world_list:
            world.scroll_x(-player.pos_virtual[0])
            world.scroll_y(-player.pos_virtual[1])

        window.fill((70, 117, 215))
        sprite_group.update()
        col_group.update()
        shadow_group.update()
        player_group.update()
        shadow.update()
        player.update()
        sprite_group.draw(window)
        player.move()
        game_font.render_to(
                window, (0, 0), f'fps - {clock.get_fps()}', (black))
        game_font.render_to(
                window, (0, 30), f'player.vel - {player.vel.x:,.2f} - {player.vel.y:,.2f}', (black))

        pygame.display.flip()
        clock.tick(fps)
