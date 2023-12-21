import pygame

from .settings import Settings
from ..data.paths import Path


class SoundMixer:
    def __init__(self):
        pygame.mixer.init()
        self.music_playing = False
        self.music_loaded = False

    @staticmethod
    def play_sound(filename, volume=None):
        path = Path.sound(filename)
        sound = pygame.mixer.Sound(path)
        if volume:
            sound.set_volume(volume)
        else:
            sound.set_volume(Settings.sound_volume)
        sound.play()

    def play_music(self, filename, repeat=True):
        path = Path.music(filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(Settings.music_volume)
        pygame.mixer.music.play(-1 if repeat else 0)
        self.music_playing = True
        self.music_loaded = True

    def pause_music(self):
        pygame.mixer.music.pause()
        self.music_playing = False

    def unpause_music(self):
        pygame.mixer.music.unpause()
        self.music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        self.music_playing = False
        self.music_loaded = False
