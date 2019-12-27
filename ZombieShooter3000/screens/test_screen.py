
import pygame
import math
import random
import event_handler
import surface_change

from screens.screen import Screen
from framework.rectangle import Rectangle
from framework.vector2 import Vector2
from framework.components.transform import Transform


class TestScreen(Screen):
    def __init__(self):
        super().__init__()
                

    def load_content(self):
        super().load_content()

        self.player = Transform(None, position=Vector2(512, 350))
        self.enemy = Transform(None)

        self.img = pygame.image.load('0.png')


    def update(self, delta_time):
        super().update(delta_time)

        self.enemy.position = Vector2.tuple_to_vector2(pygame.mouse.get_pos())

        self.player.look_at(self.enemy)


    def draw(self, surface):
        super().draw(surface)

        img = pygame.transform.rotate(self.img, self.player.rotation + 90)
        pos = self.player.position.to_tuple()

        og_size = self.img.get_rect().size
        new_size = img.get_rect().size

        diff = new_size[0] * 0.5, new_size[1] * 0.5

        surface.blit(img, (pos[0] - diff[0], pos[1] - diff[1]))
        pygame.draw.rect(surface, (255, 0, 0), (self.player.position.x, self.player.position.y, 10, 10))
