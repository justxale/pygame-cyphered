from ..data import Path
from ..objects import GameObject


class Saver:
    listened_objects: list = []

    @classmethod
    def save_all(cls):
        Path.save('save1')
        return True

    @classmethod
    def load_save_file(cls):
        ...

    @classmethod
    def add(cls, gameobject: GameObject):
        cls.listened_objects.append(gameobject)
        gameobject.is_listened = True
