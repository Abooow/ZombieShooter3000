
import math
import framework.vector2 as vector


class Transform():
    ''' position, rotation and scale of an object
    '''


    def __init__(self, gameobject, position=vector.ZERO, rotation=0, scale=vector.ONE, origin=vector.ZERO):
        '''
        :param gameobject (GameObject): the gameObject this Transform is attached to
        :param position (Vector2): the position of this Transform
        :param rotation (int): the rotation of this Transform
        :param scale (Vector2): the scale of this Transform
        :param origin (Vector2): the origin of this Transform, (0, 0) is the top left and (1, 1) is the bottom right
        '''

        self.gameobject = gameobject
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.origin = origin


    def look_at(self, target) -> None:
        ''' rotates the Transform so it's facing the targets position.

        :param target (Vector2): the target position to look at

        :returns: NoReturn
        :rtype: None
        '''

        delta_x = self.position.x - target.x
        delta_y = self.position.y - target.y

        self.rotation = -(math.atan2(delta_y, delta_x) * (180 / math.pi) - 90)


    def forward(self) -> vector.Vector2:
        ''' the forward vector of this Transform

        :returns: a normalized vector pointing forward
        :rtype: Vector2
        '''

        # 57.295 = deg to rad
        return vector.Vector2(-math.sin(self.rotation / 57.295), -math.cos(self.rotation / 57.295))


    def copy(self):
        ''' returns a copy of this Transform

        :returns: a copy of this Transform
        :rtype: Transform
        '''

        transform_copy = Transform(self.gameobject)
        transform_copy.position = self.position.copy()
        transform_copy.rotation = self.rotation
        transform_copy.scale = self.scale.copy()
        transform_copy.origin = self.origin

        return transform_copy