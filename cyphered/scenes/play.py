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

    def render(self, screen):
        all_sprites.draw(screen)
        all_sprites.update()

