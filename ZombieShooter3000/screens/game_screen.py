
import pygame
import random
import utils
import event_handler
import sound_manager
import sprite_manager

from screens.screen import Screen
from framework.tile import Tile
from framework.tilemap import Tilemap
from framework.vector2 import Vector2
from scripts.enemy_spawner import EnemySpawner
from scripts.characters.player import Player
from scripts.characters.zombie import Zombie
from scripts.characters.big_zombie import BigZombie


class GameScreen(Screen):
    
    
    def __init__(self):
        super().__init__()
                

    def load_content(self):
        super().load_content()

        sound_manager.play_song('game')

        self.player = Player(Vector2(928, 928))
        self.instantiate(self.player)
        
        # create enemy spawner
        enemy_spawner = EnemySpawner(utils.enemy_waves, self.player)
        enemy_spawner.on_new_wave = self.on_new_wave
        self.instantiate(enemy_spawner)

        # map
        map = [['grass'] * 30 for i in range(30)]
        for y in range(len(map)):
            for x in range(len(map[y])):
                if (random.random() < 0.2 or 
                    x == 0 or x == 28 or
                    y == 0 or y == 28):
                    map[y][x] = 'gravel'

        grassTile = Tile('grass', sprite_manager.get('grass'))
        gravelTile = Tile('gravel', sprite_manager.get('gravel'))

        tilemap = Tilemap(self.camera, map, [grassTile, gravelTile], Vector2(64, 64), Vector2(), 0)
        self.instantiate(tilemap)


        self._wave_text_timer = 0
        self._current_wave = 0
        

    def on_new_wave(self, wave):
        '''
        '''

        sound_manager.play_effect('new_wave')

        self._wave_text_timer = 4500
        self._current_wave = wave


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)

        if self._wave_text_timer > 0:
            self._wave_text_timer -= delta_time


    def draw(self, surface):
        '''
        '''

        super().draw(surface)

        #surface.blit(sprite_manager.get('vignette'), (0, 0))

        if self._wave_text_timer > 0:
            utils.draw_font(surface, f'WAVE {self._current_wave}', (255, 255, 255), (433, 97), size=40)
        else:
            utils.draw_font(surface, f'{self._current_wave}', (255, 255, 255), (5, 5), size=20)

        # ui
        # health
        pygame.draw.rect(surface, (20, 20, 20), (0, 680, 1024, 20))
        healthbar_width = (self.player.health / self.player.max_health) * 1024
        pygame.draw.rect(surface, (255, 50, 50), (0, 680, healthbar_width, 20))

        utils.draw_font(surface, 'press 1-8 to switch weapons', (255, 255, 255), (408, 680), size=15)