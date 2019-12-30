

class Animator():
    ''' controls the animation system
    '''

    def __init__(self, gameobject):
        '''
        :param gameobject (GameObject): the game object this Animator is attached to
        '''

        self.gameobject = gameobject
        self.animations = {}

        self.current_animation = None


    def update(self, delta_time) -> None:
        ''' updates the Animator

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        if self.current_animation is not None:
            self.current_animation.update(delta_time)

            if self.gameobject.sprite_renderer is not None:
                self.gameobject.sprite_renderer.sprite = self.current_animation.get_current_frame()


    def add_animation(self, name, animation) -> None:
        ''' adds an Animation to the Animator

        :param name (str): the name of the animation
        :param animation (Anbimation): the Animation to add

        :returns: NoReturn
        :rtype: None
        '''

        if not animation in self.animations:
            self.animations[name] = animation

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

        self.current_animation = self.animations[animation_name]


    def copy(self, gameObject):
        '''
        '''

        animator_copy = Animator(gameObject)
        animator_copy.animations = self.animations
        animator_copy.current_animation = self.current_animation

        return animator_copy