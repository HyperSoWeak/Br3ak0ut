import pygame

def render_text(surf: pygame.Surface, font: str, text: str, pos: tuple,
                color=(255, 255, 255), pivot='topleft'):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    if pivot == 'topleft':
        text_rect.topleft = pos
    elif pivot == 'center':
        text_rect.center = pos
    surf.blit(text_surf, text_rect)

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))

def is_circle_collide_point(point, center, radius):
    distance_squared = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
    return distance_squared <= radius ** 2