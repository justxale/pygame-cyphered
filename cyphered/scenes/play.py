from .base import BaseScene
from .subscenes.pause import PauseSubscene
from ..data import Path, constants
from ..objects import Player
import pygame

from ..objects.enemies import Crab
from ..objects.tiles import Tile, Tileset
from ..services.save import Saver
from ..services.sound import SoundMixer

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
tiles = pygame.sprite.Group()


class PlayScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        all_sprites.empty()
        enemies.empty()
        player.empty()
        tiles.empty()

        self.tileset = Tileset('tiles', 10, 15, mult=4)
        self.generate_level('level1')

        self.player = Player(
            'idle', 4, 2, all_sprites, player
        )

        self.crab = Crab(all_sprites, enemies)

    def generate_level(self, level_name: str):
        level_data = Path.data(level_name, ext='txt')
        with open(level_data, 'r', encoding='utf-8') as f:
            level_data = f.readlines()
        for y, line in enumerate(level_data):
            for x, tile in enumerate(line.split('; ')):
                i, j = map(int, tile.split(','))
                Tile(
                    self.tileset, (i, j),
                    (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                    all_sprites, tiles
                )

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
                            SoundMixer.pause_music()
                            self.is_paused = True
                        elif self.subscene:
                            self.subscene.destroy()
                            SoundMixer.unpause_music()
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
        screen.fill(constants.BG_COLOR)
        all_sprites.draw(screen)
        if not self.is_paused:
            all_sprites.update()

    def on_destroy(self):
        Saver.listened_objects.clear()
