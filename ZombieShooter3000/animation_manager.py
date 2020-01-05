'''
'''


_animations = {}


def add(name, animation) -> None:
    '''
    '''

    _animations[name] = animation


def get(name):
    '''
    '''

    return _animations[name].copy()