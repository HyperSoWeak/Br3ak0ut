import pygame

from config import *
from utils import render_text

from .state import State
from sprites.button import Button

class Menu(State):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font('assets/fonts/Louis George Cafe.ttf', 36)
        # self.small_font = pygame.font.Font(None, 30)

        self.buttons = {
            'Play': Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 130, 50, 'Play', on_click=self.btn_play),
            'Quit': Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, 130, 50, 'Quit', on_click=self.btn_quit)
        }

    def handle_event(self, events): 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.next_state = 'Game'

    def update(self, dt):
        for button in self.buttons.values():
            button.update()

    def render(self, screen):
        screen.fill(BG_COLOR)

        render_text(screen, self.font, 'Br3ak0ut', (SCREEN_WIDTH / 2, 200), pivot='center')

        for button in self.buttons.values():
            button.render(screen)
        # render_text(screen, self.small_font, 'Press Enter To Play', (SCREEN_WIDTH / 2, 350), pivot='center', color=(150, 150, 150))

    def btn_play(self):
        self.next_state = 'Game'

    def btn_quit(self):
        self.next_state = 'Exit'