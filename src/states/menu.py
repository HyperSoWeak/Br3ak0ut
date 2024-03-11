import pygame

from config import *
from utils import render_text

from .state import State

class Menu(State):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 44)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(BG_COLOR)

        render_text(screen, self.font, 'Br3ak0ut', (WIDTH / 2, 230), pivot='center')