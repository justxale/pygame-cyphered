from ._base import GameObject


class Trap(GameObject):
    ...

    def to_save_dict(self):
        return {
            'oid': 'player',
            'x': self.x,
            'y': self.y
        }