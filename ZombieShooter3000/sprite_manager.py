'''
'''

import pygame


_sprites = {}


def add(name, path) -> None:
    '''
    '''

    _sprites[name] = pygame.image.load(path)


def get(name):
    '''
    '''

    return _sprites[name]