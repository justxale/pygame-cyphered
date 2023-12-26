from ..data import Path
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.is_listened = False

    def _load_image(self, filename, colorkey=None):
        path = filename
        image = pygame.image.load(path)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        self.image = image

    @staticmethod
    def load_image(filename, *dirs, transparent=False):
        fullname = Path.sprite(filename, *dirs)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', filename)
            raise SystemExit(message)

        if transparent:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    def update(self, *args, **kwargs):
        pass

    def to_save_dict(self):
        return {
            'oid': 'empty_gameobject'
        }


class AnimatedGameObject(GameObject):
    def __init__(self, sheet, columns, rows, *groups, x=1, y=1, mult=1):
        super().__init__(*groups)
        self.frames: list[pygame.Surface] = []
        self.cut_sheet(sheet, columns, rows, mult=mult)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        print(x, y)
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet: pygame.Surface, columns, rows, mult=1):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                subsurface = sheet.subsurface(pygame.Rect(frame_location, self.rect.size))
               # subsurface = subsurface.convert_alpha()
                new_size = (subsurface.get_size()[0] * mult, subsurface.get_size()[1] * mult)
                # result = pygame.Surface(new_size)
                result = pygame.transform.scale(
                    subsurface, new_size
                )
                # result = result.convert_alpha()
                self.frames.append(result)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
