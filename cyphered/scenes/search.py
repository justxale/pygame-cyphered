import pygame

from .base import BaseScene
from ..ui import Button
from ..services.settings import Settings
from cyphered.ui.Text_displ import text_displ
from ..services.sound import SoundMixer


class SearchScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)

        self.back_button = Button("Назад", step_x=-400, step_y=-50)
        self.buttons = [self.back_button]

        if not SoundMixer.music_loaded:
            SoundMixer.play_music("redwood_colonnade")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button[2].collidepoint(mouse_pos):
                        # self.switch_scene(LookAround())
                        from .title import TitleScene
                        self.fade_and_switch_scene(TitleScene())
                        SoundMixer.switch_music('background_music')
                        break

    def render(self, screen):
        for button in self.buttons:
            pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
        text_displ("Вы заблудились! Чтобы выбраться из этого места, ",
                   screen, step_x=200, step_y=-310, font_size=25)
        text_displ("Вам предстоит пройти множество испытаний.",
                   screen, step_x=200, step_y=-260, font_size=25)
        text_displ("Вам нужно передвигаться из локации в локацию",
                   screen, step_x=200, step_y=-210, font_size=25)
        text_displ("Чтобы открыть двери от локаций, вам нужно",
                   screen, step_x=200, step_y=-160, font_size=25)
        text_displ("Собирать по элементам локаций части текста,",
                   screen, step_x=200, step_y=-110, font_size=25)
        text_displ("Который надо будет расшифровать. Чтобы ",
                   screen, step_x=200, step_y=-60, font_size=25)
        text_displ("Проивзаимодействовать с объектов, вам следует",
                   screen, step_x=200, step_y=-10, font_size=25)
        text_displ("Подойти к нему вплотную и начать F. После ",
                   screen, step_x=200, step_y=40, font_size=25)
        text_displ("этого Вам предоставится возможность рассмотреть",
                   screen, step_x=200, step_y=90, font_size=25)
        text_displ("Его вбизи. Если Вы заметите на нем фрагмент",
                   screen, step_x=200, step_y=140, font_size=25)
        text_displ("Текста, нажмите на него левой кнопкой мыши.",
                   screen, step_x=200, step_y=190, font_size=25)
        text_displ("После расшифровки текста, Вы сможете получить",
                   screen, step_x=200, step_y=240, font_size=25)
        text_displ("Ключ от следующего уровня и откроете дверь.",
                   screen, step_x=200, step_y=290, font_size=25)
        text_displ("Удачи в игре!",
                   screen, step_x=-400, step_y=240, font_size=25)