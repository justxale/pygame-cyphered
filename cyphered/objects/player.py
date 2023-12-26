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

        self.animation_counter = 0
        self.is_facing_right = True
        self.animation_buffer = self.is_facing_right

        self.key_state = (False, 0, 0)

    def play_next_animation_frame(self):
        self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
        if self.is_facing_right:
            self.image = self.frames[self.cur_frame]
        else:
            self.image = self.frames[self.cur_frame + 4]
        self.animation_counter = 0

    def update(self, *args, **kwargs):
        move_x = kwargs.get('move_x', 0)
        move_y = kwargs.get('move_y', 0)
        if 'keydown' in args:
            self.key_state = (True, move_x, move_y)
        elif 'keyup' in args:
            self.key_state = (False, 0, 0)

        if self.key_state[0]:
            if self.key_state[1]:
                self.rect = self.rect.move(
                    self.key_state[1], 0
                )
                if self.key_state[1] > 0:
                    self.is_facing_right = True
                else:
                    self.is_facing_right = False
            elif self.key_state[2]:
                self.rect = self.rect.move(
                    0, move_y
                )

        if self.animation_buffer != self.is_facing_right:
            self.play_next_animation_frame()
            self.animation_buffer = self.is_facing_right

        self.animation_counter += 1
        if self.animation_counter >= 25:
            self.play_next_animation_frame()
            self.animation_counter = 0

    def to_save_dict(self):
        return {
            'oid': 'player',
            'x': self.rect.x,
            'y': self.rect.y
        }
