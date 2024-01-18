from ..data import Path
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.is_listened = False
        self.rect = pygame.Rect(0, 0, 1, 1)

    def self_load_image(self, filename, transparent=False):
        path = filename
        image = pygame.image.load(path)
        if transparent:
            image = image.convert_alpha()
        else:
            image = image.convert()
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
        self.rect = self.rect.move(x, y)
        self.animation = AnimationController()

    def cut_sheet(self, sheet: pygame.Surface, columns, rows, mult=1, x=0, y=0):
        self.rect = pygame.Rect(x, y, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                subsurface = sheet.subsurface(pygame.Rect(frame_location, self.rect.size))
                new_size = (subsurface.get_size()[0] * mult, subsurface.get_size()[1] * mult)
                result = pygame.transform.scale(
                    subsurface, new_size
                )
                self.frames.append(result)
        self.rect = pygame.Rect(x, y, self.frames[0].get_rect().w, self.frames[0].get_rect().h)

    def play_next_animation_frame(self):
        # print('changing frame')
        self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
        # print(self.cur_frame)
        if self.animation.is_facing_right:
            self.image = self.frames[self.cur_frame]
        else:
            self.image = self.frames[self.cur_frame + (len(self.frames) // 2)]
        self.animation.counter = 0

    def update(self):
        if self.animation.facing_buffer != self.animation.is_facing_right:
            self.play_next_animation_frame()
            self.animation.facing_buffer = self.animation.is_facing_right

        self.animation.counter += 1
        if self.animation.counter >= self.animation.count_to_switch:
            self.play_next_animation_frame()
            self.animation.counter = 0


class AnimationController:
    def __init__(self):
        self.counter = 0
        self.count_to_switch = 25

        self.state = 'idle'

        self.is_facing_right = True
        self.facing_buffer = self.is_facing_right
