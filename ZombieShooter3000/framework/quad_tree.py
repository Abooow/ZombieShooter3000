
from framework.vector2 import Vector2
from framework.rectangle import Rectangle


class QuadTree():


    def __init__(self, boundary, capacity):
        '''
        :param boundary (Rectangle):
        '''

        self.boundary = boundary
        self.capacity = capacity
        self.transforms = []

        self._divided = False


    def insert(self, transform):
        '''

        :param transform (Transform):

        '''

        if not self.boundary.contains_point(transform.position):
            return False

        if len(self.transforms) < self.capacity:
            self.transforms.append(transform)
            return True
        else:
            if not self._divided:
                self.subdivide()
                self._divided = True

        if self.north_west.insert(transform): return True
        if self.north_east.insert(transform): return True
        if self.south_west.insert(transform): return True
        if self.south_east.insert(transform): return True


    def subdivide(self):
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


    def query(self, range):
        found=[]
        if not self.boundary.intersects(range):
            return []
        else:
            for transform in self.transforms:
                if range.contains_point(transform.position):
                    found.append(transform)

        if self._divided:
            found += self.north_west.query(range)
            found +=self.north_east.query(range)
            found +=self.south_west.query(range)
            found +=self.south_east.query(range)

        return found