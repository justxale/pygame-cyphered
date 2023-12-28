import pygame

from cyphered.scenes.base import BaseScene
from cyphered.services.fps import FPS
from cyphered.data import constants
from cyphered.services.sound import SoundMixer
from cyphered.services.settings import Settings
from cyphered.scenes import TitleScene

Settings.load_settings()


def start_game(screen_size, fps, starting_scene):

    screen = pygame.display.set_mode(screen_size)
    # clock = pygame.time.Clock()
    fps_display = FPS()
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
        active_scene.update(screen)

        active_scene = active_scene.next
#
        #    fontt = pygame.font.SysFont('./Resources/font.ttf', 40)
        #    multiple_text_discpl(screen, """        С недобрым утром! Голова раскалывается...
        #    Эх, хорошо вчера видимо погулял, ничего не помню...
        #    Вроде бы пообещал себе завязывать с этими делами,
        #    ну что такое!.. Так, стоп, что это за комната?
        #    Не моя... И что-то она странная какая-то, как
        #    будто из 90-х... Надо бы осмотреться""", (140, 250), fontt)

        fps_display.render(screen)
        pygame.display.flip()
        fps_display.clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    start_game(constants.SCREEN_SIZE, constants.FPS, TitleScene())
    pygame.quit()
