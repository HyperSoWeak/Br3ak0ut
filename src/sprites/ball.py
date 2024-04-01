import pygame
from pygame import Vector2
from config import *
from paddle import Paddle
from brick import Brick
from props import Props
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Ball:
    def __init__(self, x, y, radius, speed, color=(178, 201, 47)):
        self.pos = Vector2(x, y)
        self.radius = radius
        self.speed = Vector2(speed, speed)
        self.color = color
        self.rect = pygame.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.pos.x + self.radius, self.pos.y + self.radius)
        self.attack = 1
    
    def calculate_ball_wall_rebound(self):
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > SCREEN_WIDTH:
            self.speed.x *= -1
        if self.pos.y - self.radius < 0 or self.pos.y + self.radius > SCREEN_HEIGHT:
            self.speed.y *= -1

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

    def change_size(self, new_radius):
        self.radius = new_radius

    def update(self, dt):
        self.pos += self.speed * dt
        self.change_size(self.attack)
        self.calculate_ball_rebound()
        self.attck_change()

    def collides_with_paddle(self, paddle.rect):
        return self.rect.colliderect(paddle.rect)
    
    def collides_with_brick(self, brick.rect):
        return self.rect.colliderect(brick.rect)    

    def calculate_ball_rebound(self, paddle):
        if collides_with_paddle(paddle):
            new_speed = paddle.calculate_ball_rebound(self.speed, self.pos, self.radius)
            self.speed = new_speed
        if collides_with_brick(brick):
            self.speed.y *= -1
            #brick is smooth

    def attck_change(self, props):
        if self.rect.colliderect(props.rect)
            self.attack += 1