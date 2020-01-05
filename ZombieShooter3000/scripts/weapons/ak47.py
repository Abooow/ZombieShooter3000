
import sound_manager

from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon
from scripts.bullet import Bullet


class Ak47(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=100, spread=1, bullets=1000000, magazine_size=30, fire_rate=130)
        
        self.bullet_speed = 800
        self.bullet_max_distance = 1069


    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('ak47')
        self.owner.animator.play('ak47_shoot')
        
        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('ak47_reload')
        self.owner.animator.play('ak47_reload')
