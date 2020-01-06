
import pygame
import random
import sprite_manager

from screens.screen import Screen
from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Blood(GameObject):


    total_objects = 0


    def instantiate(position):
        '''
        '''

        if Blood.total_objects < 40:
            Screen.get_current_screen().object_handler.instantiate(Blood(position))
            Blood.total_objects += 1


    def __init__(self, position):
        super().__init__(position=position, rotation=random.randint(0, 360), origin=Vector2(0.5, 0.5))

        self.add_sprite_renderer(sprite=sprite_manager.get('blood0'), sorting_order=1)
        self.collider = None
        self._alpha = 255


    def update(self, delta_time):
        super().update(delta_time)

        self._alpha -= 25 * (delta_time / 1000)
        self._alpha = (self._alpha if self._alpha > 0 else 0)
        self.sprite_renderer.color = (255, 255, 255, int(self._alpha))

        if self._alpha <= 10:
            Blood.total_objects -= 1
            self.destroy()