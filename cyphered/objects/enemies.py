from .base import GameObject, AnimatedGameObject, AnimationController
from ..services.save import Saver


class Trap(GameObject):
    def __init__(self, *groups):
        super().__init__(*groups)
        Saver.add(self)

    def to_save_dict(self):
        return {
            'oid': 'trap',
            'x': self.rect.x,
            'y': self.rect.y
        }


class Crab(AnimatedGameObject):
    def __init__(self, *groups, x=0, y=0):
        super().__init__(
            self.load_image('walk', 'crab', transparent=True),
            8, 2, *groups, x=x, y=y, mult=2
        )
        self.rect.x = 200
        self.rect.y = 200

        self.move_state = [True, 0]
        Saver.add(self)

    def update(self):
        # print(self.move_state, self.animation.is_facing_right)
        if self.move_state[0]:
            self.rect = self.rect.move(1, 0)
        else:
            self.rect = self.rect.move(-1, 0)
        self.move_state[1] += 1

        if self.move_state[1] >= 500:
            self.move_state[0] = not self.move_state[0]
            self.move_state[1] = 0
            self.animation.is_facing_right = not self.animation.is_facing_right

        super().update()

    def to_save_dict(self):
        return {
            'oid': 'crab',
            'x': self.rect.x,
            'y': self.rect.y
        }
