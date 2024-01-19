import pygame


class Number:
    def __init__(self, n):
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(n), True, (255, 255, 255))

    # Отображение фпс
    def render(self, display, n):
        self.text = self.font.render(str(n), True, (255, 255, 255))
        display.blit(self.text, (1230, 8))
