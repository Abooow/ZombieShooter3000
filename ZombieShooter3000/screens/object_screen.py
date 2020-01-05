
import pygame
import math
import sys
import random
import event_handler
import surface_change
import framework.animation as anim

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
    def __init__(self):

        #self.objectHandler = ObjectHandler(Vector2(0, 0), Vector2(3024, 1500))
        #self.camera = Camera(surface, self.objectHandler, Transform(None), Vector2(1024, 700), Vector2(0, 0))

        super().__init__()
                

    def load_content(self):
        super().load_content()

        #############################      WALK ANIMATION      ##############################
        walk_anim_frames = [pygame.image.load(f'content/sprites/animations/zombie/walk/frame{i}.png') for i in range(5)]
        test_anim_frames = [pygame.image.load(f'content/sprites/animations/zombie/attack/frame{i}.png') for i in range(8)]


        walk_anim = anim.Animation(walk_anim_frames)
        test_anim = anim.Animation(test_anim_frames)

        ######################################################################################

        self.zombie1 = GameObject(Vector2(100, 100), origin=Vector2(0.5, 0.5))
        self.zombie1.add_collider(size=Vector2(50, 50))
        self.zombie1.add_sprite_renderer(sprite=walk_anim_frames[0])
        self.zombie1.add_animator()

        self.zombie1.animator.add_animation('walk', walk_anim)
        self.zombie1.animator.add_animation('test', test_anim)

        self.zombies = []
        for i in range(100):
            copy = self.zombie1.copy()

            copy.collider.tag = str(i)
            copy.collider.is_static = True
            copy.sprite_renderer.sorting_order = 1
            copy.transform.position = Vector2(random.randint(0, 3024), random.randint(0, 1500))
            
            self.zombies.append(self.instantiate(copy))

        
        self.zombie1.collider.on_collision_enter = self.on_trigger
        self.zombie1.collider.tag = 'player'
        self.zombie1.sprite_renderer.sorting_order = 2
        self.instantiate(self.zombie1)

        # --------------------------------------- tilemap

        map = [['grass'] * 50 for i in range(30)]

        for y in range(len(map)):
            for x in range(len(map[y])):
                if random.random() < 0.2:
                    map[y][x] = 'gravel'

        grassTile = Tile('grass', pygame.image.load('grass.png'))
        gravelTile = Tile('gravel', pygame.image.load('gravel.png'))

        tilemap = Tilemap(self.camera, map, [grassTile, gravelTile], Vector2(64, 64), Vector2(), 0)

        #self.objectHandler.instantiate(tilemap)


    def on_trigger(self, other):
        self.instantiate(Blood(other.transform.position))
        other.destroy()


    def update(self, delta_time):
        
        if event_handler.is_mouse_pressed(1):
            if self.zombie1.animator._current_animation_name == 'walk':
                self.zombie1.animator.play('test')
            else:
                self.zombie1.animator.play('walk')

        if event_handler.is_key_down(pygame.K_q):
            self.camera.zoom(0.99, self.camera.world_to_screen_point(self.zombie1.transform.position))
        if event_handler.is_key_down(pygame.K_e):
            self.camera.zoom(1.01, self.camera.world_to_screen_point(self.zombie1.transform.position))

        if event_handler.is_key_down(pygame.K_z):
            self.camera.transform.rotation -= 1
        if event_handler.is_key_down(pygame.K_c):
            self.camera.transform.rotation += 1


        for zombie in self.zombies:
            zombie.transform.look_at(self.zombie1.transform.position)
            zombie.transform.position += zombie.transform.forward()


        super().update(delta_time)