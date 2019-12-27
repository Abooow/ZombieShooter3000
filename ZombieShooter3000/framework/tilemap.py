
import pygame

from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Tilemap(GameObject):
    '''
    '''

    def __init__(self, camera, map, tiles, tile_size, position, sorting_order=0):
        '''
        :param camera (Camera): 
        :param map (list[list[str]]): 
        :param tiles (list[Tile]): 
        :param tile_size (Vector2): the size of each Tile
        :param position (Vector2): the starting position of this Tilemap
        '''

        super().__init__(position)

        self.camera = camera
        self._map = map[:]
        self._tiles = {}
        self._tile_size = tile_size
        self.sprite_renderer.sorting_order = sorting_order

        for tile in tiles:
            self._tiles[tile.name] = tile


    def draw(self, surface):
        '''
        '''

        scaled_tile_size = (int(self.camera.transform.scale.x * self._tile_size.x), 
                            int(self.camera.transform.scale.y * self._tile_size.y))

        max_tiles_on_screen = self._get_max_tiles_on_screen(scaled_tile_size)

        start_index = self._get_start_index(scaled_tile_size)

        max_tiles = Vector2(start_index[0] + max_tiles_on_screen[0],
                            start_index[1] + max_tiles_on_screen[1])

        if max_tiles.x < 0:
            max_tiles.x = 0
        if max_tiles.y < 0:
            max_tiles.y = 0

        if max_tiles.x >= len(self._map[-1]) - 1:
            max_tiles.x = len(self._map[-1]) - 1
        if max_tiles.y >= len(self._map) - 1:
            max_tiles.y = len(self._map) - 1

        max_tiles = max_tiles.to_tuple()


        for y in range(start_index[1], max_tiles[1]):
            for x in range(start_index[0], max_tiles[0]):
                name = self._map[y][x]
                tile = self._tiles[name]

                position = ((x * self._tile_size.x - self.camera.transform.position.x) * self.camera.transform.scale.x,
                            (y * self._tile_size.y - self.camera.transform.position.y) * self.camera.transform.scale.y)
                
                # scale the image
                sprite = pygame.transform.scale(tile.sprite, scaled_tile_size)  

                surface.blit(sprite, position, tile.source_rect)


    def _get_max_tiles_on_screen(self, scaled_tile_size) -> tuple:
        '''
        '''

        max_tiles_on_screen = Vector2(self.camera.size.x // scaled_tile_size[0],
                                      self.camera.size.y // scaled_tile_size[1])
        
        if max_tiles_on_screen.x < 0:
            max_tiles_on_screen.x = 0
        if max_tiles_on_screen.y < 0:
            max_tiles_on_screen.y = 0

        if max_tiles_on_screen.x >= len(self._map[-1]) - 1:
            max_tiles_on_screen.x = len(self._map[-1]) - 1
        if max_tiles_on_screen.y >= len(self._map) - 1:
            max_tiles_on_screen.y = len(self._map) - 1

        return max_tiles_on_screen.to_tuple()


    def _get_start_index(self, scaled_tile_size) -> tuple:
        '''
        '''

        start_index = Vector2(int((self.transform.position.x - self.camera.transform.position.x) // scaled_tile_size[0]), 
                              int((self.transform.position.y - self.camera.transform.position.y) // scaled_tile_size[1]))

        if start_index.x < 0:
            start_index.x = 0
        if start_index.y < 0:
            start_index.y = 0

        if start_index.x >= len(self._map[-1]) - 1:
            start_index.x = len(self._map[-1]) - 1
        if start_index.y >= len(self._map) - 1:
            start_index.y = len(self._map) - 1


        return start_index.to_tuple()