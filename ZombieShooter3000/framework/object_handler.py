
from framework.vector2 import Vector2
from framework.rectangle import Rectangle
from framework.quad_tree import QuadTree


class ObjectHandler():
    ''' handles all GameObjects that are instantiated
    '''


    def __init__(self, world_position, world_size):
        '''
        :param world_position (Vector2): the position of the world
        :param window_size (Vector2): the size of the world
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
        
        quad_tree = QuadTree(Rectangle(self.world_position, self.world_size), 3)

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
                range.position -= range.size
                range.size *= 2

                # get all objects within the range
                others = quad_tree.query(range)
                
                if others is None:
                    continue

                # check for collisions
                for other in others:
                    if other is obj:
                        continue
                    
                    # if obj have been destroyed
                    if obj._flagged_as_destroy or obj.collider is None:
                        break

                    # if other have been destroyed
                    if other._flagged_as_destroy or other.collider is None:
                        continue

                    # obj and other have collided
                    if obj.collider.get_rect().intersects(other.collider.get_rect()):
                        # on trigger enter
                        if other.collider.is_trigger:
                            if obj.collider.on_trigger_enter is not None:
                                obj.collider.on_trigger_enter(other)
                        # on collision enter
                        else:
                            if obj.collider.on_collision_enter is not None:
                                obj.collider.on_collision_enter(other)


        # remove all objects that have been flagged_as_destroy
        for obj in self._objects:
            if obj._flagged_as_destroy:
                self._objects.remove(obj)
                del obj


    def get_objects(self) -> list:
        ''' get all instantiated objects

        :returns: all instantiated objects
        :rtype: list[GameObject]
        '''

        return self._objects[:]


    def instantiate(self, object):
        ''' instantiate a gameObject

        :param object (GameObject): the gameObject to instantiate

        :returns: the instantiated gameObject
        :rtype: GameObject
        '''

        self._objects.append(object)
        #self._objects.sort()
        self._objects.sort(key=lambda obj: 0 if obj.sprite_renderer is None else obj.sprite_renderer.sorting_order)

        return object