import pygame

from abc import abstractmethod

class State:
    def __init__(self):
        self.load()

    def load(self, carry={}):
        self.carry = {}
        self.next_state = None

    def handle_event(self, events):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass

    def handle_input(self, input):
        pass