import pygame
from cyphered.ui.Button import get_component_button
from cyphered.ui.Text_displ import text_displ
from cyphered.ui.Multiple_text_displ import multiple_text_discpl

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
start_button_clicked = False  # переменная нажатия кнопки "играть"
background_lookaround_button_clicked = False  # кнопка осмотреться в предыстории

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

        screen.fill((0, 0, 0))
        start_button = get_component_button(1280, 720, "Играть")
        pygame.draw.rect(screen, (0, 0, 0), start_button[2])
        screen.blit(start_button[0], start_button[1])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button[2].collidepoint(mouse_pos):
                        start_button_clicked = True
                        break

    screen.fill("black")

    while not background_lookaround_button_clicked and running:

        screen.fill((0, 0, 0))
        background_lookaround_button = get_component_button(1280, 720, "Осмотреться", step_x=500, step_y=-200)
        pygame.draw.rect(screen, (0, 0, 0), background_lookaround_button[2])
        screen.blit(background_lookaround_button[0], background_lookaround_button[1])

        font = pygame.font.SysFont(None, 40)
        multiple_text_discpl(screen, """        С недобрым утром! Голова раскалывается...
        Эх, хорошо вчера видимо погулял, ничего не помню...
        Вроде бы пообещал себе завязывать с этими делами,
        ну что такое!.. Так, стоп, что это за комната?
        Не моя... И что-то она странная какая-то, как
        будто из 90-х... Надо бы осмотреться""", (140, 250), font)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if background_lookaround_button[2].collidepoint(mouse_pos):
                        background_lookaround_button_clicked = True
                        break

    screen.fill("black")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
