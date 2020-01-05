''' Utility stuff
'''

import pygame


# if True, then the program quits
quit_game = False

# size of the world, only colliders that is inside the bounds will be updated
world_size = (1856, 1856)

# size of the game window
window_size = (1024, 700)
window = None

enemy_waves = [[]]

def draw_font(surface, text, color, position, font='Tahoma', size=18, bold=True):
    font_ = pygame.font.SysFont(font, size, bold, False)
    new_text = font_.render(text, True, color)
    surface.blit(new_text, position)