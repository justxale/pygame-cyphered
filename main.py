import pygame
from cyphered.ui.Button import get_component_button
from cyphered.ui.Text_displ import text_displ
from cyphered.ui.Multiple_text_displ import multiple_text_discpl
from cyphered.ui.Sounds import SoundPlayer

with open('./Resources/settings') as f:
    rightleft, jump, music = tuple(map(str, f.readline().split(',')))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
start_button_clicked = False  # переменная нажатия кнопки "играть"
background_lookaround_button_clicked = False  # кнопка осмотреться в предыстории
settings_button_clicked = False  # кнопка настроек
flag = True  # вспомогательная переменная для плеера
player = SoundPlayer()  # объект класса плеера

while running:

    if music == 'on' and flag:
        player.play_music("Resources/background_music.mp3")
        flag = False

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
        start_button = get_component_button(1280, 720, "Играть", fontt='./Resources/font.ttf')
        pygame.draw.rect(screen, (0, 0, 0), start_button[2])
        screen.blit(start_button[0], start_button[1])

        settings_button = get_component_button(1280, 720, "Настройки", step_x=500, step_y=-300,
                                               fontt='./Resources/font.ttf')
        pygame.draw.rect(screen, (0, 0, 0), settings_button[2])
        screen.blit(settings_button[0], settings_button[1])

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
                    if settings_button[2].collidepoint(mouse_pos):
                        settings_button_clicked = True
                        break

        jump_button = get_component_button(1280, 720, "Прыжок", font_size=30, step_x=-170, fontt='./Resources/font.ttf')
        rightleft_button = get_component_button(1280, 720, "Управление кнопками влево-вправо", step_x=300,
                                                font_size=35, fontt='./Resources/font.ttf')
        while settings_button_clicked and running:
            screen.fill("black")
            color_music_button = 'green'
            if music == 'on':
                color_music_button = 'red'
            music_button = get_component_button(1280, 720, "Музыка", color=color_music_button, step_x=-430,
                                                font_size=35, fontt='./Resources/font.ttf')
            pygame.draw.rect(screen, (0, 0, 0), music_button[2])
            screen.blit(music_button[0], music_button[1])

            pygame.draw.rect(screen, (0, 0, 0), jump_button[2])
            screen.blit(jump_button[0], jump_button[1])

            pygame.draw.rect(screen, (0, 0, 0), rightleft_button[2])
            screen.blit(rightleft_button[0], rightleft_button[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if music_button[2].collidepoint(mouse_pos):
                            if music == 'on':
                                music = 'off'
                                music_button = get_component_button(1280, 720, "Музыка", color="red", step_x=-430,
                                                                    font_size=35, fontt='./Resources/font.ttf')
                                pygame.draw.rect(screen, (0, 0, 0), music_button[2])
                                screen.blit(music_button[0], music_button[1])
                            else:
                                music = 'on'
                                screen.fill(pygame.Color('black'), (music_button[3], music_button[4], music_button[5],
                                                                    music_button[6]))
                                music_button = get_component_button(1280, 720, "Музыка", color="green", step_x=-430,
                                                                    font_size=35, fontt='./Resources/font.ttf')
                                pygame.draw.rect(screen, (0, 0, 0), music_button[2])
                                screen.blit(music_button[0], music_button[1])

            pygame.display.flip()

    screen.fill("black")

    while not background_lookaround_button_clicked and running:

        screen.fill((0, 0, 0))
        background_lookaround_button = get_component_button(1280, 720, "Осмотреться", step_x=400, step_y=-200,
                                                            fontt='./Resources/font.ttf')
        pygame.draw.rect(screen, (0, 0, 0), background_lookaround_button[2])
        screen.blit(background_lookaround_button[0], background_lookaround_button[1])

        fontt = pygame.font.SysFont('./Resources/font.ttf', 40)
        multiple_text_discpl(screen, """        С недобрым утром! Голова раскалывается...
        Эх, хорошо вчера видимо погулял, ничего не помню...
        Вроде бы пообещал себе завязывать с этими делами,
        ну что такое!.. Так, стоп, что это за комната?
        Не моя... И что-то она странная какая-то, как
        будто из 90-х... Надо бы осмотреться""", (140, 250), fontt)

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
