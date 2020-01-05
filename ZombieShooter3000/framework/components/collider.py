
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

        self.on_collision_enter = None
        self.on_trigger_enter = None

        self.enabled = True


    def get_rect(self) -> Rectangle:
        '''

        :returns:
        :rtype: Rectangle
        '''

        position = self.gameobject.transform.position + self.offset
        size = self.size * self.gameobject.transform.scale

        return Rectangle(position, size)


    def copy(self, gameObject):
        ''' returns a copy of this Collider

        :returns: a copy of this Collider
        :rtype: Collider
        '''

        return Collider(gameObject, self.tag, self.size.copy(), self.offset.copy(), self.is_trigger)