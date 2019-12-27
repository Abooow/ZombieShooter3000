''' This module contains the Screen class
'''

import pygame
import utils
import event_handler


class Screen():
    '''Base class for all screens, this class is abstract
    '''


    def __init__(self):
        # load_content() is called automatically after __init__()
        self.load_content()


    def load_content(self) -> None:
        ''' All content the are supposed to be loaded/initialized only once at the beginning are meant to belong in this method, this method is called once

        :returns: NoReturn
        :rtype: None
        '''
        
        pass


    def update(self, delta_time) -> None:
        ''' Every thing that are supposed to update every frame are meant to belong in this method, this method is called 60 FPS
        note: This method is called BEFORE the draw() method

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        # exit window when X button is pressed
        if event_handler.check_occurred(pygame.QUIT):
            utils.quit_game = True


    def draw(self, surface) -> None:
        ''' Every thing that are supposed to be drawn are ment to belong in this method, this method is called 60 FPS
        note: This method is called AFTER the update() method

        :param surface (surface): the surface to draw on

        :returns: NoReturn
        :rtype: None
        '''

        pass