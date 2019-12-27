''' This module contains functions that allows you to change properties a pygame.surface (image)
'''

import pygame


def transform(image, scale, rotation) -> pygame.surface:
    ''' Transform an image

    :param image (surface): the image to change
    :param scale (tuple[int,int]): the new scale
    :param rotation (int): the new rotation

    :returns: a copy of the image but with a new transform
    :rtype: surface
    '''

    img_size = image.get_rect().size 

    new_image = image.copy()
    new_image = pygame.transform.scale(new_image, (img_size[0] * scale[0], img_size[1] * scale[1]))
    new_image = pygame.transform.rotate(new_image, rotation)
    
    return new_image


def transform_many(images, scale, rotation) -> list:
    ''' Change the transform on many images at once

    :param images (list[surface]): the images to change
    :param scale (tuple[int,int]): the new scale
    :param rotation (int): the new rotation

    :returns: a copy of the images but with a new transform
    :rtype: list
    '''

    return [transform(img, scale, rotation) for img in images]


def colorize(image, color) -> pygame.surface:
    ''' Create a "colorized" copy of a surface (replaces RGB values with the given color).

    :param image (surface): surface to create a colorize
    :param color (tuple[int,int,int]): the color for the filter

    :return: new colorized Surface instance
    :rtype: surface
    '''

    image = image.copy()

    # zero out RGB values
    #image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    # add in new RGB values
    image = image.convert_alpha()
    image.fill(color, None, pygame.BLEND_RGBA_MULT)

    return image
