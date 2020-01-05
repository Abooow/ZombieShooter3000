
import sound_manager

from screens.screen import Screen
from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon
from scripts.bullet import Bullet


class Shotgun(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=30, spread=12, bullets=1000000, magazine_size=1, fire_rate=450)
        
        self.bullet_speed = 700
        self.bullet_max_distance = 760


    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('shotgun')
        self.owner.animator.play('shotgun_shoot')

        # spawn bullets
        for i in range(20):
            Screen.get_current_screen().instantiate(Bullet(self, self.bullet_speed, self.bullet_max_distance))
        
        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('shotgun_reload')
        self.owner.animator.play('shotgun_reload')
