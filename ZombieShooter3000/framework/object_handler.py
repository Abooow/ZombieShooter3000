


class ObjectHandler():
    ''' handles all GameObjects that are instantiated
    '''


    def __init__(self):
        '''
        '''

        self._objects = []


    def update(self, delta_time) -> None:
        ''' updates all the gameObject

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        
        for obj in self._objects:
            obj.update(delta_time)
            if obj._flagged_as_destroy:
                self._objects.remove(obj)


    def get_objects(self) -> list:
        ''' get all instansiated objects

        :returns: all instansiated objects
        :rtype: list[GameObject]
        '''

        return self._objects[:]


    def instantiate(self, object):
        ''' instantiates a gameObject

        :param object (GameObject): the gameObject to instantiate

        :returns: the instantiated clone
        :rtype: GameObject
        '''

        self._objects.append(object)
        self._objects.sort()

        return object