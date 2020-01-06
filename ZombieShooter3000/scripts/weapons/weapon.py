

from scripts.item import Item
from scripts.bullet import Bullet
from screens.screen import Screen
from framework.vector2 import Vector2


class Weapon(Item):
    '''
    '''


    def __init__(self, owner, damage, spread, bullets, magazine_size, fire_rate, position=Vector2(0, 0), bullet_offset=Vector2(0, 0), bullet_speed=500, bullet_max_distance=700):
        '''
        '''

        super().__init__(position=position, scale=Vector2(1, 1), hitbox=Vector2(0, 0))

        self.owner = owner
        self.bullet_offset = bullet_offset
        self.bullet_speed = bullet_speed
        self.bullet_max_distance = bullet_max_distance

        self.damage = damage
        self.spread = spread
        self.bullets = bullets-1
        self.magazine_size = magazine_size
        self.fire_rate = fire_rate

        self.name = 'unknown'

        self.can_shoot = True
        self.reloading = False

        self._timer = 0


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)

        if not self.can_shoot and not self.reloading:
            self._timer += delta_time

            if self._timer >= self.fire_rate:
                self._timer = 0
                self.can_shoot = True


    def shoot(self):
        '''
        '''

        if self.bullets != 0 and self.can_shoot and not self.reloading:
            self.on_shooting()


    def on_shooting(self):
        '''
        '''

        # spawn bullet
        Screen.get_current_screen().instantiate(Bullet(self, self.bullet_speed, self.bullet_max_distance))
         
        if self.bullets != 0 and self.bullets % self.magazine_size == 0:
            self.reload()
            self.bullets -= 1
        elif self.bullets > 0:
            self.bullets -= 1

        self.can_shoot = False


    def reload(self):
        '''
        '''

        self.can_shoot = False
        self.reloading = True


    def on_reload_done(self):
        '''
        '''

        self.reloading = False