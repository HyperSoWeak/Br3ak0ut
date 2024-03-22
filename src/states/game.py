import pygame

from config import *
from utils import render_text

from .state import State
from sprites.player import Player
from sprites.button import Button

class Game(State):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font('assets/fonts/Louis George Cafe.ttf', 36)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, 150)
        self.btn = Button(100, 70, 100, 50, 'Back', on_click=self.btn_click)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.next_state = 'Menu'
    
    def update(self, dt):
        self.player.update(dt)
        self.btn.update()

    def render(self, screen):
        screen.fill(BG_COLOR)

        render_text(screen, self.font, 'Gameplay', (SCREEN_WIDTH / 2, 100), pivot='center')

        self.player.render(screen)
        self.btn.render(screen)

    def btn_click(self):
        self.next_state = 'Menu'