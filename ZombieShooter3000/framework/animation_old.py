


class Animation:
    '''
    '''

    def __init__(self, frames, loop=True):
        '''
        :paparam frames (list[Frame]): the 
        :param loop (bool): allow the Animation to loop 
        '''
        
        self.frames = frames
        self.loop = True

        self._done = False
        self._current_frame = 0
        self._set_timer()


    def update(self, delta_time, playbackspeed=1) -> None:
        ''' updates this Animation

        :param delta_time (int): the time since last frame
        :param playbackspeed (float): the playback speed of the Animation

        :returns: NoReturn
        :rtype: None
        '''

        self._timer -= delta_time * playbackspeed

        if not self._done and playbackspeed > 0 and self._timer <= 0:
            self._invoke_current_frame()

            self._current_frame += 1

            if self._current_frame >= len(self.frames):
                if self.loop:
                    self._current_frame = 0
                else:
                    self._done = True

            self._set_timer()

    def get_current_frame(self) -> object:
        ''' get what frame index that is currently being played

        :returns: the current frame index
        :rtype: int
        '''
        
        return self._current_frame


    def reset(self) -> None:
        ''' resets this Animation

        :returns: NoReturn
        :rtype: None
        '''

        self._current_frame = 0
        self._done = False
        self._set_timer()


    def copy(self):
        ''' returns a copy of this Animation

        :returns: a copy of this animation
        :rtype: Animation
        '''
        
        return Animation(self.frames, self.loop)


    def _invoke_current_frame(self) -> None:
        ''' invoke the current frame event

        :returns: NoReturn
        :rtype: None
        '''

        delegate = self.frames[self._current_frame].event

        if delegate is not None:
            delegate()


    def _set_timer(self) -> None:
        ''' sets the timer to the current frame duration

        :returns: NoReturn
        :rtype: None
        '''

        self._timer = self.frames[self._current_frame].duration


class Frame():
    '''
    '''

    def __init__(self, duration=100, event=None):
        '''
        :param duration (int): the duration of this Frame
        :param event (delegate): the function or method to be invoked once the Frame have finished
        '''
        
        self.duration = duration
        self.event = event