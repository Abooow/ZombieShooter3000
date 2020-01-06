
from framework.vector2 import Vector2
from framework.rectangle import Rectangle


class Collider():
    ''' Collider represents a rectangle that allows a GameObject to collide
    '''

    def __init__(self, gameobject, tag='', size=Vector2(0, 0), offset=Vector2(0, 0), is_trigger=False, is_static=False):
        '''
        :param gameobject (GameObject): the game object this Collider is attached to
        :param tag (str): the tag of this Collider
        :param size (Vector2): the size of this Collider
        :param offset (Vector2): the local offset of the Collider
        :param is_trigger (bool): is this collider configured as a trigger?
        :param is_static (bool): is this collider flagged as static?
        '''

        self.gameobject = gameobject
        self.tag = tag
        self.size = size
        self.offset = offset
        self.is_trigger = is_trigger
        self.is_static = is_static

        # a delegate that is invoked whenever another Collider(not configured as a trigger) enters this Collider
        self.on_collision_enter = None
        # a delegate that is invoked whenever another Collider(configured as a trigger) enters this Collider
        self.on_trigger_enter = None

        # enabled collider is updated, disabled collider is not
        self.enabled = True


    def get_rect(self) -> Rectangle:
        ''' get the hitbox bounds of this collider

        :returns: the hitbox bounds of this collider
        :rtype: Rectangle
        '''

        position = self.gameobject.transform.position + self.offset
        size = self.size * self.gameobject.transform.scale

        return Rectangle(position, size)


    def copy(self, gameobject):
        ''' returns a copy of this Collider

        :param gameobject (GameObject): the gameObject that will be attached to the new Collider

        :returns: a copy of this Collider
        :rtype: Collider
        '''

        return Collider(gameobject, self.tag, self.size.copy(), self.offset.copy(), self.is_trigger)