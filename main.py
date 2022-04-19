import pygame
import time
from menu import *

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Game - 0.2')

ww = 1280  # window width
wh = 720  # window height

black = (0,  0,  0)
white = (255, 255, 255)

time_start = time.time()

if __name__ == "__main__":
    print(f'Score: {gamemenu(True)}')
    time_played = time.time()-time_start
    if time_played > 60:
        time_played = time_played/60
        if time_played > 60:
            time_played = time_played/60
            print(f'Time played: {time_played:.1f} hours')
        else:
            print(f'Time played: {time_played:.1f} minutes')
    else:
        print(f'Time played: {time_played:.1f} seconds')
