import pygame

from config import *
from utils import render_text

from .state import State
from sprites.player import Player

class Game(State):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 44)
        self.player = Player(WIDTH / 2, HEIGHT - 100, 150, 20)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.next_state = 'Menu'
    
    def update(self, dt):
        self.player.update(dt)

    def render(self, screen):
        screen.fill(BG_COLOR)

        render_text(screen, self.font, 'Gameplay', (WIDTH / 2, 100), pivot='center')

        self.player.render(screen)