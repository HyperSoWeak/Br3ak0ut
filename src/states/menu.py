import pygame

from config import *
from utils import render_text

from .state import State

class Menu(State):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 44)
        self.small_font = pygame.font.Font(None, 30)

    def handle_event(self, events): 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.next_state = 'Game'

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(BG_COLOR)

        render_text(screen, self.font, 'Br3ak0ut', (SCREEN_WIDTH / 2, 230), pivot='center')
        render_text(screen, self.small_font, 'Press Enter To Play', (SCREEN_WIDTH / 2, 350), pivot='center', color=(150, 150, 150))