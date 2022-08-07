import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("../assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("../assets/sounds/game_over.ogg"),
            'fire_ball': pygame.mixer.Sound("../assets/sounds/meteorite.ogg"),
            'bonus': pygame.mixer.Sound("../assets/sounds/bonus.mp3"),
            'power_up': pygame.mixer.Sound("../assets/sounds/power_up.mp3"),
            'power_down': pygame.mixer.Sound("../assets/sounds/power_down.wav"),
            'music': pygame.mixer.Sound("../assets/sounds/music.mp3"),
            'coeur': pygame.mixer.Sound("../assets/sounds/coeur.mp3"),

        }

    def play(self, name,):
        self.sounds[name].play()

    def back_sound(self, name):
        self.sounds[name].play(loops=-1, maxtime=0, fade_ms=0)
