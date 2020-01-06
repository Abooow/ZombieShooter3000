
import sound_manager

from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon
from scripts.bullet import Bullet


class Uzi(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=20, spread=5, bullets=1000000, magazine_size=50, fire_rate=100)
        
        self.name = 'UZI'
        self.bullet_speed = 720


    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('uzi')
        self.owner.animator.play('uzi_shoot')
        
        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('uzi_reload')
        self.owner.animator.play('uzi_reload')