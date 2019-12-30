
from framework.vector2 import Vector2
from framework.components.collider import Collider
from framework.components.animator import Animator
from framework.components.transform import Transform
from framework.components.sprite_renderer import SpriteRenderer


class GameObject():
    ''' the base class for all gameObjects
    '''


    def __init__(self, position=Vector2(0, 0), rotation=0, scale=Vector2(1, 1), origin=Vector2(0, 0)):
        '''
        :param position (Vector2): 
        '''

        # the Transform of this GameObject
        self.transform = Transform(self, position, rotation, scale, origin)
        # the SpriteRenderer of this GameObject
        self.sprite_renderer = None
        # the Collider of this GameObject
        self.collider = None
        # the Animator of this GameObject
        self.animator = None

        self._flagged_as_destroy = False


    def update(self, delta_time) -> None:
        ''' updates this gameObject

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        if self.animator is not None:
            self.animator.update(delta_time)


    def on_render(self, surface) -> None:
        ''' a method that is invoked when the GameObject about to render

        :param surface (Surface): the surface this GameObject will render on

        :returns: NoReturn
        :rtype: None
        '''

        pass


    def add_sprite_renderer(self, sprite=None, source_rect=None, color=None, sorting_order=0) -> None:
        '''
        '''

        self.sprite_renderer = SpriteRenderer(self, sprite, source_rect, color, sorting_order)


    def add_collider(self, tag='', size=Vector2(0, 0), offset=Vector2(0, 0), is_trigger=False, is_static=False) -> None:
        '''
        '''

        self.collider = Collider(self, tag, size, offset, is_trigger, is_static)


    def add_animator(self) -> None:
        '''
        '''

        self.animator = Animator(self)


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

        # transform
        obj_copy.transform = self.transform.copy(obj_copy)

        # spriteRenderer
        if self.sprite_renderer is not None:
            obj_copy.sprite_renderer = self.sprite_renderer.copy(obj_copy)

        # collider
        if self.collider is not None:
            obj_copy.collider = self.collider.copy(obj_copy)

        # animator
        if self.animator is not None:
            obj_copy.animator = self.animator.copy(obj_copy)

        return obj_copy


    def __gt__(self, other):
        if self.sprite_renderer is None or other.sprite_renderer is None:
            return False

        return self.sprite_renderer.sorting_order > other.sprite_renderer.sorting_order


    def __lt__(self, other):
        if self.sprite_renderer is None or other.sprite_renderer is None:
            return False

        return self.sprite_renderer.sorting_order < other.sprite_renderer.sorting_order