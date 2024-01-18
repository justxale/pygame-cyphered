import pygame

from .base import BaseScene
from .subscenes.pause import PauseSubscene
from ..data import Path, constants, dev
from ..objects import Player
from ..objects.base import GameObject
from ..objects.tiles import Tile, Tileset, TriggerTile, HiddenTile
from ..services.save import Saver
from ..services.sound import SoundMixer
from ..ui.Text_displ import text_displ
from ..services.settings import Settings


class PlayScene(BaseScene):
    def __init__(self, level_name: str = 'level1', save_data=None):
        BaseScene.__init__(self)
        Saver.listened_objects.clear()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.main_tileset = Tileset('tiles', 10, 15, mult=4)
        self.decorations = Tileset('decor', 3, 3, mult=4)
        # self.objects = Tileset('objects', )

        self.floor_rects = []
        self.wall_rects = {
            'left': [],
            'right': []
        }
        self.triggers = {}
        self.interact_rects = []

        self.bg = GameObject(self.all_sprites)
        self.bg._load_image(Path.sprite('bg'))
        self.player = None

        if save_data:
            self.level_name = save_data.level_name
            self.generate_level(save_data)
        else:
            self.level_name = level_name
            self.generate_level()

        self.text = ''

    def parse_player_data(self):
        level_data = Path.data(self.level_name, ext='txt')
        with open(level_data, 'r', encoding='utf-8') as f:
            data = f.readline()
            player_data = data.strip().split(',')

        return player_data

    def generate_level(self, save_data=None):
        self.floor_rects.clear()
        self.wall_rects = {
            'left': [],
            'right': []
        }
        self.interact_rects.clear()
        self.triggers.clear()

        self.tiles.empty()
        self.all_sprites.empty()

        self.enemies.empty()

        self.bg = GameObject(self.all_sprites)
        self.bg._load_image(Path.sprite('bg'))

        if self.player is None:
            self.player_group.empty()
            if not save_data:
                player_data = self.parse_player_data()
                self.player = Player(
                    'new_idle', 4, 2, self,  self.player_group,
                    x=int(player_data[0]), y=int(player_data[1])
                )
            else:
                self.player = Player(
                    'new_idle', 4, 2, self, self.player_group,
                    x=save_data.player['x'], y=save_data.player['y']
                )

        level_data = Path.data(self.level_name, ext='txt')
        with open(level_data, 'r', encoding='utf-8') as f:
            level_data = f.readlines()

        for y, line in enumerate(level_data[1:]):
            for x, tile in enumerate(line.split('; ')):
                if tile == '-':
                    continue
                tile_list = tile.split(',')
                if len(tile_list) == 4:
                    t, i, h, w = tile_list

                    if t == 'h':
                        new_tile = TriggerTile(
                            int(i), (int(h), int(w)), (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]), 4,
                            self.all_sprites, self.tiles
                        )
                        if not self.triggers.get(i, False):
                            self.triggers[int(i)] = []
                        self.triggers[int(i)].append(new_tile.rect)
                        continue

                    elif t == 'hi':
                        hide_trigger = TriggerTile(
                            int(i), (int(h), int(w)), (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]), 4,
                            self.all_sprites, self.tiles
                        )
                        for hy in range(int(w)):
                            for hx in range(int(h)):
                                HiddenTile(
                                    int(i), (1, 1),
                                    (hx + x + constants.LEVEL_OFFSET[0], hy + y + constants.LEVEL_OFFSET[1]), 4,
                                    (self.player, hide_trigger), self.all_sprites, self.tiles
                                )
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
                        self.all_sprites, self.tiles, tile_layer=0
                    )
                    self.interact_rects.append(new_tile.rect)
                else:
                    if 'lw' in types:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles, tile_layer=2
                        )
                        self.wall_rects['left'].append(new_tile.rect)
                    if 'rw' in types:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles, tile_layer=2
                        )
                        self.wall_rects['right'].append(new_tile.rect)
                    if 'f' in types:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles, tile_layer=2
                        )
                        self.floor_rects.append(new_tile.rect)
                    else:
                        new_tile = Tile(
                            self.main_tileset, (int(i), int(j)),
                            (x + constants.LEVEL_OFFSET[0], y + constants.LEVEL_OFFSET[1]),
                            self.all_sprites, self.tiles, tile_layer=2
                        )
        print(self.all_sprites.layers())

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            from .subscenes.furniture import Furniture
            # self.open_subscene(Furniture(self, self.level_name, interaction_i))
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if not self.is_paused and Settings.move_keys == 'arrows':
                            self.player_group.update('keydown', move_x=2, k='left')
                    case pygame.K_a:
                        if not self.is_paused and Settings.move_keys == 'ad':
                            self.player_group.update('keydown', move_x=2, k='left')
                    case pygame.K_RIGHT:
                        if not self.is_paused and Settings.move_keys == 'arrows':
                            self.player_group.update('keydown', move_x=2, k='right')
                    case pygame.K_d:
                        if not self.is_paused and Settings.move_keys == 'ad':
                            self.player_group.update('keydown', move_x=2, k='right')
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
                    # case pygame.K_f:
                    #     interaction_f = self.player.rect.collidelist(self.)
                    case pygame.K_r:
                        self.generate_level()
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
        if self.triggers.get(1) and self.player.rect.collidelist(self.triggers[1]) != -1:
            if not self.is_paused:
                match self.level_name:
                    case 'level1':
                        self.fade_and_switch_scene(PlayScene('level2'))
                    case 'level2':
                        self.fade_and_switch_scene(PlayScene('level1'))
                self.is_paused = True

    def render(self, screen):
        screen.fill(constants.BG_COLOR)
        self.all_sprites.draw(screen)
        self.player_group.draw(screen)
        if dev.DEBUG:
            for sprite in self.all_sprites.sprites() + [self.player]:
                if type(sprite) is TriggerTile:
                    if sprite.id == 1:
                        pygame.draw.rect(screen, (255, 0, 0), sprite.rect, 2, 1)
                    elif sprite.id == 3:
                        pygame.draw.rect(screen, (255, 0, 255), sprite.rect, 2, 1)
                elif sprite.rect in self.interact_rects:
                    pygame.draw.rect(screen, (0, 0, 255), sprite.rect, 2, 1)
                elif type(sprite) is HiddenTile:
                    pass
                else:
                    pygame.draw.rect(screen, (0, 255, 0), sprite.rect, 2, 1)
        if not self.is_paused:
            self.all_sprites.update()
            self.player_group.update()

        text_displ(self.text, screen, font_size=24, step_y=300, step_x=-350)

    def on_destroy(self):
        self.all_sprites.empty()
        self.player_group.empty()
        self.tiles.empty()
        self.interact_rects.clear()
