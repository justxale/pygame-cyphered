import pygame


class SoundMixer:
    def __init__(self):
        pygame.mixer.init()  # Инициализация mixer'а

    @staticmethod
    def play_sound(sound_file, volume=0.1):
        sound = pygame.mixer.Sound(sound_file)  # Загрузка звукового файла
        sound.set_volume(volume)  # Установка громкости
        sound.play()  # Проигрывание звука

    @staticmethod
    def play_music(music_file, repeat=True):
        pygame.mixer.music.load(music_file)  # Загрузка музыкального файла
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1 if repeat else 0)  # Проигрывание музыки с повтором (если указано)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()  # Пауза музыки

    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()  # Возобновление проигрывания музыки
