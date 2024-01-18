import pygame

from . import SettingsScene
from .base import BaseScene
from .look_around import LookAroundScene
from .play import PlayScene
from ..data import Path, dev
from ..objects.base import GameObject
from ..services.save import Saver
from ..ui import Button
from ..ui.text import display_text
from ..services.sound import SoundMixer
from .rules import RulesScene


class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))

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
                        self.switch_scene(LookAroundScene())
                        # self.fade_and_switch_scene(PlayScene())
                        # SoundMixer.switch_music('background_music')
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
        self.sprites.draw(screen)
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 255, 255), button[2], width=4, border_radius=16)
            screen.blit(button[0], button[1])
        display_text('.'.join(map(str, dev.VERSION)) + f' | {dev.BUILD}', screen, step_y=250, step_x=450)
        display_text('C y p h e r e d', screen, step_x=-300, step_y=-300, font_size=80)
