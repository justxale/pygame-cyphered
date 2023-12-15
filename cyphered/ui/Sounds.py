import pygame


class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()  # Инициализация mixer'а

    def play_sound(self, sound_file, volume=0.1):
        sound = pygame.mixer.Sound(sound_file)  # Загрузка звукового файла
        sound.set_volume(volume)  # Установка громкости
        sound.play()  # Проигрывание звука

    def play_music(self, music_file, repeat=True):
        pygame.mixer.music.load(music_file)  # Загрузка музыкального файла
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1 if repeat else 0)  # Проигрывание музыки с повтором (если указано)

    def pause_music(self):
        pygame.mixer.music.pause()  # Пауза музыки

    def unpause_music(self):
        pygame.mixer.music.unpause()  # Возобновление проигрывания музыки