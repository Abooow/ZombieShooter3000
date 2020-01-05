''' Main file for ZoombieShooter3000
'''

import pygame
import event_handler
import utils

from screens.screen import Screen
from screens.menu_screen import MenuScreen
from screens.load_screen import LoadScreen


# Initialize pygame
pygame.init()

# Initialize the game window
utils.window = pygame.display.set_mode((utils.window_size[0], utils.window_size[1]))
pygame.display.set_caption('Zombie Shooter 3000')

# Icon
#icon = pygame.image.load('content/sprites/icon.png')
#pygame.display.set_icon(icon)

# Used font for txt
#config.font = pygame.font.SysFont('Tahoma',18, True, False)

# set the current screen to 
Screen.load_screen(LoadScreen())
Screen.load_screen(MenuScreen())

# clock is used to get a framerate of 60fps
clock = pygame.time.Clock()


def main() -> None:
    ''' The main function of the program that contains the gameLoop
    '''

    # ---------------------- GameLoop
    while not utils.quit_game:

        # --------------------UPDATE--------------------
        event_handler.update()
        Screen.get_current_screen().update(clock.get_time())    # update everything in the current screen

        # ---------------------DRAW---------------------
        utils.window.fill((20, 20, 20))                         # clear screen
        Screen.get_current_screen().draw(utils.window)          # draw everything in the current screen
        pygame.display.update()                                 # render everything

        clock.tick(100) # set the FPS to 100


if __name__ == '__main__':
    # main loop
    main()

    # Quit
    pygame.quit()
    #sys.exit()