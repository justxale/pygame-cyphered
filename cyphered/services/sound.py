import pygame

from .settings import Settings
from ..data import constants
from ..data.paths import Path


class SoundMixer:
    music_playing = False
    music_loaded = False

    def __new__(cls, *args, **kwargs):
        pygame.mixer.init()

    @staticmethod
    def play_sound(filename, volume=None):
        path = Path.sound(filename)
        sound = pygame.mixer.Sound(path)
        if volume:
            sound.set_volume(volume)
        else:
            sound.set_volume(Settings.sound_volume)
        sound.play()

    @classmethod
    def play_music(cls, filename, volume: float = 1, repeat=True):
        path = Path.music(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(Settings.music_volume * volume)
        pygame.mixer.music.play(-1 if repeat else 0, )
        cls.music_playing = True
        cls.music_loaded = True

    @classmethod
    def pause_music(cls):
        pygame.mixer.music.pause()
        cls.music_playing = False

    @classmethod
    def unpause_music(cls):
        pygame.mixer.music.unpause()
        cls.music_playing = True

    @classmethod
    def stop_music(cls):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        cls.music_playing = False
        cls.music_loaded = False

    @classmethod
    def switch_music(cls, filename: str, volume: float = 1, fade=True, repeat=True):
        if cls.music_loaded and fade:
            pygame.mixer.music.fadeout(constants.MUSIC_FADE_TIME)
            pygame.mixer.music.unload()
        path = Path.music(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(Settings.music_volume * volume)
        pygame.mixer.music.play(-1 if repeat else 0, fade_ms=constants.MUSIC_FADE_TIME if fade else 0)
        cls.music_playing = True
        cls.music_loaded = True
