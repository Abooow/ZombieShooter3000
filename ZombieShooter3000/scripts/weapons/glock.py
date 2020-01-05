
import sound_manager

from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon
from scripts.bullet import Bullet


class Glock(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=35, spread=3, bullets=1000000, magazine_size=12, fire_rate=350)
    
        self.bullet_max_distance = 750

    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('glock')
        self.owner.animator.play('glock_shoot')
        
        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('glock_reload')
        self.owner.animator.play('glock_reload')