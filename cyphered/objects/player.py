from ._base import GameObject, AnimatedGameObject
from ..data import Path


class Player(AnimatedGameObject):
    def __init__(self, filename, columns, rows, *groups, x=1, y=1):
        super().__init__(
            self.load_image(filename, 'player', transparent=True),
            columns, rows, *groups, x=x, y=y, mult=3
        )
        self.rect.x = 200
        self.rect.y = 200
        self.counter = 0

    def update(self, *args, **kwargs):
        self.counter += 1
        if self.counter >= 50:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.counter = 0
        move_x = kwargs.get('move_x')
        move_y = kwargs.get('move_y')


    def to_save_dict(self):
        return {
            'oid': 'player',
            'x': self.x,
            'y': self.y
        }
