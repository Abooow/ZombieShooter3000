
from framework.vector2 import Vector2
from framework.components.transform import Transform


class Tilemap():
    '''
    '''

    def __init__(self, object_handler, map, tiles, tile_size, position):
        '''
        :param object_handler (ObjectHandler): 
        :param map (list[list[str]]): 
        :param tiles (list[Tile]): 
        :param tile_size (Vector2): the size of each Tile
        :param position (Vector2): the starting position of this Tilemap
        '''

        self.object_handler = object_handler
        self._map = map[:]
        self._tiles = {}
        self._tile_size = tile_size
        self._position = position
        self._instantiated_objects = []

        for tile in tiles:
            self._tiles[tile.name] = tile


    def instantiate(self) -> None:
        ''' instantiates every Tile
        
        :returns: NoReturn
        :rtype: None
        '''

        for y, row in enumerate(self._map):
            for x, name in enumerate(row):
                # error
                if name not in self._tiles:
                    print(f'"{name}" was not found')
                    continue

                tile = self._tiles[name].copy()

                tile.gameobject.transform.position = Vector2(self._position.x + x * self._tile_size.x, 
                                                             self._position.y + y * self._tile_size.y)

                self._instantiated_objects.append(self.object_handler.instantiate(tile.gameobject))


    def destroy(self) -> None:
        ''' destroys every Tile that was instantiated

        :returns: NoReturn
        :rtype: None
        '''

        for object in self._instantiated_objects:
            object.destroy()
