
import pygame
import random
import sound_manager
import animation_manager

from screens.screen import Screen
from framework.vector2 import Vector2
from scripts.characters.enemy import Enemy


class Zombie(Enemy):
    '''
    '''


    def __init__(self, player, position=Vector2(0, 0), scale=Vector2(1, 1)):
        '''
        :param position (Vector2): the position of this Character
        :param rotation (int): the rotation of this Character
        :param scale (Vector2): the scale of this Character
        :param origin (Vector2): the origin of this Character
        :param max_health (int): the max health of this Character
        '''

        super().__init__(position=position, scale=scale, hitbox=Vector2(50, 50), max_health=100, damage=20, speed=60, attack_range=100)

        self.player = player
        self.add_sprite_renderer(sorting_order=3)
        self.collider.tag = 'zombie'

        self.add_animator()
        self.animator.add_animation('walk', animation_manager.get('zombie_walk'))
        self.animator.add_animation('attack', animation_manager.get('zombie_attack'))
        self.animator.add_animation('dead', animation_manager.get('zombie_attack'))

        self.animator.animations['attack'].on_done = self.attack

        self.attack = False


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)

        if random.random() < 0.0007:
            sound_manager.play_effect('zombie1')

        if not self.is_dead:
            speed = self.speed * (delta_time / 1000)
            self.transform.look_at(self.player.transform.position)

            # get distance between zombie and player
            dist = (self.transform.position - self.player.transform.position).length()

            # walk if dist >= 20
            if dist >= 10:
                self.transform.position += self.transform.forward() * speed

            # attack if dist <= 80
            if dist <= self.attack_range and not self.attack:
                self.attack = True
                self.animator.play('attack')


    def die(self):
        '''
        '''

        super().die()
        self.animator.play('dead')
        sound_manager.play_effect('zombie_hurt')


    def attack(self):
        '''
        '''

        super().attack()

        self.attack = False
        self.animator.play('walk')

        # get distance between zombie and player
        dist = (self.transform.position - self.player.transform.position).length()
        if dist <= self.attack_range:
            self.player.take_damage(self.damage)