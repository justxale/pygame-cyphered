import pygame

from .base import AnimatedGameObject, AnimationController
from ..services.save import Saver


class Player(AnimatedGameObject):
    def __init__(self, filename, columns, rows, play_scene,  *groups, x=0, y=0):
        super().__init__(
            self.load_image(filename, 'player', transparent=True),
            columns, rows, *groups, x=x, y=y, mult=3
        )
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.animation = AnimationController()
        self.scene = play_scene
        Saver.add(self)

        self.key_state = [False, False, 0]

    def switch_state(self, state, count_to_switch):
        if self.animation.state != state:
            self.cur_frame = 0
            self.frames = []
            print(f'switching animation state to {state}')
            match state:
                case 'idle':
                    sheet = self.load_image('new_idle', 'player', transparent=True)
                    self.cut_sheet(sheet, 4, 2, mult=3, x=self.rect.x, y=self.rect.y)
                    self.animation.state = 'idle'
                    self.animation.count_to_switch = count_to_switch

                case 'walk':
                    sheet = self.load_image('new_walk', 'player', transparent=True)
                    self.cut_sheet(sheet, 8, 2, mult=3, x=self.rect.x, y=self.rect.y)
                    self.animation.state = 'walk'
                    self.animation.count_to_switch = count_to_switch

    def update(self, *args, **kwargs):
        move_x = kwargs.get('move_x', 0)
        move_y = kwargs.get('move_y', 0)
        if 'keydown' in args:
            if kwargs.get('k') == 'left':
                self.key_state[0] = True
            if kwargs.get('k') == 'right':
                self.key_state[1] = True
            self.key_state[2] = move_x
        elif 'keyup' in args:
            if kwargs.get('k') == 'left':
                self.key_state[0] = False
            if kwargs.get('k') == 'right':
                self.key_state[1] = False

        is_colliding_walls = (self.rect.collidelist(self.scene.wall_rects['left']) != -1 or
                              self.rect.collidelist(self.scene.wall_rects['right']) != -1)
        is_colliding_floor = self.rect.collidelist(self.scene.floor_rects) != -1

        if self.key_state[0] and self.rect.collidelist(self.scene.wall_rects['left']) == -1:
            self.rect = self.rect.move(-self.key_state[2], 0)
            self.animation.is_facing_right = False
        if self.key_state[1] and self.rect.collidelist(self.scene.wall_rects['right']) == -1:
            self.rect = self.rect.move(self.key_state[2], 0)
            self.animation.is_facing_right = True

        if not is_colliding_floor:
            self.rect = self.rect.move(0, 2)

        if self.key_state[0] and self.key_state[1]:
            self.switch_state('idle', 25)
        elif self.key_state[0] or self.key_state[1]:
            self.switch_state('walk', 10)
        else:
            self.switch_state('idle', 25)

        super().update()

    def to_save_dict(self):
        return {
            'oid': 'player',
            'x': self.rect.x,
            'y': self.rect.y
        }
