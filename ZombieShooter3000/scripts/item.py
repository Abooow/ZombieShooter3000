
from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Item(GameObject):
    '''
    '''

    def __init__(self, position=Vector2(0, 0), scale=Vector2(1, 1), hitbox=Vector2(50, 50)):
        '''
        '''

        super().__init__(position=position, rotation=0, scale=scale, origin=Vector2(0.5, 0.5))

        if hitbox != Vector2(0, 0):
            self.add_collider('item', hitbox, Vector2(0, 0), False, True)
            self.collider.on_collider_enter = self.on_pick_up


    def update(self, delta_time):
        super().update(delta_time)


    def on_pick_up():
        '''
        '''

        self.collider = None