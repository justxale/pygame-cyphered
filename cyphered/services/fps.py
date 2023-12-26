import pygame


class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, (255, 255, 255))

    # Отображение фпс
    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(), 2)), True, (255, 255, 255))
        display.blit(self.text, (0, 0))

    # Получение фпс
    def get_fps(self):
        return int(self.clock.get_fps())
