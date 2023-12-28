import json

from ..data import Path
# from ..objects.base import GameObject


class Savefile:
    def __init__(self, data):
        self.objects = data['objects']


class Saver:
    #listened_objects: list[GameObject] = []
    listened_objects: list = []

    @classmethod
    def save_all(cls):
        data = {
            'objects': []
        }
        for obj in cls.listened_objects:
            data['objects'].append(obj.to_save_dict())
        with open(Path.save('save1'), 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def load_save_file(cls, filename: str = 'save1'):
        try:
            with open(Path.save(filename), 'w', encoding='utf-8') as file:
                data = json.load(file)
            return Savefile(data)
        except OSError:
            pass

    @classmethod
    #def add(cls, gameobject: GameObject):
    def add(cls, gameobject):
        cls.listened_objects.append(gameobject)
        gameobject.is_listened = True
