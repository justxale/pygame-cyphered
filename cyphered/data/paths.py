import os

RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')
DATA_PATH = os.path.join(os.getcwd(), 'gamedata')
SAVES_PATH = os.path.join(DATA_PATH, 'saves')

FONTS_PATH = os.path.join(RESOURCES_PATH, 'fonts')
SPRITES_PATH = IMAGES_PATH = os.path.join(RESOURCES_PATH, 'sprites')
MUSIC_PATH = os.path.join(RESOURCES_PATH, 'music')


class Path:
    @classmethod
    def music(cls, filename: str) -> str:
        return os.path.join(MUSIC_PATH, f'{filename}.mp3')

    @classmethod
    def sprite(cls, filename: str) -> str:
        return os.path.join(SPRITES_PATH, f'{filename}.png')

    @classmethod
    def image(cls, filename: str) -> str:
        return cls.sprite(filename)

    @classmethod
    def save(cls, filename: str) -> str:
        return os.path.join(SAVES_PATH, f'{filename}.json')

    @classmethod
    def settings(cls) -> str:
        return os.path.join(DATA_PATH, 'settings.txt')
