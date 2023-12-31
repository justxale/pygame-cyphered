import os

import pygame

from cyphered.data.paths import FONTS_PATH


# функция для многострочного текста. принимает сам текст, холст, кортеж позиции, куда мы поместим угол текста,
# готовый через pygame сгенерированный шрифт, цвет
# отрисовывает текст на холсте
# пример вызова: font = pygame.font.SysFont("Arial", 50); multiple_text_discpl(screen, text, (20, 20), font)
def multiple_text_discpl(
        screen, text_surface, pos,
        fontfile=os.path.join(FONTS_PATH, 'ds_pixel_regular.ttf'), font_size=50,
        color=(255, 255, 255)
):
    words = [word.split(' ') for word in text_surface.splitlines()]  # 2D array where each row is a list of words.
    space = 14  # The width of a space.
    max_width, max_height = screen.get_size()
    x, y = pos
    font = pygame.font.Font(fontfile, font_size)
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.