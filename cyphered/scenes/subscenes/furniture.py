import pygame
from ...scenes.base import BaseSubscene
from ...data.constants import SCREEN_SIZE
from ...ui.Multiple_text_displ import multiple_text_discpl


class Furniture(BaseSubscene):
    def __init__(self, parent_scene, level_name, sign_number):
        super().__init__(parent_scene)
        self.i = sign_number
        self.level_i = level_name

    def render(self, screen: pygame.Surface):
        super().render(screen)
        s = pygame.Surface(SCREEN_SIZE)
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        # надо открыть картинку увеличенную, на нее еще надо добавить фрагмент текста
