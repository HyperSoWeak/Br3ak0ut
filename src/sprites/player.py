import pygame

class Player:
    def __init__(self, x, y, width, height, color=(178, 201, 47)):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.color = color
        self.speed = 500

    def update(self, dt):
        self.movement_x = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.movement_x += 1
        if key_pressed[pygame.K_LEFT]:
            self.movement_x -= 1

        self.rect.x += self.movement_x * self.speed * dt

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=int(self.rect.height / 2))