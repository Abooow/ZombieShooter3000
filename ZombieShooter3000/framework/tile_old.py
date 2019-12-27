


class Tile():
    '''
    '''

    def __init__(self, gameobject, name):
        '''
        :param gameobject (GameObject): the GameObject attached to this Tile
        :param name (str): the name of this Tile
        '''

        self.gameobject = gameobject
        self.name = name



    def copy(self):
        '''
        '''

        return Tile(self.gameobject.copy(), self.name)
