
import pygame
import math
import random
import event_handler
import surface_change

from screens.screen import Screen
from framework.rectangle import Rectangle
from framework.vector2 import Vector2
from framework.camera import Camera
from framework.tile import Tile
from framework.tilemap import Tilemap
from framework.gameobject import GameObject
from framework.object_handler import ObjectHandler
from framework.components.transform import Transform
from framework.components.sprite_renderer import SpriteRenderer


class TestScreen(Screen):
    def __init__(self):
        super().__init__()
                

    def load_content(self):
        super().load_content()

        self.objectHandler = ObjectHandler()
        self.camera = Camera(Transform(None), Vector2(1024, 700), Vector2(0, 0), self.objectHandler)

        self.zombie1 = GameObject(Vector2(100, 100))
        self.zombie1.sprite_renderer.sprite = pygame.image.load('0.png')
        self.zombie1.transform.origin = Vector2(0.5, 0.5)

        self.zombies = []

        for i in range(100):
            copy = self.zombie1.copy()
            copy.sprite_renderer.sorting_order = 1
            copy.transform.position = Vector2(random.randint(0, 3024), random.randint(0, 1500))
            self.zombies.append(self.objectHandler.instantiate(copy))


        self.zombie1.sprite_renderer.sorting_order = 2
        self.zombie1.sprite_renderer.color = (255, 0, 0)
        self.objectHandler.instantiate(self.zombie1)


        # --------------------------------------- tilemap

        map = [['grass'] * 100 for i in range(100)]

        for y in range(len(map)):
            for x in range(y):
                if random.random() < 0.2:
                    map[x][y] = 'gravel'

        grassTile = Tile('grass', pygame.image.load('grass.png'))
        gravelTile = Tile('gravel', pygame.image.load('gravel.png'))

        self.tilemap = Tilemap(self.camera, map, [grassTile, gravelTile], Vector2(32, 32), Vector2(), 0)



    def update(self, delta_time):
        super().update(delta_time)

        if event_handler.is_key_down(pygame.K_UP):
            self.zombie1.transform.position += self.zombie1.transform.forward() * 10

        if event_handler.is_key_down(pygame.K_w):
            self.camera.transform.position.y -= 10
        if event_handler.is_key_down(pygame.K_s):
            self.camera.transform.position.y += 10
        if event_handler.is_key_down(pygame.K_a):
            self.camera.transform.position.x -= 10
        if event_handler.is_key_down(pygame.K_d):
            self.camera.transform.position.x += 10

        if event_handler.is_key_down(pygame.K_q):
            self.camera.zoom(0.99, self.camera.world_to_screen_point(self.zombie1.transform.position))
        if event_handler.is_key_down(pygame.K_e):
            self.camera.zoom(1.01, self.camera.world_to_screen_point(self.zombie1.transform.position))

        if event_handler.is_key_down(pygame.K_z):
            self.camera.transform.rotation -= 1
        if event_handler.is_key_down(pygame.K_c):
            self.camera.transform.rotation += 1

        if event_handler.is_key_pressed(pygame.K_SPACE):
            self.zombie1.destroy()


        self.zombie1.transform.look_at(Transform(None, 
                                                 self.camera.screen_to_world_point(Vector2.tuple_to_vector2(pygame.mouse.get_pos()))))

        for zombie in self.zombies:
            zombie.transform.look_at(self.zombie1.transform)
            #zombie.transform.position += zombie.transform.forward()

        #self.objectHandler.update(delta_time)


    def draw(self, surface):
        super().draw(surface)

        self.tilemap.draw(surface)
        self.camera.render(surface)