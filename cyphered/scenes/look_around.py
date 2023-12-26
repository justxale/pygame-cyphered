import pygame

from ._base import BaseScene
from ..ui import Button
from cyphered.ui.Multiple_text_displ import multiple_text_discpl


class LookAround(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.music_button_plus = Button("+", font_color=(255, 255, 255), step_x=-370, font_size=35)
        self.music_button_minus = Button("-", font_color=(255, 255, 255), step_x=-440, font_size=35)
        self.back = Button("Назад", font_color=(255, 255, 255), step_x=550, font_size=35, step_y=-250)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    # if self.music_button_plus[2].collidepoint(mouse_pos):
                    #     if Settings.music_volume + 0.1 <= 1:
                    #         Settings.music_volume += 0.1
                    #     else:
                    #         Settings.music_volume = 1.0
                    # elif self.music_button_minus[2].collidepoint(mouse_pos):
                    #     if Settings.music_volume - 0.1 >= 0:
                    #         Settings.music_volume -= 0.1
                    #     else:
                    #         Settings.music_volume = 0.0
                    # Settings.music_volume = round(Settings.music_volume, 1)
                    # pygame.mixer.music.set_volume(Settings.music_volume)
                    # if self.jump_button[2].collidepoint(mouse_pos):
                    #     if Settings.jump_key == "w":
                    #         Settings.jump_key = 'space'
                    #         self.jump_button = Button("пробел", font_size=25, step_x=-160)
                    #     else:
                    #         Settings.jump_key = 'w'
                    #         self.jump_button = Button("w", font_size=25, step_x=-160)
                    # if self.rightleft_button[2].collidepoint(mouse_pos):
                    #     if Settings.move_keys == "arrows":
                    #         Settings.move_keys = "ad"
                    #         self.rightleft_button = Button("ad", step_x=300, font_size=25)
                    #     else:
                    #         Settings.move_keys = "arrows"
                    #         self.rightleft_button = Button("стрелки", step_x=300, font_size=25)
                    # Settings.save_settings()
                    # if self.back[2].collidepoint(mouse_pos):
                    #     from .title import TitleScene
                    #     self.switch_scene(TitleScene())

    def render(self, screen):

        multiple_text_discpl(screen, """            С недобрым утром! Голова раскалывается...
           Эх, хорошо вчера видимо погулял, ничего не помню...
           Вроде бы пообещал себе завязывать с этими делами,
           ну что такое!.. Так, стоп, что это за комната?
           Не моя... И что-то она странная какая-то, как
           будто из 90-х... Надо бы осмотреться""", (140, 250), fontt='./resources/fonts/font.ttf', font_size=40)

        # pygame.draw.rect(screen, (0, 0, 0), self.rightleft_button[2])
        # screen.blit(self.rightleft_button[0], self.rightleft_button[1])
        # pygame.draw.rect(screen, (0, 0, 0), self.back[2])
        # screen.blit(self.back[0], self.back[1])
