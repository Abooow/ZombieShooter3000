
import pygame
import random
import event_handler
import sound_manager

from screens.screen import Screen
from framework.tile import Tile
from framework.tilemap import Tilemap
from framework.vector2 import Vector2
from scripts.characters.player import Player
from scripts.characters.zombie import Zombie
from scripts.characters.big_zombie import BigZombie
from scripts.enemy_wave import EnemyWave
from scripts.enemy_spawner import EnemySpawner


class NewScreen(Screen):
    
    
    def __init__(self):
        super().__init__()
                

    def load_content(self):
        super().load_content()

        sound_manager.play_song('game')

        self.player = Player(Vector2(928, 928))
        self.instantiate(self.player)
        

        #for i in range(20):
        #    zombie = Zombie(self.player, Vector2(random.randint(0, 1856), random.randint(0, 1856)))
        #    self.instantiate(zombie)

        #for i in range(5):
        #    zombie = BigZombie(self.player, Vector2(random.randint(0, 1856), random.randint(0, 1856)))
        #    self.instantiate(zombie)

        # create enemy spawner
        waves = [EnemyWave(i).enemies for i in range(100)]
        enemy_spawner = EnemySpawner(waves, self.player)
        enemy_spawner.on_new_wave = self.on_new_wave

        self.instantiate(enemy_spawner)

        # map
        map = [['grass'] * 30 for i in range(30)]
        for y in range(len(map)):
            for x in range(len(map[y])):
                if random.random() < 0.2:
                    map[y][x] = 'gravel'

        grassTile = Tile('grass', pygame.image.load('grass.png'))
        gravelTile = Tile('gravel', pygame.image.load('gravel.png'))

        tilemap = Tilemap(self.camera, map, [grassTile, gravelTile], Vector2(64, 64), Vector2(), 0)

        self.instantiate(tilemap)
        

    def on_new_wave(self, wave):
        print(f'Wave {wave}')


    def update(self, delta_time):
        

        super().update(delta_time)