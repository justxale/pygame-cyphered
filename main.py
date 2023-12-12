import pygame
import cyphered
from cyphered.data import constants

# pygame setup
pygame.init()
screen = pygame.display.set_mode(constants.SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

    screen.fill("black")
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(constants.FPS)  # limits FPS to 60

pygame.quit()
