import pygame

from .settings import Settings
from ..data.paths import Path


class SoundMixer:
    def __init__(self):
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

    @staticmethod
    def play_music(filename, repeat=True):
        path = Path.music(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(Settings.music_volume)
        pygame.mixer.music.play(-1 if repeat else 0)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()
