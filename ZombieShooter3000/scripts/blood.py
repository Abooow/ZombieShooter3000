
import pygame
import random

from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Blood(GameObject):

    def __init__(self, position):
        super().__init__(position=position)

        self.transform.rotation = random.randint(0, 360)
        self.transform.origin = Vector2(0.5, 0.5)

        self.sprite_renderer.sprite = pygame.image.load('content/sprites/effects/blood0.png')

        self.collider = None

        self.alpha = 255


    def update(self, delta_time):
        super().update(delta_time)

        self.alpha -= 0.4
        self.sprite_renderer.color = (255, 255, 255, int(self.alpha))

        if self.alpha <= 0:
            self.destroy()