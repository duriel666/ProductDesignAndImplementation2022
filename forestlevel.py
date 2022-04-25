from selecttilelevel import *
import random

vec = pygame.math.Vector2


def start_game_forest(run, score):
    alive = True
    while alive:
        pygame.init()
        pygame.font.init()

        gw = 4961  # game world width
        gh = 3508  # game world height
        fps = 60
        friction = -0.06
        black = (0,  0,  0, 200)
        white = (255, 255, 255, 200)
        red = (255, 0, 0, 200)
        text_shadow = (0, 0, 0, 125)

        game_font = pygame.freetype.Font('fonts/HelveticaNeue Light.ttf', 50)

        volume_up, timer = pygame.USEREVENT+1, 200
        bounce = pygame.mixer.Sound('sfx/forest-bounce.wav')
        point_get = pygame.mixer.Sound('sfx/forest-point.wav')
        point_get.set_volume(0.4)

        pygame.time.set_timer(volume_up, timer)

        '''class Polygon(pygame.sprite.Sprite):
            def __init__(self, pos, surface, color, points):
                super().__init__()
                self.surface = surface
                lx, ly = zip(*points)
                min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
                self.rect = pygame.Rect(
                    pos[0], pos[1], max_x - min_x, max_y - min_y)
                self.shape = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                pygame.draw.polygon(self.shape, color, [
                                    (x - min_x, y - min_y) for x, y in points])
                self.pos = vec(pos[0],pos[1]+wh)
                self.vel = vec(0, 0)

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed

            def update(self):
                self.surface.blit(self.shape, self.rect)'''

        class Door(pygame.sprite.Sprite):
            def __init__(self, pos, level, door_image, size):
                super().__init__()
                self.image = pygame.image.load(door_image).convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.width = size[0]
                self.height = size[1]
                self.pos = vec(pos[0], pos[1]+wh)
                self.vel = vec(0, 0)
                self.level = level

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed*((self.width-ww)/(gw-ww))

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed*((self.height-wh)/(gh-wh))

            def select(self):
                if self.level == 'map':
                    return 'map'
                if self.level == 'tile':
                    return select_forest_tile(player.score)

        class Point(pygame.sprite.Sprite):
            def __init__(self, pos):
                super().__init__()
                self.image = pygame.image.load(
                    'gfx/forest-point.png').convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.pos = vec(pos[0], pos[1]+wh)
                self.vel = vec(0, 0)

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed

        class Chest(pygame.sprite.Sprite):
            def __init__(self, pos):
                super().__init__()
                self.index = 0
                self.images = []
                self.images.append(pygame.image.load(
                    'gfx/forest-chest-closed.png').convert_alpha())
                self.images.append(pygame.image.load(
                    'gfx/forest-chest-open.png').convert_alpha())
                self.image = self.images[self.index].convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.pos = vec(pos[0], pos[1]+wh)
                self.vel = vec(0, 0)
                self.status = True

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed

            def open(self):
                self.index = 1
                self.image = self.images[self.index]
                player.health += 1
                self.status = False

        class Enemy_soft(pygame.sprite.Sprite):
            def __init__(self, pos, enemy_image, size):
                super().__init__()
                self.image = pygame.image.load(enemy_image).convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.width = size[0]
                self.height = size[1]
                self.pos = vec(pos[0], pos[1]+wh)
                self.vel = vec(0, 0)

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed*((self.width-ww)/(gw-ww))

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed*((self.height-wh)/(gh-wh))

        class World(pygame.sprite.Sprite):
            def __init__(self, world_image):
                super().__init__()
                self.image = pygame.image.load(world_image).convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.pos = vec(0, wh-self.height)
                self.vel = vec(0, 0)

            def scroll_x(self, speed):
                self.rect.topleft = self.pos
                self.pos.x += speed*((self.width-ww)/(gw-ww))

            def scroll_y(self, speed):
                self.rect.topleft = self.pos
                self.pos.y += speed*((self.height-wh)/(gh-wh))

        class Player(pygame.sprite.Sprite):
            def __init__(self, pos):
                super().__init__()
                self.index = 0
                self.images = []
                for i in range(0, 72):
                    self.images.append(pygame.image.load(
                        f'gfx/character/puolukka{str(i+1)}.png'))
                self.image = self.images[self.index].convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.pos = vec(pos[0], pos[1]+wh)
                self.vel = vec(0, 0)
                self.acc = vec(0, 0)
                self.jumping = False
                self.score = 0
                self.keys = 0
                self.health = 3
                self.gravity = 0.4
                self.acceleration = 0.4

            def move(self):
                self.acc = vec(0, self.gravity)
                vol = 40
                key = pygame.key.get_pressed()
                hits_floor = pygame.sprite.spritecollide(
                    self, col_group, False, collided=pygame.sprite.collide_mask)
                hits_wall = pygame.sprite.spritecollide(
                    self, col_group_wall, False, collided=pygame.sprite.collide_mask)

                # if bounce.wav played at speed related volume if not playing
                if bounce.get_num_channels() < 1:
                    if hits_floor and self.vel.y != 0:
                        sound_volumey = self.vel.y/vol
                        if sound_volumey < 0:
                            sound_volumey = -sound_volumey
                        bounce.set_volume(sound_volumey)
                        bounce.play()
                    elif hits_wall and self.vel.x != 0:
                        sound_volumex = self.vel.x/vol
                        if sound_volumex < 0:
                            sound_volumex = -sound_volumex
                        bounce.set_volume(sound_volumex)
                        bounce.play()

                # character animation played to movement direction
                if key[K_a]:
                    self.acc.x = -self.acceleration
                    self.index -= 1
                    if self.index <= 0:
                        self.index = len(self.images)-1
                if key[K_d]:
                    self.acc.x = self.acceleration
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0

                if hits_floor or hits_wall:
                    if self.jumping:
                        self.jumping = False
                    if hits_wall:
                        if self.vel.x > 0:
                            self.pos.x -= 2
                        if self.vel.x < 0:
                            self.pos.x += 2
                        if self.vel.y < 0:
                            self.vel.y = 0
                        self.vel.x = 0
                if hits_floor:
                    self.gravity = 0
                    self.vel.y = 0
                    if self.vel.y > 10:
                        self.vel.y = -self.vel.y*0.7
                    elif self.vel.y <= 7:
                        self.vel.y = -7
                if not hits_floor:
                    self.gravity = 0.4

                self.image = self.images[self.index]

                self.acc.x += self.vel.x * friction
                self.vel += self.acc
                self.pos += self.vel + self.gravity * self.acc

                self.rect.midbottom = self.pos

                sound_volume = -self.vel.y/40
                if sound_volume > 1:
                    sound_volume = 1

            def jump(self):
                if not self.jumping:
                    self.jumping = True
                    self.vel.y = -17

            def cancel_jump(self):
                if self.jumping:
                    if self.vel.y < -5:
                        self.vel.y = -5

        player = Player((100, -100))
        player_group = pygame.sprite.GroupSingle()
        player_group.add(player)

        # images for World class
        collision_wall = World('gfx/forest-col-wall.png')
        collision_floor = World('gfx/forest-col-floor.png')
        taakse = World(f'gfx/forest-bg.png')
        eteen = World('gfx/forest-fg.png')
        light = World('gfx/forest-light.png')
        testi = World(f'gfx/menu-bg.png')

        # adding water droplets to be collected
        points = []
        points.append(Point((1013, -534)))
        points.append(Point((1949, -822)))
        points.append(Point((4697, -1182)))
        points.append(Point((4661, 1781)))
        points.append(Point((2009, -1865)))
        points.append(Point((144, -2804)))
        points.append(Point((547, -1649)))
        points.append(Point((1917, -2005)))
        points.append(Point((3603, -2855)))
        points.append(Point((4597, -2056)))
        points.append(Point((2899, -1187)))
        points.append(Point((2104, -1860)))
        points.append(Point((2312, -1872)))
        points.append(Point((2460, -1805)))
        points.append(Point((2218, -1872)))
        points.append(Point((2159, -1868)))
        points.append(Point((903, -2318)))
        points.append(Point((3497, -521)))
        points.append(Point((4061, -2921)))
        points.append(Point((641, -3250)))
        points.append(Point((1948, -400)))
        points.append(Point((1126, -228)))
        points.append(Point((1064, -1633)))
        points.append(Point((1283, -1520)))
        points.append(Point((1991, -3187)))
        # points.append(Point(()))

        points_found = []
        point_group = pygame.sprite.Group()
        for point in points:
            point_group.add(point)

        chests = []
        chests.append(Chest((4073, -233)))
        chests.append(Chest((500, -233)))
        chests.append(Chest((4073, -1233)))
        chest_group = pygame.sprite.Group()
        for chest in chests:
            chest_group.add(chest)

        doors = []
        doors.append(
            Door((25, -280), 'map', 'gfx/forest-entrance.png', (gw*0.95, gh*0.95)))
        doors.append(Door((4553, -2585), 'tile',
                     'gfx/forest-entrance.png', (gw*1.05, gh*1.05)))
        door_group = pygame.sprite.Group()
        for door in doors:
            door_group.add(door)

        # enemies_soft take one health from player
        # enemies_hard kill from single hit (not implemented yet)
        enemies_soft = []
        enemies_soft.append(Enemy_soft(
            (2189, -292), 'gfx/forest-enemy-soft.png', (gw*0.95, gh*0.95)))
        enemies_soft.append(Enemy_soft(
            (1271, -1148), 'gfx/forest-enemy-soft.png', (gw*1.05, gh*0.95)))
        enemies_soft.append(Enemy_soft(
            (593, -2242), 'gfx/forest-enemy-soft.png', (gw*1.1, gh*1.05)))
        enemies_soft.append(Enemy_soft(
            (3200, -2920), 'gfx/forest-enemy-soft.png', (gw*0.9, gh*0.9)))
        enemies_soft_hit = []
        enemy_soft_group = pygame.sprite.Group()
        for enemy_soft in enemies_soft:
            enemy_soft_group.add(enemy_soft)

        score_count = int(len(points))

        col_group = pygame.sprite.Group()
        col_group.add(collision_floor)
        col_group_wall = pygame.sprite.Group()
        col_group_wall.add(collision_wall)
        # sprites added in sequence from bottom to top
        sprite_group = pygame.sprite.Group()
        sprite_group_back = pygame.sprite.Group()
        sprite_group_back.add(testi)
        sprite_group.add(taakse)
        sprite_group2 = pygame.sprite.Group()
        sprite_group2.add(light)
        sprite_group2.add(eteen)

        world_list = [light, testi, eteen, taakse,
                      collision_wall, collision_floor]
        for point in points:
            world_list.append(point)
        for door in doors:
            world_list.append(door)
        for chest in chests:
            world_list.append(chest)
        for enemy_soft in enemies_soft:
            world_list.append(enemy_soft)

        clock = pygame.time.Clock()

        def rect_a(surface, color, rect):
            shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.rect(shape, color, shape.get_rect())
            surface.blit(shape, rect)

        player.score = score
        # background audio is raised from zero when level starts to x in y milliseconds with userevent
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
                for chest in chests:
                    if pygame.sprite.spritecollide(chest, player_group, False, collided=pygame.sprite.collide_mask):
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_e:
                                if chest.status:
                                    chest.open()

            # scrolling screen when player goes near edge. in map the player stays in the middle
            speed_x = player.vel.x
            speed_y = player.vel.y
            if player.pos.x < ww/3.2 and player.vel.x < 0 and collision_floor.pos.x < 0:
                for world in world_list:
                    world.scroll_x(-speed_x)
                player.vel.x = 0
                player.pos.x -= speed_x
            elif player.pos.x > ww-(ww/3.2) and player.vel.x > 0 and collision_floor.pos.x > (-gw+ww):
                for world in world_list:
                    world.scroll_x(-speed_x)
                player.vel.x = 0
                player.pos.x -= speed_x
            if player.pos.y < wh/3 and player.vel.y < 0 and collision_floor.pos.y < 0:
                for world in world_list:
                    world.scroll_y(-speed_y)
                player.vel.y = 0
                player.pos.y -= speed_y
            elif player.pos.y > wh-(wh/3) and player.vel.y > 0 and collision_floor.pos.y > (-gh+wh):
                for world in world_list:
                    world.scroll_y(-speed_y)
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

            # counting score and health
            for point in points:
                if pygame.sprite.spritecollide(point, player_group, False, collided=pygame.sprite.collide_mask):
                    point.kill()
                    points_found.append(point)
                    points.remove(point)
                    point_get.play()
            player.score = -int(len(points))+int(score_count)

            for enemy_soft in enemies_soft:
                if pygame.sprite.spritecollide(enemy_soft, player_group, False, collided=pygame.sprite.collide_mask):
                    enemy_soft.kill()
                    enemies_soft_hit.append(enemy_soft)
                    enemies_soft.remove(enemy_soft)
            player.health -= len(enemies_soft_hit)
            enemies_soft_hit = []
            # updating and drawing sprites & items
            sprite_group.update()
            col_group.update()
            player_group.update()
            point_group.update()
            enemy_soft_group.update()
            window.fill(white)
            sprite_group_back.draw(window)
            door_group.draw(window)
            sprite_group.draw(window)
            chest_group.draw(window)
            player_group.draw(window)
            point_group.draw(window)
            enemy_soft_group.draw(window)
            player.move()
            sprite_group2.update()
            sprite_group2.draw(window)

            # rendering text to screen
            '''game_font.render_to(
                window, (20, 20), f'fps - {clock.get_fps():,.2f}', white)'''
            game_font.render_to(
                window, (ww-303, 23), 'Health', text_shadow)
            game_font.render_to(
                window, (ww-300, 20), 'Health', white)
            if player.health < 4:
                game_font.render_to(
                    window, (ww-143, 23), player.health*'O', text_shadow)
                game_font.render_to(
                    window, (ww-140, 20), player.health*'O', red)
            elif player.health >= 4 and player.health < 7:
                game_font.render_to(
                    window, (ww-143, 23), 3*'O', text_shadow)
                game_font.render_to(
                    window, (ww-140, 20), 3*'O', red)
                game_font.render_to(
                    window, (ww-143, 73), (player.health-3)*'O', text_shadow)
                game_font.render_to(
                    window, (ww-140, 70), (player.health-3)*'O', red)
            game_font.render_to(
                window, (ww-233, wh-57), f'Score {player.score}', text_shadow)
            game_font.render_to(
                window, (ww-230, wh-60), f'Score {player.score}', white)

            if len(enemies_soft_hit) == int(player.health):
                game_font.render_to(window, (400, 50),
                                    f'You died! press esc to exit', black)
                rect_a(window, (255, 0, 0, 80), (0, 0, ww, wh))
                player.gravity = 0
                player.acc = (0, 0)
                player.vel.x = 0
                player.vel.y = 0
                alive = False

            # refresh screen
            pygame.display.flip()
            clock.tick(fps)
