'''
'''

import pygame


effects_muted = False
songs_muted = False

_effects = {}
_songs = {}


def add_effect(name, path) -> None:
    '''
    '''

    _effects[name] = pygame.mixer.Sound(path)


def add_song(name, path):
    '''
    '''

    _songs[name] = path


def play_effect(name) -> None:
    '''
    '''

    if not effects_muted:
        _effects[name].play()


def play_song(name):
    '''
    '''

    pygame.mixer.music.load(_songs[name])
    if not songs_muted:
        pygame.mixer.music.play(-1)


def mute_songs():
    '''
    '''

    songs_muted = True
    pygame.mixer.pause()