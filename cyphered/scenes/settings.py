import pygame

from .base import BaseScene
from ..data import Path
from ..objects.base import GameObject
from ..ui import Button
from ..services.settings import Settings
from ..services.settings import Settings
from cyphered.ui.text import display_text


class SettingsScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.sprites = pygame.sprite.Group()

        self.bg = GameObject(self.sprites)
        self.bg.self_load_image(Path.sprite('bg'))
        if Settings.jump_key == "space":
            self.jump_button = Button("пробел", font_size=25, step_x=-160)  # fontt='./Resources/font.ttf')
        elif Settings.jump_key == "w":
            self.jump_button = Button("w", font_size=25, step_x=-160)
        if Settings.move_keys == "arrows":
            self.rightleft_button = Button("стрелки", step_x=300, font_size=25)
        elif Settings.move_keys == "ad":
            self.rightleft_button = Button("ad", step_x=300, font_size=25)
        self.music_button_plus = Button("+", font_color=(255, 255, 255), step_x=-370, font_size=35)
        self.music_button_minus = Button("-", font_color=(255, 255, 255), step_x=-440, font_size=35)
        self.back = Button("Назад", font_color=(255, 255, 255), step_x=550, font_size=35, step_y=-250)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.music_button_plus[2].collidepoint(mouse_pos):
                        if Settings.music_volume + 0.1 <= 1:
                            Settings.music_volume += 0.1
                        else:
                            Settings.music_volume = 1.0
                    elif self.music_button_minus[2].collidepoint(mouse_pos):
                        if Settings.music_volume - 0.1 >= 0:
                            Settings.music_volume -= 0.1
                        else:
                            Settings.music_volume = 0.0
                    Settings.music_volume = round(Settings.music_volume, 1)
                    pygame.mixer.music.set_volume(Settings.music_volume)
                    if self.jump_button[2].collidepoint(mouse_pos):
                        if Settings.jump_key == "w":
                            Settings.jump_key = 'space'
                            self.jump_button = Button("пробел", font_size=25, step_x=-160)
                        else:
                            Settings.jump_key = 'w'
                            self.jump_button = Button("w", font_size=25, step_x=-160)
                    if self.rightleft_button[2].collidepoint(mouse_pos):
                        if Settings.move_keys == "arrows":
                            Settings.move_keys = "ad"
                            self.rightleft_button = Button("ad", step_x=300, font_size=25)
                        else:
                            Settings.move_keys = "arrows"
                            self.rightleft_button = Button("стрелки", step_x=300, font_size=25)
                    Settings.save_settings()
                    if self.back[2].collidepoint(mouse_pos):
                        from .title import TitleScene
                        self.switch_scene(TitleScene())

    def render(self, screen):
        self.sprites.draw(screen)
        screen.blit(self.music_button_plus[0], self.music_button_plus[1])
        screen.blit(self.music_button_minus[0], self.music_button_minus[1])

        display_text("Громкость музыки", screen, step_x=-390, step_y=-80, font_size=25)
        display_text(str(int(Settings.music_volume * 10)), screen, step_x=-405, step_y=-30, font_size=25)
        display_text("Прыжок", screen, step_x=-160, step_y=-80, font_size=25)
        display_text("Управление кнопками движения вправо-влево", screen, step_x=250, step_y=-80, font_size=25)

        screen.blit(self.jump_button[0], self.jump_button[1])
        screen.blit(self.rightleft_button[0], self.rightleft_button[1])
        screen.blit(self.back[0], self.back[1])
