


class Animation:
    '''
    '''

    def __init__(self, frames, framerate=12, loop=True):
        '''
        :param frames (list[Surface]): the 
        :param framerate (int): the framerate of the Animation
        :param loop (bool): allow the Animation to loop 
        '''
        
        self.frames = frames
        self.framerate = framerate
        self.loop = True

        # the playback speed of the Animation
        self.playbackspeed = 1
        # the delegate to invoke once the Animation have finished (only if loop==False)
        self.on_done = None

        self._done = False
        self._current_frame = 0
        self._timer = 0


    def update(self, delta_time) -> None:
        ''' updates this Animation

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        # don't animate if the framerate is <= 0
        if self.framerate <= 0 or self.playbackspeed <= 0 or self._done:
            return

        # update timer
        self._timer += delta_time * self.playbackspeed

        if self._timer >= 1000/self.framerate:
            self._current_frame += 1
            self._timer = 0

            if self._current_frame >= len(self.frames):
                if self.loop:
                    self._current_frame = 0
                else:
                    self._done = True
                    if self.on_done is not None:
                        self.on_done()


    def get_current_frame(self):
        ''' get what frame that is currently being played

        :returns: the current frame
        :rtype: Surface
        '''
        
        return self.frames[self._current_frame]


    def reset(self) -> None:
        ''' resets this Animation

        :returns: NoReturn
        :rtype: None
        '''

        self._timer = 0
        self._current_frame = 0
        self._done = False


    def copy(self):
        ''' returns a copy of this Animation

        :returns: a copy of this animation
        :rtype: Animation
        '''
        
        anim_copy = Animation(self.frames, self.loop)

        anim_copy.on_done = self.on_done
        return Animation(self.frames, self.loop)