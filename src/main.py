import pygame
import sys

from app import App

if __name__ == '__main__':
    pygame.init()

    app = App()
    app.run()

    pygame.quit()
    sys.exit(0)