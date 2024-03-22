import pygame
from config import *

class Player:
    def __init__(self, x, y, length, color=(178, 201, 47)):
        self.rect = pygame.Rect(0, 0, length, 15)
        self.rect.center = (x, y)
        self.color = color
        self.velocity = 0

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()

        key_pressed = pygame.key.get_pressed()
        if(key_pressed[pygame.K_RIGHT]):
            self.setLength(self.rect.width + 5)
        if(key_pressed[pygame.K_LEFT]):
            self.setLength(self.rect.width - 5)

        prev_pos_x = self.rect.centerx
        self.rect.centerx = mouse_pos[0]
        
        if(self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
        if(self.rect.left < 0):
            self.rect.left = 0

        self.velocity = (self.rect.centerx - prev_pos_x) / dt

    def setLength(self, length):
        min_length = 50

        if length > SCREEN_WIDTH:
            length = SCREEN_WIDTH
        if length < min_length:
            length = min_length
        self.rect.width = length

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=int(self.rect.height / 2))