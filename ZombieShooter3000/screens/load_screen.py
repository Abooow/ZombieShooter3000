
import pygame
import utils
import sound_manager
import sprite_manager
import animation_manager

from screens.screen import Screen
from framework.animation import Animation
from scripts.enemy_wave import EnemyWave


class LoadScreen(Screen):
    '''
    '''


    def __init__(self):
        super().__init__()


    def load_content(self):
        super().load_content()

        self.load_sounds()
        self.load_sprites()
        self.load_animations()

        # create 100 waves
        utils.enemy_waves = [EnemyWave(i).enemies for i in range(100)]
        

    def load_sounds(self) -> None:
        '''
        '''

        # effects
        # weapons
        sound_manager.add_effect('glock', 'content/sounds/effects/weapons/glock.wav')
        sound_manager.add_effect('uzi', 'content/sounds/effects/weapons/uzi.wav')
        sound_manager.add_effect('shotgun', 'content/sounds/effects/weapons/shotgun.wav')
        sound_manager.add_effect('pump_shotgun', 'content/sounds/effects/weapons/pump_shotgun.wav')
        sound_manager.add_effect('ak47', 'content/sounds/effects/weapons/ak47.wav')
        sound_manager.add_effect('scar', 'content/sounds/effects/weapons/scar.wav')
        sound_manager.add_effect('glock_reload', 'content/sounds/effects/weapons/glock_reload.wav')
        sound_manager.add_effect('uzi_reload', 'content/sounds/effects/weapons/uzi_reload.wav')
        sound_manager.add_effect('shotgun_reload', 'content/sounds/effects/weapons/shotgun_reload.wav')
        sound_manager.add_effect('pump_shotgun_reload', 'content/sounds/effects/weapons/pump_shotgun_reload.wav')
        sound_manager.add_effect('ak47_reload', 'content/sounds/effects/weapons/ak47_reload.wav')
        sound_manager.add_effect('scar_reload', 'content/sounds/effects/weapons/scar_reload.wav')
        # other
        sound_manager.add_effect('new_wave', 'content/sounds/effects/new_wave.wav')
        sound_manager.add_effect('player_hurt', 'content/sounds/effects/player_hurt.wav')
        sound_manager.add_effect('player_death', 'content/sounds/effects/player_death.wav')
        sound_manager.add_effect('zombie_hurt', 'content/sounds/effects/zombie_hurt.wav')
        sound_manager.add_effect('zombie0', 'content/sounds/effects/zombie0.wav')
        sound_manager.add_effect('zombie1', 'content/sounds/effects/zombie1.wav')

        # songs
        sound_manager.add_song('menu', 'content/sounds/songs/menu.mp3')
        sound_manager.add_song('game', 'content/sounds/songs/game.mp3')


    def load_sprites(self) -> None:
        '''
        '''

        # effects
        sprite_manager.add('blood0', 'content/sprites/effects/blood0.png')
        sprite_manager.add('bullet', 'content/sprites/effects/bullet.png')
        # tiles
        sprite_manager.add('grass', 'content/sprites/tiles/grass.png')
        sprite_manager.add('gravel', 'content/sprites/tiles/gravel.png')
        # GUI
        sprite_manager.add('menu_screen', 'content/sprites/menu_screen.png')
        sprite_manager.add('death_screen', 'content/sprites/death_screen.png')
        sprite_manager.add('vignette', 'content/sprites/vignette.png')


    def load_animations(self) -> None:
        '''
        '''

        # ----------- Zombie
        # walk
        frames = [pygame.image.load(f'content/sprites/animations/zombie/walk/frame{i}.png') for i in range(17)]
        animation = Animation(frames=frames, framerate=15, loop=True)
        animation_manager.add('zombie_walk', animation)
        # attack
        frames = [pygame.image.load(f'content/sprites/animations/zombie/attack/frame{i}.png') for i in range(8)]
        animation = Animation(frames=frames, framerate=60, loop=False)
        animation_manager.add('zombie_attack', animation)

        # ----------- Player
        # glock idle
        frames = [pygame.image.load(f'content/sprites/animations/player/glock/idle/frame{i}.png') for i in range(7)]
        animation = Animation(frames=frames, framerate=12, loop=True)
        animation_manager.add('glock_idle', animation)
        # glock walk
        frames = [pygame.image.load(f'content/sprites/animations/player/glock/walk/frame{i}.png') for i in range(10)]
        animation = Animation(frames=frames, framerate=12, loop=True)
        animation_manager.add('glock_walk', animation)
        # glock shoot
        frames = [pygame.image.load(f'content/sprites/animations/player/glock/shoot/frame{i}.png') for i in range(3)]
        animation = Animation(frames=frames, framerate=25, loop=False)
        animation_manager.add('glock_shoot', animation)
        # glock reload
        frames = [pygame.image.load(f'content/sprites/animations/player/glock/reload/frame{i}.png') for i in range(8)]
        animation = Animation(frames=frames, framerate=12, loop=False)
        animation_manager.add('glock_reload', animation)