import pygame, sys
from tilemap import * 
from tilelevel import Level

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('pink')
	level.run()

	pygame.display.update()
	clock.tick(60)