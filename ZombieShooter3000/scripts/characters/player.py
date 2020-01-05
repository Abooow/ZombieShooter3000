
import pygame
import utils
import event_handler
import animation_manager
import sound_manager

from screens.screen import Screen
from screens.death_screen import DeathScreen
from framework.vector2 import Vector2
from framework.gameobject import GameObject
from scripts.characters.character import Character
from scripts.weapons.pump_shotgun import PumpShotgun
from scripts.weapons.shotgun import Shotgun
from scripts.weapons.glock import Glock
from scripts.weapons.ak47 import Ak47
from scripts.weapons.uzi import Uzi


class Player(Character):
    '''
    '''

    def __init__(self, position=Vector2(0, 0), scale=Vector2(1, 1), max_health=100):
        '''
        :param position (Vector2): the position of this Character
        :param rotation (int): the rotation of this Character
        :param scale (Vector2): the scale of this Character
        :param origin (Vector2): the origin of this Character
        :param max_health (int): the max health of this Character
        '''

        super().__init__(position=position, rotation=0, scale=scale, origin=Vector2(0.5, 0.5), max_health=max_health)

        self.speed = 269

        self.add_sprite_renderer(sorting_order=4)
        self.add_collider(tag='player', size=Vector2(50, 50))  

        self.weapons = [Glock(self), Uzi(self), Shotgun(self), PumpShotgun(self), Ak47(self)]
        self.current_gun = self.weapons[2]

        self.add_animator()
        # glock animations
        self.animator.add_animation('glock_idle', animation_manager.get('glock_idle'))
        self.animator.add_animation('glock_walk', animation_manager.get('glock_walk'))
        self.animator.add_animation('glock_shoot', animation_manager.get('glock_shoot'))
        self.animator.add_animation('glock_reload', animation_manager.get('glock_reload'))
        # uzi animations
        self.animator.add_animation('uzi_shoot', animation_manager.get('glock_shoot'))
        self.animator.add_animation('uzi_reload', animation_manager.get('glock_reload'))
        # shotgun animations
        self.animator.add_animation('shotgun_shoot', animation_manager.get('glock_shoot'))
        self.animator.add_animation('shotgun_reload', animation_manager.get('glock_reload'))
        # pump shotgun animations
        self.animator.add_animation('pump_shotgun_shoot', animation_manager.get('glock_shoot'))
        self.animator.add_animation('pump_shotgun_reload', animation_manager.get('glock_reload'))
        # ak47 animations
        self.animator.add_animation('ak47_shoot', animation_manager.get('glock_shoot'))
        self.animator.add_animation('ak47_reload', animation_manager.get('glock_reload'))
        
        # glock
        self.animator.animations['glock_shoot'].on_done = self._shoot_done
        self.animator.animations['glock_reload'].on_done = self.weapons[0].on_reload_done
        # uzi
        self.animator.animations['uzi_shoot'].on_done = self._shoot_done
        self.animator.animations['uzi_reload'].on_done = self.weapons[1].on_reload_done
        # shotgun
        self.animator.animations['shotgun_shoot'].on_done = self._shoot_done
        self.animator.animations['shotgun_reload'].on_done = self.weapons[2].on_reload_done
        # pump shotgun
        self.animator.animations['pump_shotgun_shoot'].on_done = self._shoot_done
        self.animator.animations['pump_shotgun_reload'].on_done = self.weapons[3].on_reload_done
        # ak47
        self.animator.animations['ak47_shoot'].on_done = self._shoot_done
        self.animator.animations['ak47_reload'].on_done = self.weapons[4].on_reload_done


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)

        if self.is_dead:
            return

        # update current gun
        self.current_gun.update(delta_time)

        # handle movement
        self._movement(delta_time)

        # shoot
        if event_handler.is_mouse_down(1):
            self.attack()

        # switch weapons
        self._swith_weapons()

        # get the camera in current screen
        camera = Screen.get_current_screen().camera

        # look at mouse
        self.transform.look_at(camera.screen_to_world_point(Vector2.tuple_to_vector2(pygame.mouse.get_pos())))

        # make the camera follow player
        self._camera_follow(camera)


    def die(self):
        '''
        '''

        super().die()

        Screen.load_screen(DeathScreen(Screen.get_current_screen()))
        sound_manager.play_effect('player_death')


    def attack(self):
        '''
        '''

        super().attack()
        self.current_gun.shoot()


    def take_damage(self, damage):
        '''
        '''

        super().take_damage(damage)
        sound_manager.play_effect('player_hurt')


    def _shoot_done(self):
        self.animator.play('glock_walk')


    def _movement(self, delta_time):
        ''' move the player

        :returns: NoReturn
        :rtype: None
        '''

        speed = self.speed * (delta_time / 1000)
        direction = Vector2(0, 0)
        if event_handler.is_key_down(pygame.K_w):
            direction.y += -1
        if event_handler.is_key_down(pygame.K_s):
            direction.y += 1
        if event_handler.is_key_down(pygame.K_a):
            direction.x += -1
        if event_handler.is_key_down(pygame.K_d):
            direction.x += 1
        # update position
        self.transform.position += direction * speed
        
        # constrain player position
        if self.transform.position.x <= 0:
            self.transform.position.x = 0
        elif self.transform.position.x >= utils.world_size[0]:
            self.transform.position.x = utils.world_size[0]
        
        if self.transform.position.y <= 0:
            self.transform.position.y = 0
        elif self.transform.position.y >= utils.world_size[1]:
            self.transform.position.y = utils.world_size[1]


    def _swith_weapons(self):
        '''
        '''

        if event_handler.is_key_down(pygame.K_1):   # glock
            self.current_gun = self.weapons[0]
        elif event_handler.is_key_down(pygame.K_2): # uzi
            self.current_gun = self.weapons[1]
        elif event_handler.is_key_down(pygame.K_3): # shotgun
            self.current_gun = self.weapons[2]
        elif event_handler.is_key_down(pygame.K_4): # pump shotgun
            self.current_gun = self.weapons[3]
        elif event_handler.is_key_down(pygame.K_5): # ak47
            self.current_gun = self.weapons[4]


    def _camera_follow(self, camera):
        ''' makes the camera follow the player

        :returns: NoReturn
        :rtype: None
        '''

        camera.transform.position = self.transform.position * camera.transform.scale - camera.size * 0.5
        
        # constrain camera position
        if camera.transform.position.x <= 0:
            camera.transform.position.x = 0
        elif camera.transform.position.x >= utils.world_size[0] - camera.size.x:
            camera.transform.position.x = utils.world_size[0] - camera.size.x
        
        if camera.transform.position.y <= 0:
            camera.transform.position.y = 0
        elif camera.transform.position.y >= utils.world_size[1] - camera.size.y:
            camera.transform.position.y = utils.world_size[1] - camera.size.y