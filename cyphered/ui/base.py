import os
from ..data.constants import SCREEN_SIZE
from ..data.paths import FONTS_PATH
import pygame


# Класс кнопки. Для создания достаточно вызвать Button(*параметры*)
class Button:
    def __new__(
            cls, text: str, screen_size: tuple[int, int] = SCREEN_SIZE, font_size: int = 48,
            font_color: tuple[int, int, int] = (255, 255, 255),
            step_x: int = 0, step_y: int = 0
    ):
        font = pygame.font.Font(os.path.join(FONTS_PATH, 'ds_pixel_regular.ttf'), font_size)
        text_surface = font.render(text, True, font_color)

        button_width = text_surface.get_width() + 20
        button_height = text_surface.get_height() + 20
        button_x = (screen_size[0] - button_width) // 2 + step_x
        button_y = (screen_size[1] - button_height) // 2 + step_y

        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        text_rect = text_surface.get_rect(center=button_rect.center)

        return text_surface, text_rect, button_rect


class ProgressBar:
    ...
