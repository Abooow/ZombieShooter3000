
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
        :param position (Vector2): the position of this GameObject
        :param rotation (int): the rotation of this GameObject
        :param scale (Vector2): the scale of this GameObject
        :param origin (Vector2): the origin of this GameObject, (0, 0) is the top left and (1, 1) is the bottom right
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
        ''' updates this GameObject

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
        ''' adds a SpriteRenderer to the GameObject

        :param sprite (Surface): the sprite to render
        :param source_rect (Rectangle): represents a smaller portion of the sprite to draw
        :param color (tuple[int,int,int,int]): rendering color for the sprite (R, G, B, A), use None for no color
        :param sorting_order (int): the rendering order

        :returns: NoReturn
        :rtype: None
        '''

        self.sprite_renderer = SpriteRenderer(self, sprite, source_rect, color, sorting_order)


    def add_collider(self, tag='', size=Vector2(0, 0), offset=Vector2(0, 0), is_trigger=False, is_static=False) -> None:
        ''' adds a Collider to the GameObject

        :param tag (str): the tag of this Collider
        :param size (Vector2): the size of this Collider
        :param offset (Vector2): the local offset of the Collider
        :param is_trigger (bool): is this collider configured as a trigger?
        :param is_static (bool): is this collider flagged as static?

        :returns: NoReturn
        :rtype: None
        '''

        self.collider = Collider(self, tag, size, offset, is_trigger, is_static)


    def add_animator(self) -> None:
        ''' adds a Animator to the GameObject

        :returns: NoReturn
        :rtype: None
        '''

        self.animator = Animator(self)


    def destroy(self) -> None:
        ''' destroys this gameObject

        :returns: NoReturn
        :rtype: None
        '''

        self._flagged_as_destroy = True


    def copy(self):
        ''' returns a copy of this GameObject

        :returns: a copy of this GameObject
        :rtype: GameObject
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