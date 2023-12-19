import os.path
import json
from ..data import Path
from ..data.constants import DEFAULT_SETTINGS


class Settings:
    sound_volume: float = None
    music_volume: float = None
    jump_key: str = None
    move_keys: str = None

    @classmethod
    def load_settings(cls):
        path = Path.settings()
        if not os.path.isfile(path):
            cls.create_default()
        with open(path, 'r', encoding='utf-8') as f:
            data: dict = json.load(f)
        for k, v in data.items():
            setattr(cls, k, v)

    @classmethod
    def save_settings(cls):
        path = Path.settings()
        to_save = {
            "music_volume": cls.music_volume,
            "sound_volume": cls.sound_volume,
            "jump_key": cls.jump_key,
            "move_keys": cls.move_keys
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(to_save, f)

    @classmethod
    def create_default(cls):
        path = Path.settings()
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_SETTINGS, f)

    @classmethod
    def __setitem__(cls, key, value):
        setattr(cls, key, value)

    @classmethod
    def __getitem__(cls, key, value):
        return getattr(cls, key, value)
