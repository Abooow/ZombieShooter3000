
import pygame
import random
import math
import sprite_manager

from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Bullet(GameObject):
    '''
    '''

    def __init__(self, weapon, speed=300, max_distance=700):

        rotation = weapon.owner.transform.rotation
        position = weapon.owner.transform.position
        point = weapon.bullet_offset + position

        c = -math.cos(rotation/57.295);
        s = -math.sin(rotation/57.295);

        # translate point back to origin:
        point.x -= position.x;
        point.y -= position.y;

        # rotate point
        xnew = point.x * s - point.y * c;
        ynew = point.x * c + point.y * s;

        # translate point back:
        point.x = xnew + position.x;
        point.y = ynew + position.y;

        super().__init__(position=point, 
                         rotation=rotation, 
                         scale=Vector2(1, 1), 
                         origin=Vector2(0.5, 0.5))

        self.transform.rotation += (random.random() * 2 - 1) * weapon.spread

        self.damage = weapon.damage
        self.speed = speed
        self.max_distance = max_distance

        self.add_sprite_renderer(sprite=sprite_manager.get('bullet'), sorting_order=2)
        self.add_collider('bullet', Vector2(50, 50), Vector2(0, 0), True, True)



    def update(self, delta_time):
        super().update(delta_time)

        distance = self.speed * (delta_time/1000)
        self.transform.position += self.transform.forward() * distance

        self.max_distance -= distance
        if self.max_distance <= 0:
            self.destroy()