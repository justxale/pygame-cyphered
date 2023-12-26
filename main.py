import pygame

from cyphered.scenes._base import BaseScene
from cyphered.ui.Multiple_text_displ import multiple_text_discpl
from cyphered.data import constants
from cyphered.services.sound import SoundMixer
from cyphered.services.settings import Settings
from cyphered.scenes import TitleScene, SettingsScene

Settings.load_settings()


def start_game(screen_size, fps, starting_scene):

    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Cyphered')
    SoundMixer()  # объект класса плеера
    running = True

    active_scene: BaseScene = starting_scene

    while active_scene and running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        active_scene.process_events(events)
        active_scene.update()
        active_scene.render(screen)

        active_scene = active_scene.next

        #    for event in pygame.event.get():
        #        if event.type == pygame.MOUSEBUTTONDOWN:
        #            if event.button == 1:
        #                mouse_pos = pygame.mouse.get_pos()
        #                if start_button[2].collidepoint(mouse_pos):
        #                    start_button_clicked = True
        #                    break
        #                if settings_button[2].collidepoint(mouse_pos):
        #                    settings_button_clicked = True
        #                    break
#
        #
        #
        #
        #    while settings_button_clicked and running:
        #        screen.fill("black")
#
        #        pygame.display.flip()
#
        #screen.fill("black")
#
        #while not background_lookaround_button_clicked and running:
#
        #    screen.fill((0, 0, 0))
        #    background_lookaround_button = Button("Осмотреться", step_x=500, step_y=-200)
        #    pygame.draw.rect(screen, (0, 0, 0), background_lookaround_button[2])
        #    screen.blit(background_lookaround_button[0], background_lookaround_button[1])
#
        #    fontt = pygame.font.SysFont('./Resources/font.ttf', 40)
        #    multiple_text_discpl(screen, """        С недобрым утром! Голова раскалывается...
        #    Эх, хорошо вчера видимо погулял, ничего не помню...
        #    Вроде бы пообещал себе завязывать с этими делами,
        #    ну что такое!.. Так, стоп, что это за комната?
        #    Не моя... И что-то она странная какая-то, как
        #    будто из 90-х... Надо бы осмотреться""", (140, 250), fontt)
#
        #    pygame.display.flip()
#
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            running = False
        #            break
        #        if event.type == pygame.MOUSEBUTTONDOWN:
        #            if event.button == 1:
        #                mouse_pos = pygame.mouse.get_pos()
        #                if background_lookaround_button[2].collidepoint(mouse_pos):
        #                    background_lookaround_button_clicked = True
        #                    break

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    start_game(constants.SCREEN_SIZE, constants.FPS, TitleScene())
    pygame.quit()
