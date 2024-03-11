import pygame

from config import *
from states.menu import Menu

class App:
    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = FPS

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption(GAME_CAPTION)

        self.clock = pygame.time.Clock()

        self.states = {
            'Menu': Menu()
        }
        self.state = self.states['Menu']

        self.running = True

    def flip_state(self, state_name, carry):
        if state_name == 'Exit':
            pygame.time.delay(200)
            self.running = False
            return

        self.state = self.states[state_name]
        self.state.load(carry)
        pygame.time.delay(100)
        
    def handle_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.state.handle_event(events)
    
    def update(self, dt):
        self.state.update(dt)
        if self.state.next_state:
            self.flip_state(self.state.next_state, self.state.carry)

    def render(self):
        self.state.render(self.screen)

    def run(self):
        while self.running:
            dt = self.clock.tick(self.FPS) / 1000.0

            self.handle_event()
            self.update(dt)
            self.render()

            pygame.display.flip()