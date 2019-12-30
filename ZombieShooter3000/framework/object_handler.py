
from framework.vector2 import Vector2
from framework.rectangle import Rectangle
from framework.quad_tree import QuadTree


class ObjectHandler():
    ''' handles all GameObjects that are instantiated
    '''


    def __init__(self, world_position, world_size):
        '''
        :param window_size (Vector2): the size of the window
        '''

        self.world_position = world_position
        self.world_size = world_size

        self._objects = []


    def update(self, delta_time) -> None:
        ''' updates all the gameObject

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        
        quad_tree = QuadTree(Rectangle(self.world_position, self.world_size), 4)

        # buid the quad_tree
        for obj in self._objects:
            # skip object without a collider
            if obj.collider is None or not obj.collider.enabled:
                continue

            # insert object
            quad_tree.insert(point=obj.transform.position, object=obj)

        # update objects
        for obj in self._objects:
            # update object
            obj.update(delta_time)

            # object have a collider
            if obj.collider is not None and obj.collider.enabled and not obj.collider.is_static:
                # create a range to check other objects
                range = obj.collider.get_rect()
                range.position -= range.size * 1.5
                range.size *= 3

                # get all objects within the range
                others = quad_tree.query(range)
                
                if others is None:
                    continue

                # check for collisions
                for other in others:
                    if other is obj:
                        continue
                    
                    # collided
                    if obj.collider.get_rect().intersects(other.collider.get_rect()):
                        if obj.collider.is_trigger:
                            if obj.collider.on_trigger_enter:
                                obj.collider.on_trigger_enter(other)
                        else:
                            if obj.collider.on_collision_enter:
                                obj.collider.on_collision_enter(other)
           
                        if other._flagged_as_destroy:
                            self._objects.remove(other)

            if obj._flagged_as_destroy:
                self._objects.remove(obj)


    def get_objects(self) -> list:
        ''' get all instantiated objects

        :returns: all instansiated objects
        :rtype: list[GameObject]
        '''

        return self._objects[:]


    def instantiate(self, object):
        ''' instantiate a gameObject

        :param object (GameObject): the gameObject to instantiate

        :returns: the instantiated clone
        :rtype: GameObject
        '''

        self._objects.append(object)
        self._objects.sort()

        return object