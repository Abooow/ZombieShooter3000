
import math


class Vector2():
    ''' describes a 2D-vector.
    '''


    def tuple_to_vector2(tuple):
        ''' converts a tuple[int,int] to a Vector2

        :param tuple (tuple[int,int]): the tuple to convert

        :returns: a Vector2 version of a tuple
        :rtype: Vector2
        '''

        return Vector2(tuple[0], tuple[1])


    def __init__(self, x=0, y=0):
        '''
        :param x (float): x value for the vector
        :param y (float): y value for the vector
        '''

        self.x = x
        self.y = y


    def copy(self):
        ''' returns a copy of this Vector2

        :returns: a copy of this Vector2
        :rtype: Vector2
        '''

        return Vector2(self.x, self.y)


    def length(self) -> float:
        ''' get the length of this Vector2

        :returns: the length of this vector
        :rtype: float
        '''

        return math.sqrt(self.x ** 2 + self.y ** 2)


    def normalized(self):
        ''' returns a normalized copy of this Vector2

        :returns: a normalized copy of this Vector2
        :rtype: Vector2
        '''

        length = self.length()
        return Vector2(self.x / length, self.y / length)


    def to_tuple(self) -> tuple:
        '''
        '''

        return (self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __gt__(self, value):
        return self.x > other.x and self.y > other.y


    def __add__(self, other):
        if type(other) is float or type(other) is int:
            return Vector2(self.x + other, self.y + other)
        elif type(other) is Vector2:
            return Vector2(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        if type(other) is float or type(other) is int:
            return Vector2(self.x - other, self.y - other)
        elif type(other) is Vector2:
            return Vector2(self.x - other.x, self.y - other.y)


    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return Vector2(self.x * other, self.y * other)
        elif type(other) is Vector2:
            return Vector2(self.x * other.x, self.y * other.y)


    def __floordiv__(self, other):
        if type(other) is float or type(other) is int:
            return Vector2(self.x // other, self.y // other)
        elif type(other) is Vector2:
            return Vector2(int(self.x // other.x), int(self.y // other.y))


    def __truediv__(self, other):
        if type(other) is float or type(other) is int:
            return Vector2(self.x / other, self.y / other)
        elif type(other) is Vector2:
            return Vector2(self.x / other.x, self.y / other.y)



UP = Vector2(0, -1)     # a Vector2 pointing up
DOWN = Vector2(0, 1)    # a Vector2 pointing down
LEFT = Vector2(-1, 0)   # a Vector2 pointing left
RIGHT = Vector2(1, 0)   # a Vector2 pointing right

ZERO = Vector2(0, 0)    # a Vector2 with components 0, 0
ONE = Vector2(1, 1)     # a Vector2 with components 1, 1