import pygame

from .base import BaseScene
from .subscenes.pause import PauseSubscene
from ..data import Path, constants, dev
from ..objects import Player
from ..objects.base import GameObject
from ..objects.enemies import Crab
from ..objects.tiles import Tile, Tileset, TriggerTile
from ..services.save import Saver
from ..services.sound import SoundMixer
from ..ui.Text_displ import text_displ


class PlayScene(BaseScene):
    def __init__(self, level_name: str = 'level1'):
        BaseScene.__init__(self)
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.main_tileset = Tileset('tiles', 10, 15, mult=4)
        self.decorations = Tileset('decor', 3, 3, mult=4)

        self.floor_rects = []
        self.wall_rects = {
            'left': [],
            'right': []
        }
        self.triggers = {}
        self.interact_rects = []

        self.bg = GameObject(self.all_sprites)
        self.bg._load_image(Path.sprite('bg'))

        self.level_name = level_name
        player_data = self.generate_level(self.level_name)
        self.player = Player(
            'new_idle', 4, 2, self, self.all_sprites, self.player_group,
            x=int(player_data[0]), y=int(player_data[1])
        )
        self.crab = Crab(self.all_sprites, self.enemies)

        self.text = ''

    def generate_level(self, level_name: str):
        self.floor_rects.clear()
        self.wall_rects = {
            'left': [],
            'right': []
        }
        self.interact_rects.clear()

        self.triggers.clear()

        self.tiles.empty()
        self.all_sprites.empty()

        self.bg = GameObject(self.all_sprites)
        self.bg._load_image(Path.sprite('bg'))

        level_data = Path.data(level_name, ext='txt')
        with open(level_data, 'r', encoding='utf-8') as f:
            level_data = f.readlines()
            player_data = level_data[0].strip().split(',')

        for y, line in enumerate(level_data[1:]):
            for x, tile in enumerate(line.split('; ')):
                if tile == '-':
                    continue
                tile_list = tile.split(',')
                if len(tile_list) == 4:
                    t, i, h, w = tile_list

                    new_tile = TriggerTile(
                        int(i), (int(h), int(w)), (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]), 4,
                        self.all_sprites, self.tiles
                    )

                    if not self.triggers.get(i, False):
                        self.triggers[int(i)] = []
                    self.triggers[int(i)].append(new_tile.rect)
                    continue
                elif len(tile_list) == 3:
                    i, j, t = tile_list
                else:
                    continue
                types = list(map(str.strip, t.split('+')))
                if 'i' in types:
                    new_tile = Tile(
                        self.decorations, (int(i), int(j)),
                        (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                        self.all_sprites, self.tiles
                    )
                    self.interact_rects.append(new_tile.rect)
                else:
                    if 'lw' in types:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles
                        )
                        self.wall_rects['left'].append(new_tile.rect)
                    if 'rw' in types:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles
                        )
                        self.wall_rects['right'].append(new_tile.rect)
                    else:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles
                        )
                        self.floor_rects.append(new_tile.rect)
        return player_data

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        if not self.is_paused:
                            self.player_group.update('keydown', move_x=2, k='left')
                    case pygame.K_RIGHT | pygame.K_d:
                        if not self.is_paused:
                            self.player_group.update('keydown', move_x=2, k='right')
                    case pygame.K_UP:
                        self.player_group.update()
                    case pygame.K_ESCAPE:
                        if not self.is_paused:
                            self.open_subscene(PauseSubscene(self))
                            SoundMixer.pause_music()
                            self.is_paused = True
                        elif self.subscene:
                            self.subscene.destroy()
                            SoundMixer.unpause_music()
                            self.is_paused = False
                    case pygame.K_e:
                        interaction_i = self.player.rect.collidelist(self.interact_rects)
                        if interaction_i != -1:
                            if not self.is_paused:
                                from .subscenes.signs import SignSubscene
                                self.open_subscene(SignSubscene(self, self.level_name, interaction_i))
                                self.is_paused = True
                            elif self.subscene:
                                self.subscene.destroy()
                                self.is_paused = False
                    case pygame.K_r:
                        self.generate_level(self.level_name)
                    case pygame.K_t:
                        dev.DEBUG = not dev.DEBUG
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        self.player_group.update('keyup', k='left')
                    case pygame.K_RIGHT | pygame.K_d:
                        self.player_group.update('keyup', k='right')
                    case pygame.K_UP:
                        self.player_group.update()

        if self.player.rect.collidelist(self.interact_rects) != -1:
            self.text = 'Нажмите E, чтоб заимодействовать.'
        else:
            self.text = ''
        if self.triggers.get(1) is not None and self.player.rect.collidelist(self.triggers[1]) != -1:
            if not self.is_paused:
                self.fade_and_switch_scene(PlayScene('level2'))
                self.is_paused = True

    def render(self, screen):
        screen.fill(constants.BG_COLOR)
        self.all_sprites.draw(screen)
        if dev.DEBUG:
            for sprite in self.all_sprites.spritedict.keys():
                if isinstance(sprite, TriggerTile):
                    pygame.draw.rect(screen, (255, 0, 0), sprite.rect, 2, 1)
                elif sprite.rect in self.interact_rects:
                    pygame.draw.rect(screen, (0, 0, 255), sprite.rect, 2, 1)
                else:
                    pygame.draw.rect(screen, (0, 255, 0), sprite.rect, 2, 1)
        if not self.is_paused:
            self.all_sprites.update()

        text_displ(self.text, screen, font_size=24, step_y=300, step_x=-350)

    def on_destroy(self):
        Saver.listened_objects.clear()
