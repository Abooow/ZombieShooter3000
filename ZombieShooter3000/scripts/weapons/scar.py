
import sound_manager

from screens.screen import Screen
from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon


class Scar(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=100, spread=3, bullets=1000000, magazine_size=50, fire_rate=80)
        
        self.name = 'FN SCAR'
        self.bullet_speed = 810
        self.bullet_max_distance = 1420


    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('scar')
        self.owner.animator.play('scar_shoot')

        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('scar_reload')
        self.owner.animator.play('scar_reload')
