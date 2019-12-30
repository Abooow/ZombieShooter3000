

class Animator():
    ''' controls the animation system
    '''

    def __init__(self, gameobject):
        '''
        :param gameobject (GameObject): the game object this Animator is attached to
        '''

        self.gameobject = gameobject
        self._animations = {}

        self.current_animation = None


    def update(self, delta_time, playbackspeed=1) -> None:
        ''' updates the Animator

        :param delta_time (int): time since last frame
        :param playbackspeed (float): the playback speed of the Animation

        :returns: NoReturn
        :rtype: None
        '''

        if self.current_animation is not None:
            self.current_animation.update(delta_time, playbackspeed)


    def add_animation(self, name, animation) -> None:
        ''' adds an Animation to the Animator

        :param name (str): the name of the animation
        :param animation (Anbimation): the Animation to add

        :returns: NoReturn
        :rtype: None
        '''

        if not animation in self._animations:
            self._animations[name] = animation

            if self.current_animation is None:
                self.current_animation = animation


    def play(self, animation_name, reset=True) -> None:
        ''' plays an animation

        :param animation_name (str): the name of the animation
        :param reset (bool): reset the animation before playing

        :returns: NoReturn
        :rtype: None
        '''
        
        if reset:
            self._animations[animation_name].reset()

        self.current_animation = self._animations[animation_name]


    def copy(self, gameObject):
        '''
        '''

        copy_ = Animator(gameObject)
        copy_._animations = self._animations
        copy_.current_animation = self.current_animation

        return copy_