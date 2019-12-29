
import pygame

from framework.vector2 import Vector2
from framework.gameobject import GameObject


class Tilemap(GameObject):
    ''' Tilemap is a system which handles Tiles
    '''

    def __init__(self, camera, map, tiles, tile_size, position, sorting_order=0):
        '''
        :param camera (Camera): the Camera that is attached to this Tilemap
        :param map (list[list[str]]): the map to draw
        :param tiles (list[Tile]): the list of Tiles to use
        :param tile_size (Vector2): the size of each Tile
        :param position (Vector2): the position of this Tilemap
        :param sorting_order (int): the rendering order of this TileMap
        '''

        super().__init__(position)

        self._camera = camera
        self._map = map[:]
        self._tiles = {}
        self._tile_size = tile_size
        self.sprite_renderer.sorting_order = sorting_order

        for tile in tiles:
            self._tiles[tile.name] = tile


    def on_render(self, surface) -> None:
        ''' a method that is invoked when the GameObject about to render

        :param surface (Surface): the surface this Tilemap will render on

        :returns: NoReturn
        :rtype: None
        '''

        super().on_render(surface)

        # the size of each tile after scaling
        scaled_tile_size = Vector2(int(self._camera.transform.scale.x * self._tile_size.x), 
                                   int(self._camera.transform.scale.y * self._tile_size.y))

        # calculate how many tiles will fit on the screen 
        max_tiles_on_screen = Vector2(self._camera.size.x // scaled_tile_size.x,
                                      self._camera.size.y // scaled_tile_size.y)

        # calculate the start index to begin drawing the map
        start_index = (self.transform.position + self._camera.transform.position) // scaled_tile_size
        if start_index.x < 0: start_index.x = 0
        if start_index.y < 0: start_index.y = 0

        # calculate the end index to stop drawing the map
        end_index = start_index + max_tiles_on_screen + Vector2(2, 2)
        if end_index.x > len(self._map[-1]) - 1: end_index.x = len(self._map[-1]) - 1
        if end_index.y > len(self._map) - 1: end_index.y = len(self._map) - 1


        for y in range(start_index.y, end_index.y):
            for x in range(start_index.x, end_index.x):
                name = self._map[y][x]   # get Tile name
                tile = self._tiles[name] # get Tile

                # scale the tile
                sprite = pygame.transform.scale(tile.sprite, scaled_tile_size.to_tuple())  

                # position of the tile
                position = self.transform.position - self._camera.transform.position + Vector2(x, y) * scaled_tile_size

                # draw tile
                surface.blit(sprite, position.to_tuple(), tile.source_rect)