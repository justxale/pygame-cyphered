from ._base import BaseScene
from ..objects import Player, Trap
from ..data import Path
import pygame

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()


class PlayScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.player = Player(
            'idle', 4, 2, all_sprites, player
        )

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        player.update('keydown', move_x=-5)
                    case pygame.K_RIGHT | pygame.K_d:
                        player.update('keydown', move_x=5)
                    case pygame.K_UP:
                        player.update()
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        player.update('keyup')
                    case pygame.K_RIGHT | pygame.K_d:
                        player.update('keyup')
                    case pygame.K_UP:
                        player.update()

    def render(self, screen):
        all_sprites.draw(screen)
        all_sprites.update()

