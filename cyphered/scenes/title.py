import pygame

from . import SettingsScene
from .base import BaseScene
from .play import PlayScene
from ..services.save import Saver
from ..ui import Button
from ..services.sound import SoundMixer
from .rules import RulesScene


class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)

        self.start_button = Button("Играть", step_x=-400, step_y=-150)
        self.continue_button = Button("Продолжить", step_x=-400, step_y=-50)
        self.search_button = Button("Правила", step_x=-400, step_y=50)
        self.settings_button = Button("Настройки", step_x=-400, step_y=150)
        self.quit_button = Button("Выйти из игры", step_x=-400, step_y=250)
        self.buttons = [self.start_button, self.continue_button, self.settings_button, self.quit_button,
                        self.search_button]

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(LookAround())
                        self.fade_and_switch_scene(PlayScene())
                        SoundMixer.switch_music('background_music')
                        break

                    if self.continue_button[2].collidepoint(mouse_pos):
                        save = Saver.load_save_file('save1')
                        if save:
                            self.fade_and_switch_scene(PlayScene(save_data=save))
                            SoundMixer.switch_music('background_music')
                        break

                    if self.settings_button[2].collidepoint(mouse_pos):
                        self.switch_scene(SettingsScene())
                        break

                    if self.quit_button[2].collidepoint(mouse_pos):
                        self.destroy()
                        break

                    if self.search_button[2].collidepoint(mouse_pos):
                        self.switch_scene(RulesScene())

    def render(self, screen):
        for button in self.buttons:
            pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
