import pygame


# функция, принимает текст, холст, ширину и высоту экрана, шрифт, размер шрифта, цвет, отступ от центру по горизотнтали
# и по вертикали
# функция отрисовывает на экране текст, я ее реализовала для облегчения работы с сюжеткой, которую мы рассказываем
# игроку
def text_displ(text_surface, screen, width=1280, height=780, font1=None, font_size=50, color=(255, 255, 255), step_x=0, step_y=0):
    font = pygame.font.Font(font1, font_size)
    text = font.render(text_surface, True, color)
    text_x = width // 2 - text.get_width() // 2 + step_x
    text_y = height // 2 - text.get_height() // 2 + step_y
    screen.blit(text, (text_x, text_y))