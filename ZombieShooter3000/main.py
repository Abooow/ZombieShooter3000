''' Main file for ZoombieShooter3000
'''

import pygame
import event_handler
import config
import utils

from screens.test_screen import TestScreen
from screens.object_screen import TestScreen


# Initialize pygame
pygame.init()

# Initialize the game window
window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Zombie Shooter 3000')

# Icon
#icon = pygame.image.load('content/sprites/icon.png')
#pygame.display.set_icon(icon)

# Used font for txt
#config.font = pygame.font.SysFont('Tahoma',18, True, False)

# set the current screen to 
utils.current_screen = TestScreen(window)

# clock is used to get a framerate of 60fps
clock = pygame.time.Clock()


def main() -> None:
    ''' The main function of the program

    :returns: nothing
    :rtype: None
    '''

    # ---------------------- GameLoop
    while not utils.quit_game:

        pygame.display.set_caption(f'Zombie Shooter 3000 - fps: {clock.get_fps()}')

        # --------------------UPDATE--------------------
        event_handler.update()
        utils.current_screen.update(clock.get_time()) # update everything in the current screen

        # ---------------------DRAW---------------------
        window.fill((20, 20, 20))               # clear screen
        utils.current_screen.draw(window)       # draw everything in the current screen
        pygame.display.update()                 # render everything

        clock.tick(100) # set the FPS to 100


if __name__ == '__main__':
    # main loop
    main()

    # Quit
    pygame.quit()
    #sys.exit()