import pygame

from ..base import BaseSubscene
from ...ui import Button
from ...data.constants import SCREEN_SIZE


class PauseSubscene(BaseSubscene):
    def __init__(self, parent):
        super().__init__(parent)
        self.continue_button = Button(
            'Продолжить', step_y=-100
        )
        self.save_and_exit_button = Button(
            'Сохранить и выйти', step_y=100
        )

        self.buttons = [self.save_and_exit_button, self.continue_button]

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.continue_button[2].collidepoint(mouse_pos):
                        self.parent_scene.is_paused = False
                        self.destroy()
                        break

                    if self.save_and_exit_button[2].collidepoint(mouse_pos):
                        ...
                        break

    def render(self, screen: pygame.Surface):
        super().render(screen)
        s = pygame.Surface(SCREEN_SIZE)
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        for button in self.buttons:
            # pygame.draw.rect(screen, (0, 0, 0), button[2])
            screen.blit(button[0], button[1])
