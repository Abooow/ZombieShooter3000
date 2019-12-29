
from framework.vector2 import Vector2


class Rectangle():
    ''' describes a 2D-rectangle.
    '''

    def __init__(self, position=Vector2(), size=Vector2()):
        '''
        :param position (Vector2): the position of the Rectangle
        :param size (Vector2): the size of the Rectangle
        '''

        self.position = position
        self.size = size


    def top(self) -> float:
        ''' get the top position of this Rectangle

        :returns: the top position of this Rectangle
        :rtype: float
        '''

        return self.position.y


    def bottom(self) -> float:
        ''' get the bottom position of this Rectangle

        :returns: the bottom position of this Rectangle
        :rtype: float
        '''

        return self.position.y + self.size.y


    def left(self) -> float:
        ''' get the left position of this Rectangle

        :returns: the left position of this Rectangle
        :rtype: float
        '''

        return self.position.x


    def right(self) -> float:
        ''' get the right position of this Rectangle

        :returns: the right position of this Rectangle
        :rtype: float
        '''

        return self.position.x + self.size.x


    def intersects(self, other) -> bool:
        ''' checks if this rectangle intersects with another Rectangle

        :param other (Rectangle): the other Rectangle

        :returns: True if this Rectangle intersects with the other Rectangle, oterwise False
        :rtype: bool
        '''

        return (self.bottom() > other.top() and self.top() < other.bottom() and
                self.right() > other.left() and self.left() < other.right())


    def contains_point(self, point) -> bool:
        ''' gets whether or not the provided point lies within the bounds of this Rectangle.

        :param point (Vector2): the coordinates to check for inclusion in this Rectangle.
        '''

        return (point.y >= self.top() and point.y <= self.bottom() and
                point.x >= self.left() and point.x <= self.right())


    def copy(self):
        ''' creates a copy of this Rectangle

        :returns: a copy of this Rectangle
        :rtype: Rectangle
        '''

        return Rectangle(self.position.copy(), self.size.copy())


    def to_tuple(self) -> tuple:
        ''' converts this Rectangle to a tuple[int,int,int,int] (x, y, width, height)

        :returns: a tuple version of this Rectangle
        :rtype: tuple[int,int,int,int]
        '''

        return (self.position.x, self.position.y, self.size.x, self.size.y)