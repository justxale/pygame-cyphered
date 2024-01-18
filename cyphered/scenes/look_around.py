import pygame

from .base import BaseScene
from ..data import Path
from ..objects.base import GameObject
from ..services.sound import SoundMixer
from ..ui import Button
from ..ui.text import display_multiline_text

TEXT = """С недобрым утром! Голова раскалывается...
Эх, хорошо вчера видимо погулял, ничего не помню...
Вроде бы пообещал себе завязывать с этими делами,
ну что такое!.. Стоп... Я в пещере?
Что тут произошло... Стоит осмотреться"""


class LookAroundScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))
        self.continue_button = Button("Продолжить", font_color=(255, 255, 255), step_x=370, font_size=35, step_y=300)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    from .play import PlayScene
                    mouse_pos = pygame.mouse.get_pos()
                    if self.continue_button[2].collidepoint(mouse_pos):
                        self.fade_and_switch_scene(PlayScene())
                        SoundMixer.switch_music('crossroads', volume=0.2)

    def render(self, screen):
        self.sprites.draw(screen)
        display_multiline_text(screen, TEXT, (40, 100), font_size=40)
        pygame.draw.rect(screen, (255, 255, 255), self.continue_button[2], width=4)
        screen.blit(self.continue_button[0], self.continue_button[1])
