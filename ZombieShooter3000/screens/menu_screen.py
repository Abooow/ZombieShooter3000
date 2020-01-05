
import pygame
import random
import event_handler
import sound_manager
import sprite_manager

from screens.screen import Screen
from screens.game_screen import GameScreen


class MenuScreen(Screen):
    
    
    def __init__(self):
        super().__init__()


    def load_content(self):
        '''
        '''
        super().load_content()

        sound_manager.play_song('menu')


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)

        if event_handler.is_key_pressed(pygame.K_RETURN):
            Screen.load_screen(GameScreen())


    def draw(self, surface):
        '''
        '''

        super().draw(surface)

        # draw background img
        surface.blit(sprite_manager.get('menu_screen'), (0, 0))