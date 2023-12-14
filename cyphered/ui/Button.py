import pygame


# функция для создания кнопки
# в качестве аргументов принимает ширину и высоту экрана, тект, цвет текста, насколько от середины отодвинуть
# текст по x и y, размер шрифта
def get_component_button(screen_width, screen_height, text, color=(255, 255, 255), step_x=0, step_y=0, font_size=50):
    font = pygame.font.Font(None, font_size)  # надо спросить у Артема, тк я сама не понимаю, какой путь прописывать
    # нужно для шрифта
    text_surface = font.render(text, True, color)

    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = (screen_width - button_width) // 2 + step_x
    button_y = (screen_height - button_height) // 2 + step_y

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    text_rect = text_surface.get_rect(center=button_rect.center)

    return (text_surface, text_rect, button_rect)