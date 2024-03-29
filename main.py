import pygame

from cyphered.scenes.base import BaseScene
from cyphered.services.fps import FPS
from cyphered.data import constants
from cyphered.services.sound import SoundMixer
from cyphered.services.settings import Settings
from cyphered.scenes import TitleScene

Settings.load_settings()


def start_game(screen, fps, starting_scene):

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

        fps_display.render(screen)
        pygame.display.flip()
        fps_display.clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    start_game(screen, constants.FPS, TitleScene())
    pygame.quit()
