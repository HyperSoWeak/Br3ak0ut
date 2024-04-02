import pygame
from pygame.math import Vector2
from paddle import calculate_ball_rebound
from random import randint
import config

class Ball(pygame.sprite.Sprite):
    def __init__(self, velocity: Vector2, pos_x, pos_y, radius, color = 'yellow'):
        super().__init__()

        self.color = color
        self.pos = Vector2(pos_x, pos_y)
        self.radius = radius
        self.velocity = velocity
        self.dt = 1

        # define ball's appearance
        # make the ball grow in size as its attack increases
        weak_ball = pygame.image.load('PATH').convert_alpha()
        medium_ball = pygame.image.load('PATH').convert_alpha()
        strong_ball = pygame.image.load('PATH').convert_alpha()
        self.ball_image = [weak_ball, medium_ball, strong_ball]
        self.image_index = 0
        self.image = self.ball_image[self.image_index]
        self.rect = self.image.get_rect(center = self.pos)

        # define music
        self.hit_brick_music = pygame.mixer.Sound('MUSIC PATH')
        self.hit_paddle_music = pygame.mixer.Sound('MUSIC PATH')

    def collision_with_wall(self):
        if self.rect.left <= 0 | self.rect.right >= SCREEN.WIDTH:
            self.velocity.x *= -1
        if self.rect.top <= 0:
            self.velocity.y *= -1

    def collision_with_paddle(self):
        if pygame.sprite.spritecollide(ball.sprite, paddle, False):
            self.hit_paddle_music.play()
            self.velocity = calculate_ball_rebound(self.velocity, self.radius) 
    
    def collision_with_brick(self):
        if pygame.sprite.spritecollide(ball.sprite, bricks, False):
            self.hit_brick_music.play()
            self.velocity.y *= -1

            # increase attack power
            self.image_index += 0.05
            if self.image_index >= len(self.ball_image): self.image_index = len(self.ball_image)
            self.image = self.ball_image[int(self.image_index)]

    # make the ball move unexpectedly with lots of twists and turns
    # 這裡還沒寫完 還在想要怎麼寫 get_event 跟設定持續時間
    def choatic_movement(self):
        choas_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(choas_timer, randint(10000, 15000))
        for event in pygame.event.get():
            if event.type == choas_timer:
                self.velocity += (randint(-0.5, 0.5), randint(-0.5, 0.5))

        
    def update(self):
        self.collision_with_paddle()
        self.collision_with_brick()
        self.collision_with_wall()
        self.rect.center += self.velocity * self.dt


"""
To be discussed
1. calculate_ball_rebound 裡面好像沒用到ball.size?
"""