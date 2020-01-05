
import pygame
import random
import utils
import event_handler
import sound_manager
import sprite_manager

from screens.screen import Screen
from framework.vector2 import Vector2


class DeathScreen(Screen):
    
    
    def __init__(self, last):
        super().__init__()
                
        self.last = last


    def load_content(self):
        '''
        '''
        super().load_content()


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)


        if event_handler.is_key_pressed(pygame.K_RETURN):
            Screen.get_last_screen().load_content()
            Screen.load_screen(Screen.get_last_screen())


    def draw(self, surface):
        '''
        '''

        #super().draw(surface)

        self.last.draw(surface)

        # draw background img
        surface.blit(sprite_manager.get('death_screen'), (0, 0))
        # wave text
        utils.draw_font(surface, f'you survived {self.last._current_wave - 1} waves', (255, 255, 255), (395, 240), size=24)