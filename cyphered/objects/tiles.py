import pygame

from ..data import constants
from ..objects.base import GameObject


class Tileset:
    def __init__(self, tileset_name, columns, rows, mult=1):
        super().__init__()
        self.tiles_surfaces = {}
        self.path = tileset_name
        self.tile_size = constants.TILE_SIZE
        self.tiles = []
        self.multiplier = mult
        self.parse_tiles(GameObject.load_image(tileset_name, transparent=True), columns, rows, mult=mult)

    def parse_tiles(self, sheet, columns, rows, mult):
        # self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.tile_size * j, self.tile_size * i)
                subsurface = sheet.subsurface(pygame.Rect(
                    frame_location, (self.tile_size, self.tile_size))
                )
                new_size = (subsurface.get_size()[0] * mult, subsurface.get_size()[1] * mult)
                result = pygame.transform.scale(
                    subsurface, new_size
                )
                self.tiles_surfaces[j + 1, i + 1] = result

    def get_tile(self, i, j):
        return self.tiles_surfaces[i, j]


class Tile(pygame.sprite.Sprite):
    def __init__(self, tileset: Tileset, tile_sprite: tuple[int, int], coords: tuple[int, int], *groups, tile_layer=-1):
        super().__init__()
        self.tileset = tileset
        if tile_layer != -1:
            self.layer = tile_layer
        for g in groups:
            g.add(self)
        self.image = tileset.get_tile(*tile_sprite)
        self.rect = self.image.get_rect().move(
            constants.TILE_SIZE * coords[0] * self.tileset.multiplier,
            constants.TILE_SIZE * coords[1] * self.tileset.multiplier
        )
        tileset.tiles.append(self)

    def change_tile(self, new_tile: tuple[int, int]):
        self.image = self.tileset.get_tile(*new_tile)


class TriggerTile(pygame.sprite.Sprite):
    def __init__(self, trigger_id, size: tuple[int, int], coords: tuple[int, int], multiplier, *groups):
        super().__init__(*groups)
        self.id = trigger_id
        self.image = pygame.Surface((
            constants.TILE_SIZE * multiplier * size[0],
            constants.TILE_SIZE * multiplier * size[1]
        ))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect().move(
            constants.TILE_SIZE * coords[0] * multiplier,
            constants.TILE_SIZE * coords[1] * multiplier,
        )


class HiddenTile(TriggerTile):
    def __init__(self, trigger_id, size: tuple[int, int], coords: tuple[int, int], multiplier, rects, *groups):
        super().__init__(trigger_id, size, coords, multiplier)
        self.layer = 3
        self.rects = rects
        for g in groups:
            g.add(self)
        self.tileset = Tileset('tiles', 10, 15, mult=4)
        self.image = self.tileset.get_tile(2, 3)
        self.alpha_counter = 255

    def update(self, *args, **kwargs):
        if pygame.sprite.collide_rect(self.rects[0], self.rects[1]):
            if self.alpha_counter >= 0:
                self.alpha_counter -= 4
        else:
            if self.alpha_counter <= 255:
                self.alpha_counter += 4
        self.image.set_alpha(self.alpha_counter)

