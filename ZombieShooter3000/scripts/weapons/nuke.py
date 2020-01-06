
import sound_manager

from screens.screen import Screen
from framework.vector2 import Vector2
from scripts.weapons.weapon import Weapon
from scripts.bullet import Bullet


class Nuke(Weapon):
    '''
    '''


    def __init__(self, owner):
        super().__init__(owner=owner, bullet_offset=Vector2(47, 15), damage=1000, spread=180, bullets=1000000, magazine_size=1000000, fire_rate=1000)
        
        self.name = 'NUKE'
        self.bullet_speed = 500
        self.bullet_max_distance = 2000


    def update(self, delta_time):
        super().update(delta_time)


    def on_shooting(self):
        '''
        '''
        
        sound_manager.play_effect('shotgun')
        self.owner.animator.play('nuke_shoot')

        # spawn bullets
        for i in range(359):
            Screen.get_current_screen().instantiate(Bullet(self, self.bullet_speed, self.bullet_max_distance))
        
        super().on_shooting()


    def reload(self):
        '''
        '''

        super().reload()

        sound_manager.play_effect('shotgun_reload')
        self.owner.animator.play('nuke_reload')
