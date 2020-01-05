
import pygame
import event_handler

from screens.screen import Screen
from framework.vector2 import Vector2
from scripts.characters.character import Character


class Enemy(Character):
    '''
    '''

    def __init__(self, position=Vector2(0, 0), scale=Vector2(1, 1), hitbox=Vector2(50, 50), max_health=100, damage=10, speed=20, attack_range=80):
        '''
        :param position (Vector2): the position of this Character
        :param rotation (int): the rotation of this Character
        :param scale (Vector2): the scale of this Character
        :param origin (Vector2): the origin of this Character
        :param max_health (int): the max health of this Character
        '''

        super().__init__(position=position, rotation=0, scale=scale, origin=Vector2(0.5, 0.5), max_health=max_health, speed=speed)
        
        self.add_collider('enemy', hitbox, Vector2(0, 0), False, False)
        self.collider.on_trigger_enter = self.on_trigger_enter

        self.damage = damage
        self.attack_range = attack_range


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)


    def die(self):
        '''
        '''

        super().die()


    def attack(self):
        '''
        '''

        super().attack()


    def take_damage(self, damage):
        '''
        '''

        super().take_damage(damage)


    def on_trigger_enter(self, other):
        if other.collider.tag == 'bullet':
            self.take_damage(other.damage)
            other.destroy()