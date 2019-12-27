''' Handles all events
'''

import pygame


events = []


def update() -> None:
    ''' updates all the events

    :returns: NoReturn
    :rtype: None
    '''

    global events

    events = pygame.event.get()


# ---------------------------------- Keys
def is_key_down(key) -> bool:
    ''' gets whether given key is currently being held down 

    :param key (int): the key to check

    :returns: True if the key is being held down; False otherwise
    :rtype: bool
    '''

    keys = pygame.key.get_pressed()
    if keys[key]:
        return True

    return False


def is_key_pressed(key) -> bool:
    ''' gets whether given key have been pressed

    :param key (int): the key to check

    :returns: True the key was pressed; False otherwise
    :rtype: bool
    '''

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                return True

    return False


# ---------------------------------- Mouse
def is_mouse_down(button) -> bool:
    ''' gets whether given mouse button is currently being held down 

    :param button (int): the mouse button to check (1=left, 2=middle, 3=right)

    :returns: True if the mouse button is being held down; False otherwise
    :rtype: bool
    '''

    if pygame.mouse.get_pressed()[button-1]:
        return True

    return False


def is_mouse_pressed(button) -> bool:
    ''' gets whether given mouse button is have been pressed

    :param button (int): the mouse button to check (1=left, 2=middle, 3=right)

    :returns: True if the mouse button have been pressed; False otherwise
    :rtype: bool
    '''

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == button:
            return True

    return False


def check_occurred(type) -> bool:
    ''' gets whatever given eventType that occurred

    :param type (int): the event type to check

    :returns: True if the event occurred; False otherwise
    :rtype: bool
    '''

    for event in events:
        if event.type == type:
            return True

    return False