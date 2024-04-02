# Import libaries
import pygame
import random
from ball import Ball

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Define brick size
brick_width = 20
brick_height = 20

# Define brick keys and hardnesses
brick_data = {
    red: {'hardness':3, 'score':10},    # Red with hardness 3
    green: {'hardness':2, 'score':5},    # Green with hardness 2
    blue: {'hardness':1, 'score':1}    # Blue with hardness 1
}

# Define text data
text_color = black
font_size = 12

# This class represents each brick
class Brick(pygame.sprite.Sprite):
    # Constructor, which passes in the color of the block, and its x and y position
    def __init__(self, color, x, y, text):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Set the color of the brick
        self.image = pygame.Surface([brick_width, brick_height])
        self.color = random.choice(list(brick_data.keys()))
        self.image.fill(self.color)

        # Construct the size and position of the brick
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Set the collision of the brick
        self.__is_collided = False

        # Set the hardnesses of the brick
        self.hardness = brick_data[self.color]['hardness']
        self.destroyed = False

        # Set the text of the brick
        self.text = self.hardness
        self.text_color = text_color
        self.font = pygame.font.Font('assets/fonts/Louis George Cafe.ttf', font_size)

        # Set the score of the brick
        self.score = brick_data[self.color]['score']

        # Set the props of the brick
        self.has_prop = False

    # Update if collided with ball
    def update(self, Ball):
        # Check if collided with ball
        self.__is_collided = self.rect.colliderect(Ball.rect)
        if self.__is_collided == True:
            temp_color = self.color
            self.color = white
            self.image.fill(self.color)
            self.hardness -= Ball.attack

            # Check if brick is destroyed
            if self.hardness <= 0:
                self.destroyed == True

            # Kill brick
            if self.destroyed:
                if self.has_prop == True:
                    Prop.drop    # Not done
                Player.score += self.score    # Not done
                pygame.sprite.Sprite.kill(self)

            # Brick not destroyed
            else:
                pygame.time.delay(20)
                self.color = temp_color
                self.image.fill(self.color)

        # Return collision to false
        self.__is_collided = False

    # Render the text on the brick
    def render(self, screen):
        # Set the text color and position
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)