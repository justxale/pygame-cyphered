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


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
start_button_clicked = False  # переменная нажатия кнопки "играть"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    while not start_button_clicked and running:
        button = get_component_button(1280, 720, 'Войти')
        pygame.draw.rect(screen, (0, 0, 0), button[2])
        screen.blit(button[0], button[1])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        start_button_clicked = True
                        break

    screen.fill("purple")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()