
from framework.vector2 import Vector2
from framework.rectangle import Rectangle


class QuadTree():
    ''' are used to efficiently store data of points, which can be used to check for collision
    '''

    def __init__(self, boundary, capacity):
        '''
        :param boundary (Rectangle): the starting size of the QuadTree
        :param capacity (int): the maximum amount of points to insert to the QuadTree before subdividing
        '''

        self.boundary = boundary
        self.capacity = capacity
        self._points = []

        self._divided = False


    def insert(self, point, object) -> bool:
        ''' insert a point into the QuadTree

        :param point (Vector2): the point to insert
        :param object (object): the data that is stored with the point

        :returns: True if the point was within the boundaries of this QuadTree, otherwise False
        :rtype: bool
        '''

        if not self.boundary.contains_point(point):
            return False

        if len(self._points) < self.capacity:
            self._points.append((point, object))
            return True
        else:
            if not self._divided:
                self._subdivide()
                self._divided = True

        if self.north_west.insert(point, object): return True
        if self.north_east.insert(point, object): return True
        if self.south_west.insert(point, object): return True
        if self.south_east.insert(point, object): return True


    def query(self, range) -> list:
        ''' get all objects within the provided range

        :param range (Rectangle): the area to get objects from

        :returns: all objects that are within the range
        :rtype: list[object]
        '''

        found=[]

        if self.boundary.intersects(range):
            for point in self._points:
                if range.contains_point(point[0]):
                    found.append(point[1])
        else:
            return []

        if self._divided:
            found += self.north_west.query(range)
            found += self.north_east.query(range)
            found += self.south_west.query(range)
            found += self.south_east.query(range)

        return found


    def _subdivide(self) -> None:
        ''' subdivides the QuadTree into 4 new QuadTrees

        :returns: NoReturn
        :rtype: None
        '''

        position = self.boundary.position
        half_size = self.boundary.size/2

        nw = Rectangle(position, half_size)
        ne = Rectangle(position + half_size * Vector2(1, 0), half_size)
        sw = Rectangle(position + half_size * Vector2(0, 1), half_size)
        se = Rectangle(position + half_size * Vector2(1, 1), half_size)

        self.north_west = QuadTree(nw, self.capacity)
        self.north_east = QuadTree(ne, self.capacity)
        self.south_west = QuadTree(sw, self.capacity)
        self.south_east = QuadTree(se, self.capacity)