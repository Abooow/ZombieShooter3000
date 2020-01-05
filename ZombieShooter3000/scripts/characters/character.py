
import random

from scripts.blood import Blood
from screens.screen import Screen
from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Character(GameObject):
    '''
    '''


    def __init__(self, position=Vector2(0, 0), rotation=0, scale=Vector2(1, 1), origin=Vector2(0, 0), max_health=100, speed=10):
        '''
        :param position (Vector2): the position of this Character
        :param rotation (int): the rotation of this Character
        :param scale (Vector2): the scale of this Character
        :param origin (Vector2): the origin of this Character, (0, 0) is the top left and (1, 1) is the bottom right
        :param max_health (int): the max health of this Character
        '''

        super().__init__(position, rotation, scale, origin)

        self.speed = speed
        self.health = max_health
        self.max_health = max_health
        self.is_dead = False

        self._alpha = 255


    def update(self, delta_time):
        ''' updates this Character

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        super().update(delta_time)

        if self.is_dead:
            self._alpha -= 80 * (delta_time / 1000)
            self._alpha = (self._alpha if self._alpha > 0 else 0)
            self.sprite_renderer.color = (255, 255, 255, self._alpha)

            if self._alpha <= 10:
                self.destroy()


    def die(self) -> None:
        '''

        :returns: NoReturn
        :rtype: None
        '''

        self.is_dead = True
        self.collider = None

        Blood.instantiate(self.transform.position)


    def take_damage(self, damage) -> None:
        '''

        :param damage (float): 
        
        :returns: NoReturn
        :rtype: None
        '''

        if damage > 0 and random.random() < 0.25:
            Blood.instantiate(self.transform.position)

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()


    def attack(self) -> None:
        '''
        
        :returns: NoReturn
        :rtype: None
        '''

        pass