


class Tile():
    '''
    '''

    def __init__(self, name, sprite, source_rect=None):
        '''
        :param name (str): the name of this Tile
        :param sprite (Surface): 
        :param source_rect (Rectangle):
        '''

        self.name = name
        self.sprite = sprite
        self.source_rect = source_rect