import os

RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')
DATA_PATH = os.path.join(os.getcwd(), 'gamedata')
SAVES_PATH = os.path.join(DATA_PATH, 'saves')

FONTS_PATH = os.path.join(RESOURCES_PATH, 'fonts')
SPRITES_PATH = IMAGES_PATH = os.path.join(RESOURCES_PATH, 'sprites')
MUSIC_PATH = os.path.join(RESOURCES_PATH, 'music')


class Path:
    """Class containing methods for file paths generation"""
    # Usage: Paths.music('music1')
    @classmethod
    def music(cls, filename: str) -> str:
        """Returns a path of MUSIC MP3 file by its filename."""
        return os.path.join(MUSIC_PATH, f'{filename}.mp3')

    # Usage: Paths.sprite('sprite1')
    @classmethod
    def sprite(cls, filename: str) -> str:
        """Returns a path of SPRITE PNG file by its filename."""
        return os.path.join(SPRITES_PATH, f'{filename}.png')

    # Usage: Paths.image('sprite1')
    @classmethod
    def image(cls, filename: str) -> str:
        """Returns a path of SPRITE PNG file by its filename. Equals to Paths.sprite(filename)"""
        return cls.sprite(filename)

    # Usage: Paths.save('save1')
    @classmethod
    def save(cls, filename: str) -> str:
        """Returns a path of SAVE TXT file by its filename."""
        return os.path.join(SAVES_PATH, f'{filename}.json')

    # Usage: Paths.settings()
    @classmethod
    def settings(cls) -> str:
        """Returns a path of settings TXT file."""
        return os.path.join(DATA_PATH, 'settings.txt')
