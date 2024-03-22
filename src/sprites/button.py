import pygame

class Button:
    def __init__(self, x, y, width, height, text, button_color=(60, 60, 60), hover_color=(80, 80, 80),
                 text_color=(220, 220, 220), font_size=30, corner_radius=0, on_click=lambda: None):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.text = text

        self.button_color = button_color
        self.hover_color = hover_color
        self.text_color = text_color

        self.font = pygame.font.Font(None, font_size)
        self.corner_radius = corner_radius

        self.__is_hovered = False
        self.__is_pressed = False
        self.is_clicked = False

        self.enabled = True
        self.on_click = on_click

    def update(self):
        self.is_clicked = False
        if not self.enabled:
            return

        mouse_pos = pygame.mouse.get_pos()
        self.__is_hovered = self.rect.collidepoint(mouse_pos)

        mouse_left = pygame.mouse.get_pressed()[0]
        if self.__is_hovered and mouse_left and not self.__is_pressed:
            self.__is_pressed = True
            self.is_clicked = True
            if callable(self.on_click):
                self.on_click()
            else:
                print('on_click argument is not callable.')
        
        if not mouse_left:
            self.__is_pressed = False

    def render(self, screen):
        if self.enabled:
            button_color = self.hover_color if self.__is_hovered else self.button_color
        else:
            button_color = (150, 150, 150)

        pygame.draw.rect(screen, button_color, self.rect, border_radius=self.corner_radius)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
