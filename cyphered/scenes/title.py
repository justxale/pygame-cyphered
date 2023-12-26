import pygame

from . import SettingsScene
from ._base import BaseScene
from ..ui import Button
from ..services.sound import SoundMixer
from .look_around import LookAround


class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.buttons = []

        self.start_button = Button("Играть", step_x=-400, step_y=-50)
        self.continue_button = Button("Продолжить", step_x=-400, step_y=50)
        self.settings_button = Button("Настройки", step_x=-400, step_y=150)
        self.quit_button = Button("Выйти из игры", step_x=-400, step_y=250)

        self.buttons.append(self.start_button)
        self.buttons.append(self.continue_button)
        self.buttons.append(self.settings_button)
        self.buttons.append(self.quit_button)

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button[2].collidepoint(mouse_pos):
                        self.switch_scene(LookAround())
                        break

                    if self.continue_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(SettingsScene())
                        break

                    if self.settings_button[2].collidepoint(mouse_pos):
                        self.switch_scene(SettingsScene())
                        break

                    if self.quit_button[2].collidepoint(mouse_pos):
                        self.destroy()
                        break

    def render(self, screen):
        for button in self.buttons:
            pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
