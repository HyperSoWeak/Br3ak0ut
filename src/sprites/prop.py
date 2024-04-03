import pygame
import random
from pygame.math import Vector2
from config import *
from paddle import Paddle
from ball import Ball

#Define prop size
prop_radius = 10

#define dropping velocity acceleration dt
prop_velocity = 3
prop_acceleration = 0
prop_dt = 1

#define colors
WHITE = (248, 248, 255)
TRANSPARENT = (0, 0, 0, 0) 

class Prop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #initialize
        super().__init__()

        #set dropping velocity acceleration dt
        self.velocity = prop_velocity
        self.acceleration = prop_acceleration
        self.dt = prop_dt
        

        # Construct the size and position of the prop
        self.rect.center = (x, y)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)  
        self.image.fill(TRANSPARENT)  
        self.rect = self.image.get_rect()
       

        #set existance
        self._exist = False
        
    
    def update(self,Paddle):
        #update the collision between ball and bricks
        if pygame.sprite.spritecollide(ball.sprite, bricks, False):
            self.rect.x = ball.pos_x
            self.rect.y = ball.pos_y
            pygame.draw.circle(self.image, WHITE, (x, y), prop_radius) 
            self._exist = True
        #update the collision with Paddle
        if pygame.sprite.spritecollide(Prop,Paddle, False):
            self.kill()
            self._exist = False
        
        if self._exist:
            self.move()

    def move(self):
        self.velocity += self.dt*self.acceleration
        self.rect.y += self.velocity*self.dt
        
        

        


        
        
            

