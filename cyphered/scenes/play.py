from .base import BaseScene
from .subscenes.pause import PauseSubscene
from ..objects import Player
import pygame

from ..objects.enemies import Crab
from ..services.save import Saver

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()


class PlayScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        all_sprites.empty()
        enemies.empty()
        player.empty()

        self.player = Player(
            'idle', 4, 2, all_sprites, player
        )

        self.crab = Crab(all_sprites, enemies)
        self.is_paused = False

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        if not self.is_paused:
                            player.update('keydown', move_x=2, k='left')
                    case pygame.K_RIGHT | pygame.K_d:
                        if not self.is_paused:
                            player.update('keydown', move_x=2, k='right')
                    case pygame.K_UP:
                        player.update()
                    case pygame.K_ESCAPE:
                        if not self.is_paused:
                            self.open_subscene(PauseSubscene(self))
                            self.is_paused = True
                        elif self.subscene:
                            self.subscene.destroy()
                            self.is_paused = False
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        player.update('keyup', k='left')
                    case pygame.K_RIGHT | pygame.K_d:
                        player.update('keyup', k='right')
                    case pygame.K_UP:
                        player.update()

    def render(self, screen):
        all_sprites.draw(screen)
        if not self.is_paused:
            all_sprites.update()

    def on_destroy(self):
        Saver.listened_objects.clear()
