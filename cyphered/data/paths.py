import os

RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')
DATA_PATH = os.path.join(os.getcwd(), 'gamedata')
SAVES_PATH = os.path.join(DATA_PATH, 'saves')

FONTS_PATH = os.path.join(RESOURCES_PATH, 'fonts')
SPRITES_PATH = os.path.join(RESOURCES_PATH, 'sprites')
MUSIC_PATH = os.path.join(RESOURCES_PATH, 'music')
JSONDATA_PATH = os.path.join(RESOURCES_PATH, 'data')
SOUNDS_PATH = os.path.join(RESOURCES_PATH, 'sounds')


class Path:
    """Class containing methods for file paths generation"""
    # Usage: Paths.music('music1')
    @classmethod
    def music(cls, filename: str, *dirs) -> str:
        """Returns a path of MUSIC MP3 file by its filename."""
        if dirs:
            return os.path.join(MUSIC_PATH, *dirs, f'{filename}.mp3')
        else:
            return os.path.join(MUSIC_PATH, f'{filename}.mp3')


    # Usage: Paths.sprite('sprite1')
    @classmethod
    def sprite(cls, filename: str, *dirs) -> str:
        """Returns a path of SPRITE PNG file by its filename."""
        if dirs:
            return os.path.join(SPRITES_PATH, *dirs, f'{filename}.png')
        else:
            return os.path.join(SPRITES_PATH, f'{filename}.png')

    # Usage: Paths.save('save1')
    @classmethod
    def save(cls, filename: str, *dirs) -> str:
        """Returns a path of SAVE JSON file by its filename."""
        return os.path.join(SAVES_PATH, *dirs, f'{filename}.json')

    # Usage: Paths.settings()
    @classmethod
    def settings(cls) -> str:
        """Returns a path of settings JSON file."""
        return os.path.join(DATA_PATH, 'settings.json')

    # Usage: Paths.settings()
    @classmethod
    def sound(cls, filename: str, *dirs) -> str:
        """Returns a path of sound MP3 file."""
        return os.path.join(SOUNDS_PATH, *dirs, f'{filename}.mp3')

    @classmethod
    def data(cls, filename: str, *dirs, ext: str = 'json') -> str:
        """Returns a path of DATA JSON file by its filename."""
        if dirs:
            return os.path.join(JSONDATA_PATH, *dirs, f'{filename}.{ext}')
        else:
            return os.path.join(JSONDATA_PATH, f'{filename}.{ext}')

