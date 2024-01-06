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
    def __init__(self, tileset: Tileset, tile_type: tuple[int, int], coords: tuple[int, int], *groups):
        super().__init__(*groups)
        self.image = tileset.get_tile(*tile_type)
        self.rect = self.image.get_rect().move(
            constants.TILE_SIZE * coords[0] * tileset.multiplier,
            constants.TILE_SIZE * coords[1] * tileset.multiplier
        )
        tileset.tiles.append(self)
