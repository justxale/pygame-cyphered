import pygame

from .base import BaseScene
from ..data import Path
from ..objects.base import GameObject
from ..ui import Button
from cyphered.ui.text import display_text
from ..services.sound import SoundMixer


class Description(BaseScene):
    def __init__(self, level_name, s):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))

        self.continue_button = Button("Продолжить", step_x=350, step_y=-250)
        self.buttons = [self.continue_button]

        self.level_name = level_name
        self.s = s

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.continue_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(LookAround())
                        from .cipher import CipherScene1
                        from .title import TitleScene
                        if not self.is_paused:
                            match self.level_name:
                                case 'level1':
                                    self.switch_scene(CipherScene1(self.level_name, self.s))
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
        display_text("Данный шифр - это Азбука Морзе. Шифр был создан Сюмиэлем",
                     screen, step_x=-100, step_y=-240, font_size=20)
        display_text("Морзе, Альфредом Вейлем и Джозефом Генри в 1838 году для изобретенного",
                     screen, step_x=-100, step_y=-200, font_size=20)
        display_text("ими телеграфного аппарата, получившего название Аппарат Морзе. Это было",
                     screen, step_x=-100, step_y=-160, font_size=20)
        display_text("первое широко используемое электрическое приспособление для передачи сообщений",
                     screen, step_x=-100, step_y=-120, font_size=20)
        display_text("на дальние расстояния. Телеграф произвел революцию в СМИ и позволял немедленно",
                     screen, step_x=-100, step_y=-80, font_size=20)
        display_text("передавать сообщения о событиях, произошедших в одной стране, по всему миру.",
                     screen, step_x=-100, step_y=-40, font_size=20)
