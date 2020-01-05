''' This module contains the Screen class
'''

import pygame
import utils
import event_handler

from framework.vector2 import Vector2
from framework.camera import Camera
from framework.object_handler import ObjectHandler
from framework.components.transform import Transform


class Screen():
    '''Base class for all screens, this class is abstract
    '''


    _current_screen = None
    _last_screen = None


    ##################################################### Static methods
    def load_screen(screen) -> None:
        '''
        '''

        Screen._last_screen = Screen._current_screen
        Screen._current_screen = screen
        pass


    def get_current_screen():
        '''
        '''

        return Screen._current_screen


    def get_last_screen():
        '''
        '''

        return Screen._last_screen
    #####################################################


    def __init__(self):
        # load_content() is called automatically after __init__()
        self.load_content()


    def load_content(self) -> None:
        ''' All content the are supposed to be loaded/initialized only once at the beginning are meant to belong in this method, this method is called once

        :returns: NoReturn
        :rtype: None
        '''
        
        self.object_handler = ObjectHandler(Vector2(0, 0),
                                            Vector2.tuple_to_vector2(utils.world_size))
        self.camera = Camera(utils.window, 
                             self.object_handler, 
                             Transform(None), 
                             Vector2.tuple_to_vector2(utils.window_size), 
                             Vector2(0, 0))


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


        self.object_handler.update(delta_time)


    def draw(self, surface) -> None:
        ''' Every thing that are supposed to be drawn are ment to belong in this method, this method is called 60 FPS
        note: This method is called AFTER the update() method

        :param surface (surface): the surface to draw on

        :returns: NoReturn
        :rtype: None
        '''

        self.camera.render()


    def instantiate(self, object):
        ''' instantiate a gameObject

        :param object (GameObject): the gameObject to instantiate

        :returns: the instantiated clone
        :rtype: GameObject
        '''

        return self.object_handler.instantiate(object)