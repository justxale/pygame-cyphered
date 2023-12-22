import pygame

from . import SettingsScene
from ._base import BaseScene
from ..ui import Button


class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.start_button = Button("Играть", step_x=-450, step_y=-100)
        self.continue_button = Button("Продолжить", step_x=-450, step_y=0)
        self.settings_button = Button("Настройки", step_x=-450, step_y=100)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(...())
                        break
                    if self.settings_button[2].collidepoint(mouse_pos):
                        self.switch_scene(SettingsScene())
                        break

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), self.start_button[2])
        screen.blit(self.start_button[0], self.start_button[1])
        pygame.draw.rect(screen, (0, 0, 0), self.settings_button[2])
        screen.blit(self.settings_button[0], self.settings_button[1])
        pygame.draw.rect(screen, (0, 0, 0), self.continue_button[2])
        screen.blit(self.continue_button[0], self.continue_button[1])
