import pygame

from ._base import BaseScene
from ..ui import Button


class SettingsScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.jump_button = Button("Прыжок", font_size=30, step_x=-170)  # fontt='./Resources/font.ttf')
        self.rightleft_button = Button(
            "Управление кнопками влево-вправо", step_x=300, font_size=35
        )

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('boo')
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.music_button[2].collidepoint(mouse_pos):
                        if music == 'on':
                            music = 'off'
                            self.music_button = Button(
                                "Музыка", font_color=(255, 0, 0), step_x=-430, font_size=35
                            )
                        else:
                            music = 'on'
                            self.music_button = Button(
                                "Музыка", font_color=(0, 255, 0), step_x=-430, font_size=35
                            )

    def render(self, screen):
        color_music_button = (0, 255, 0)
        if music == 'on':
            color_music_button = (255, 0, 0)
        music_button = Button("Музыка", font_color=color_music_button, step_x=-430,
                              font_size=35)  # fontt='./Resources/font.ttf')
        pygame.draw.rect(screen, (0, 0, 0), music_button[2])
        screen.blit(music_button[0], music_button[1])
        pygame.draw.rect(screen, (0, 0, 0), self.jump_button[2])
        screen.blit(self.jump_button[0], self.jump_button[1])
        pygame.draw.rect(screen, (0, 0, 0), self.rightleft_button[2])
        screen.blit(self.rightleft_button[0], self.rightleft_button[1])
