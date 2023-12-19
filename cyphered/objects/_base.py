from ..data import Path
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        ...

    def _load_image(self, filename, colorkey=None):
        path = Path.sprite(filename)
        image = pygame.image.load(path)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        self.image = image

    def update(self, *args, **kwargs):
        pass
