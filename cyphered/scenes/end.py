import pygame

from .base import BaseScene
from ..data import Path
from ..objects.base import GameObject
from ..ui import Button
from ..services.settings import Settings
from cyphered.ui.text import display_text
from ..services.sound import SoundMixer


class EndScene(BaseScene):
    def __init__(self, level_name, s):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))

        self.back_button = Button("Продолжить", step_x=-400, step_y=-50)
        self.buttons = [self.back_button]

        self.level_name = level_name
        self.s = s

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(LookAround())
                        from .play import PlayScene
                        from .title import TitleScene
                        if not self.is_paused:
                            match self.level_name:
                                case 'level1':
                                    self.fade_and_switch_scene(PlayScene('level2'))
                                case 'level2':
                                    self.fade_and_switch_scene(TitleScene())
                            self.is_paused = True
                        # SoundMixer.switch_music('background_music')
                        break

    def render(self, screen):
        self.sprites.draw(screen)
        for button in self.buttons:
            # pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
        if self.level_name[-1] == '1':
            display_text(f"Поздравляем! Вы прошли этот уровень за {self.s} секунд!",
                         screen, step_x=200, font_size=25)
            display_text("Вы получаете ключ, чтобы открыть дверь от следующего уровня!",
                         screen, step_x=200, step_y=50, font_size=25)
        else:
            display_text(f"Поздравляем! Вы прошли этот уровень за {self.s} секунд!",
                         screen, step_x=200, font_size=25)
            display_text("Вы прошли игру!",
                         screen, step_x=200, step_y=50, font_size=25)
