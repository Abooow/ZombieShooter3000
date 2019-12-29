


class SpriteRenderer():
    ''' for rendering a sprite
    '''


    def __init__(self, gameobject, sprite=None, source_rect=None, color=None, sorting_order=0):
        '''
        :param gameobject (GameObject): the game object this SpriteRenderer is attached to
        :param sprite (Surface): the sprite to render
        :param source_rect (Rectangle): represents a smaller portion of the sprite to draw
        :param color (tuple[int,int,int,int]): rendering color for the sprite (R, G, B, A), use None for no color
        :param sorting_order (int): the rendering order
        '''
        
        self.gameobject = gameobject
        self.sprite = sprite
        self.source_rect = source_rect
        self.color = color
        self.sorting_order = sorting_order
        self.enabled = True



    def copy(self):
        ''' returns a copy of this SpriteRenderer

        :returns: a copy of this SpriteRenderer
        :rtype: SpriteRenderer
        '''

        renderer_copy = SpriteRenderer(self.gameobject, self.sprite, self.source_rect, self.color, self.sorting_order)
        renderer_copy.enabled = self.enabled
        
        return renderer_copy