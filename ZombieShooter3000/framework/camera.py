

import pygame
import math

from framework.vector2 import Vector2


class Camera():
    ''' camera is a device that allows the player to view the world with all GameObject
    '''


    def __init__(self, surface, object_handler, transform, size, offset):
        '''
        :param surface (Surface): the Surface to render all objects on
        :param object_handler (ObjectHandler): the ObjectHandler attached to this Camera to keep track of all GameObjects
        :param transform (Transform): the Transform that is attached to this Camera
        :param size (Vector2): the rendering size of the Camera
        :param offset (Vector2): the offset of the rendering
        '''

        self.surface = surface
        self._object_handler = object_handler
        self.transform = transform
        self.size = size
        self.offset = offset


    def zoom(self, amount, to=Vector2(0, 0)) -> None:
        ''' zoom the camera towards a specified point

        :param amount (float): the amount to zoom
        :param to (Vector2): the point to zoom towards (screen coordinates)

        :returns: NoReturn
        :rtype: None
        '''

        new_scale = self.transform.scale * amount

        width = self.transform.position.x + to.x
        height = self.transform.position.y + to.y
        

        self.transform.position.x -= width  * (1 - new_scale.x/self.transform.scale.x)
        self.transform.position.y -= height * (1 - new_scale.y/self.transform.scale.y)
        
        self.transform.scale = new_scale


    def screen_to_world_point(self, point) -> Vector2:
        ''' transforms a point from screen space into world space

        :param point (Vector2): the Vector2 to convert to a world point

        :returns: a new point that is converted to world space
        :rtype: Vector2
        '''

        return Vector2((point.x + self.transform.position.x) / self.transform.scale.x, 
                       (point.y + self.transform.position.y) / self.transform.scale.y)


    def world_to_screen_point(self, point) -> Vector2:
        ''' transforms a point from world space into screen space

        :param point (Vector2): the Vector2 to convert to a screen point

        :returns: a new point that is converted to screen space
        :rtype: Vector2
        '''

        return Vector2((point.x * self.transform.scale.x - self.transform.position.x), 
                       (point.y * self.transform.scale.y - self.transform.position.y))


    def render(self) -> None:
        ''' renders all GameObjects

        :returns: NoReturn
        :rtype: None
        '''
        
        objects = self._object_handler.get_objects()
        
        for obj in objects:
            obj_transform = obj.transform
            obj_renderer = obj.sprite_renderer

            obj.on_render(self.surface)

            if obj_renderer is None or obj_renderer.sprite is None:
                continue

            # get the size of the image before rotation and scaling
            orig_size = obj_renderer.sprite.get_rect().size
            # calculate the new size of imge
            new_size = (int(orig_size[0] * obj_transform.scale.x * self.transform.scale.x),
                        int(orig_size[1] * obj_transform.scale.y * self.transform.scale.y))

            # scale the image
            sprite = pygame.transform.scale(obj_renderer.sprite, new_size)  
            # rotate the image
            sprite = pygame.transform.rotate(sprite, obj_transform.rotation)

            # get the size of the image after rotation and scaling
            size = sprite.get_rect().size
            # calculate the position of the image
            position = Vector2(obj_transform.position.x * self.transform.scale.x, 
                               obj_transform.position.y * self.transform.scale.y)

            # offset of the image
            offset = (size[0] * obj_transform.origin.x,
                      size[1] * obj_transform.origin.y)

            # position of the image with the offset and 
            new_position = (position.x - offset[0] - self.transform.position.x, 
                            position.y - offset[1] - self.transform.position.y)

            if obj_renderer.color is not None:
                sprite.fill(obj_renderer.color, None, pygame.BLEND_RGBA_MULT)

            # draw the image
            self.surface.blit(sprite, new_position, obj_renderer.source_rect)