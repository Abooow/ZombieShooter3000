
from framework.vector2 import Vector2
from framework.components.transform import Transform
from framework.components.sprite_renderer import SpriteRenderer


class GameObject():
    ''' the base class for all gameObjects
    '''


    def __init__(self, position=Vector2()):
        '''
        :param position (Vector2): 
        '''

        # the Transform of this GameObject
        self.transform = Transform(self, position)
        # the SpritrRenderer of this GameObject
        self.sprite_renderer = SpriteRenderer(self)
        self._flagged_as_destroy = False


    def update(self, delta_time) -> None:
        ''' updates this gameObject

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        pass


    def destroy(self) -> None:
        ''' destroys this gameObject

        :returns: NoReturn
        :rtype: None
        '''

        self._flagged_as_destroy = True


    def copy(self):
        '''
        '''

        obj_copy = GameObject()
        obj_copy.sprite_renderer = self.sprite_renderer.copy()
        obj_copy.transform = self.transform.copy()

        return obj_copy


    def __gt__(self, other):
        return self.sprite_renderer.sorting_order > other.sprite_renderer.sorting_order


    def __lt__(self, other):
        return self.sprite_renderer.sorting_order < other.sprite_renderer.sorting_order