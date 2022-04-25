import time
from menu import *

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Game - 0.4 beta')

black = (0,  0,  0)
white = (255, 255, 255)

time_start = time.time()

# starting the game and timer. first screen is menu with "start", "help", "options" and "quit" buttons
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
