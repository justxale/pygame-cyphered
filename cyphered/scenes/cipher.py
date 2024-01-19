import pygame

from .base import BaseScene
from ..data import Path
from ..objects.base import GameObject
from ..ui import Button
from cyphered.ui.text import display_text
from ..services.sound import SoundMixer
from ..ui.input import InputBox


class CipherScene1(BaseScene):
    def __init__(self, level_name, s):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))

        self.to_know_button = Button("Узнать шифр", step_x=-400, step_y=-50)
        self.buttons = [self.to_know_button]

        self.level_name = level_name
        self.s = s
        self.e = False
        self.input_box1 = InputBox(100, 100, 140, 32)
        self.input_boxes = [self.input_box1]
        self.res = ''
        self.answer = "муха села на варенье вот и все стихотворенье"

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.to_know_button[2].collidepoint(mouse_pos):
                        from .cipher_description import Description
                        self.switch_scene(Description(self.level_name, self.s))

            self.res = self.input_boxes[0].r
            if self.res == self.answer:
                from .end import EndScene
                self.switch_scene(EndScene(self.level_name, self.s))
                # SoundMixer.switch_music('background_music')
                break

            for box in self.input_boxes:
                box.handle_event(event)

    def render(self, screen):
        self.sprites.draw(screen)
        for button in self.buttons:
            # pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
        display_text("Расшифруйте послание!",
                     screen, step_x=200, font_size=17, step_y=-200)
        display_text("-- ..- .... .- / ... . .-.. .- / -. .- / .-- .- .-. . -. -..- . / ",
                     screen, step_x=200, font_size=17, step_y=-175)
        display_text(".-- --- - /../.-- ... . / ... - .. .... --- - .-- --- .-. . -. -..- .",
                     screen, step_x=200, font_size=17, step_y=-150)
        display_text("Примечание: '/' - символ пробела, а в этом тексте",
                     screen, step_x=200, font_size=17, step_y=-125)
        display_text("пробел означает разделение между буквами",
                     screen, step_x=200, font_size=17, step_y=-100)
        display_text("Текст вводится без учета регистра и знаков",
                     screen, step_x=200, font_size=17, step_y=-75)
        display_text("препинания. Е и ё - одна и та же буква.",
                     screen, step_x=200, font_size=17, step_y=-50)
        for box in self.input_boxes:
            box.update()

        for box in self.input_boxes:
            box.draw(screen)