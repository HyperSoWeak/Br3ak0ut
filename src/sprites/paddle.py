import pygame
from math import sqrt
from pygame import Vector2
from config import *

class Paddle:
    def __init__(self, x, y, length, color=(178, 201, 47)):
        self.rect = pygame.Rect(0, 0, length, 15)
        self.rect.center = (x, y)
        self.color = color
        self.velocity = Vector2(0, 0)

        self.mu_k = 1

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

        self.velocity = Vector2((self.rect.centerx - prev_pos_x) / dt, 0)

    def set_length(self, length):
        min_length = 50

        if length > SCREEN_WIDTH:
            length = SCREEN_WIDTH
        if length < min_length:
            length = min_length
        self.rect.width = length

    def calculate_ball_rebound(self, ball_velocity: Vector2, ball_size: int) -> Vector2:
        sv_m = self.velocity.magnitude()
        # bv_m = ball_velocity.magnitude()
        # cos_theta = ball_velocity.dot(self.velocity) / sv_m / bv_m
        # k = 1

        ans = 2 * ball_velocity.dot(self.velocity) / sv_m * Vector2(0 ,-1) + ball_velocity
        # ans += Vector2(0, sqrt(k * ))
        ans -= self.mu_k * abs(ball_velocity.x - self.velocity.x) * self.velocity.normalize()

        return ans

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=int(self.rect.height / 2))