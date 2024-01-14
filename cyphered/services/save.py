import json

from ..data import Path


class Savefile:
    def __init__(self, data):
        self.objects = data['objects']
        self.level_name = data['level']
        self.player = self.objects['player']


class Saver:
    listened_objects: list = []

    @classmethod
    def save_all(cls, cur_playscene):
        data = {
            'objects': {},
            'level': cur_playscene.level_name
        }
        for obj in cls.listened_objects:
            data['objects'].update(obj.to_save_dict())
        with open(Path.savefile('save1'), 'w', encoding='utf-8') as file:
            print(data)
            json.dump(data, file)

    @classmethod
    def load_save_file(cls, filename: str = 'save1'):
        try:
            with open(Path.savefile(filename), 'r', encoding='utf-8') as file:
                print(Path.savefile(filename))
                data = json.load(file)
            print(Savefile(data))
            return Savefile(data)
        except OSError:
            print('Savefile not found')
            return None
        except json.decoder.JSONDecodeError:
            print('Something went wrong')
            return None

    @classmethod
    def add(cls, gameobject):
        if not gameobject.is_listened:
            cls.listened_objects.append(gameobject)
            gameobject.is_listened = True
        print(cls.listened_objects)
