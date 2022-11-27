import pygame

pygame.font.init()

default_font = pygame.font.get_default_font()


def render_text(text, size, color=(0, 0, 0)):
    """Returns a surface with rendered text"""
    font = pygame.font.SysFont('Comic Sans MS', size)
    return font.render(text, True, color)


def center_text(text_surface, surface):
    """Centers text_surface in surface"""
    text_rect = text_surface.get_rect() #creates rectangle of text surface
    text_size = text_rect.width, text_rect.height #uses the width and height of the text rectangle to determine font size
    surface_rect = surface.get_rect() #creates a rectangle with the surface
    pos_x = (surface_rect.width - text_size[0]) / 2 #centers the x in the middle of the surface rectangle
    pos_y = (surface_rect.height - text_size[1]) / 2 #centers the y in the middle of the surface rectangle
    surface.blit(text_surface, (pos_x, pos_y)) #blits the text into the center of the rectangle

    