from ._base import GameObject, AnimatedGameObject
from ..data import Path


class AnimationController:
    def __init__(self):
        self.counter = 0
        self.count_to_switch = 25

        self.state = 'idle'

        self.is_facing_right = True
        self.facing_buffer = self.is_facing_right


class Player(AnimatedGameObject):
    def __init__(self, filename, columns, rows, *groups, x=1, y=1):
        super().__init__(
            self.load_image(filename, 'player', transparent=True),
            columns, rows, *groups, x=x, y=y, mult=3
        )
        self.rect.x = 200
        self.rect.y = 200
        self.animation = AnimationController()

        self.key_state = (False, 0, 0)

    def switch_state(self, state, count_to_switch):
        if self.animation.state != state:
            self.cur_frame = 0
            self.frames = []
            print(f'switching state to {state}')
            match state:
                case 'idle':
                    sheet = self.load_image('idle', 'player', transparent=True)
                    self.cut_sheet(sheet, 4, 2, mult=3, x=self.rect.x, y=self.rect.y)
                    self.animation.state = 'idle'
                    self.animation.count_to_switch = count_to_switch

                case 'walk':
                    sheet = self.load_image('walk', 'player', transparent=True)
                    self.cut_sheet(sheet, 8, 2, mult=3, x=self.rect.x, y=self.rect.y)
                    self.animation.state = 'walk'
                    self.animation.count_to_switch = count_to_switch

    def play_next_animation_frame(self):
        # print('changing frame')
        self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
        # print(self.cur_frame)
        if self.animation.is_facing_right:
            self.image = self.frames[self.cur_frame]
        else:
            self.image = self.frames[self.cur_frame + (len(self.frames) // 2)]
        self.animation.counter = 0

    def update(self, *args, **kwargs):
        move_x = kwargs.get('move_x', 0)
        move_y = kwargs.get('move_y', 0)
        if 'keydown' in args:
            self.key_state = (True, move_x, move_y)
        elif 'keyup' in args:
            self.key_state = (False, 0, 0)

        if self.key_state[0]:
            self.switch_state('walk', 10)
            if self.key_state[1]:
                self.rect = self.rect.move(
                    self.key_state[1], 0
                )
                if self.key_state[1] > 0:
                    self.animation.is_facing_right = True
                else:
                    self.animation.is_facing_right = False
            elif self.key_state[2]:
                self.rect = self.rect.move(
                    0, move_y
                )
        else:
            self.switch_state('idle', 25)

        if self.animation.facing_buffer != self.animation.is_facing_right:
            self.play_next_animation_frame()
            self.animation.facing_buffer = self.animation.is_facing_right

        self.animation.counter += 1
        if self.animation.counter >= self.animation.count_to_switch:
            self.play_next_animation_frame()
            self.animation.counter = 0

    def to_save_dict(self):
        return {
            'oid': 'player',
            'x': self.rect.x,
            'y': self.rect.y
        }
