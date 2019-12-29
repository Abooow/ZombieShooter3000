
import pygame
import math
import random
import event_handler
import surface_change

from screens.screen import Screen
from scripts.blood import Blood
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
    def __init__(self, surface):

        self.objectHandler = ObjectHandler(Vector2(0, 0), Vector2(3024, 1500))
        self.camera = Camera(surface, self.objectHandler, Transform(None), Vector2(1024, 700), Vector2(0, 0))

        super().__init__()
                

    def load_content(self):
        super().load_content()

        self.zombie1 = GameObject(Vector2(100, 100))
        self.zombie1.sprite_renderer.sprite = pygame.image.load('0.png')
        self.zombie1.transform.origin = Vector2(0.5, 0.5)
        self.zombie1.collider.size = Vector2(50, 50)
        self.zombie1.collider.enabled = True


        self.zombies = []
        for i in range(200):
            copy = self.zombie1.copy()

            copy.transform.gameobject = copy
            copy.sprite_renderer.gameobject = copy
            copy.collider.gameobject = copy

            copy.collider.tag = str(i)
            copy.collider.enabled = True
            copy.collider.is_trigger = True
            copy.sprite_renderer.sorting_order = 1
            copy.transform.position = Vector2(random.randint(0, 3024), random.randint(0, 1500))
            
            self.zombies.append(self.objectHandler.instantiate(copy))

        self.zombie1.collider.on_collision_enter = self.on_trigger
        self.zombie1.collider.tag = 'player'
        self.zombie1.sprite_renderer.sorting_order = 2
        self.zombie1.sprite_renderer.color = (255, 0, 0)
        self.objectHandler.instantiate(self.zombie1)


        # --------------------------------------- tilemap

        map = [['grass'] * 50 for i in range(30)]

        for y in range(len(map)):
            for x in range(len(map[y])):
                if random.random() < 0.2:
                    map[y][x] = 'gravel'

        grassTile = Tile('grass', pygame.image.load('grass.png'))
        gravelTile = Tile('gravel', pygame.image.load('gravel.png'))

        tilemap = Tilemap(self.camera, map, [grassTile, gravelTile], Vector2(64, 64), Vector2(), 0)

        self.objectHandler.instantiate(tilemap)

    def on_trigger(self, other):
        self.objectHandler.instantiate(Blood(other.gameobject.transform.position))
        other.gameobject.destroy()

    def update(self, delta_time):
        super().update(delta_time)

        speed = 500 * (delta_time / 1000)

        if event_handler.is_key_down(pygame.K_w):
            self.zombie1.transform.position += Vector2(0, -1) * speed
        if event_handler.is_key_down(pygame.K_s):
            self.zombie1.transform.position += Vector2(0, 1) * speed
        if event_handler.is_key_down(pygame.K_a):
            self.zombie1.transform.position += Vector2(-1, 0) * speed
        if event_handler.is_key_down(pygame.K_d):
            self.zombie1.transform.position += Vector2(1, 0) * speed

        self.camera.transform.position = self.zombie1.transform.position * self.camera.transform.scale - self.camera.size * 0.5

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


        self.zombie1.transform.look_at(self.camera.screen_to_world_point(Vector2.tuple_to_vector2(pygame.mouse.get_pos())))

        for zombie in self.zombies:
            zombie.transform.look_at(self.zombie1.transform.position)
            #zombie.transform.position += zombie.transform.forward()

        self.objectHandler.update(delta_time)


    def draw(self, surface):
        super().draw(surface)

        self.camera.render()