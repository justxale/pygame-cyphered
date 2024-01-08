import pygame

from ..base import BaseSubscene
from ...services.save import Saver
from ...services.sound import SoundMixer
from ...ui.Multiple_text_displ import multiple_text_discpl
from ...data.constants import SCREEN_SIZE

FIRST_TEXT = """Ищи подсказки, разгадывай шифры,
Уйди отсюда живым. Удачи!~"""

SECOND_TEXT = """

"""

TEXTS = {
    0: FIRST_TEXT,
    1: SECOND_TEXT
}


class SignSubscene(BaseSubscene):
    def __init__(self, parent_scene, sign_number):
        super().__init__(parent_scene)
        self.i = sign_number

    def render(self, screen: pygame.Surface):
        super().render(screen)
        s = pygame.Surface(SCREEN_SIZE)
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        multiple_text_discpl(screen, TEXTS[self.i], (100, 100), font_size=24)
