import pygame
import random

from src.sounds import SoundManager


class Extracts(pygame.sprite.Sprite):

    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(f"../assets/{name}.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.position = [x, y]
        # self.value = random.randint(1, 5)
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.sound = SoundManager()

    def load_position(self):

        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def erase(self):
        self.rect.x = - 50
        self.rect.y = - 10


class Bonus(Extracts):

    def __init__(self, name, x, y):
        super().__init__(name, 0, 0)
        self.name = name
        self.value = 2
        self.position = [x, y]


class FireBall(Extracts):

    def __init__(self, name, x, y):
        super().__init__(name, 0, 0)
        self.name = name
        self.position = [x, y]
        self.value = random.randint(1, 8)
        self.speed = random.randint(1, 3)

    def move(self):

        if self.rect.x > 47:
            self.rect.x -= self.speed
        else:
            self.load_position()
            self.sound.play('fire_ball')


class Heart(Extracts):

    def __init__(self, name, x, y):
        super().__init__(name, 0, 0)
        self.name = name
        self.position = [x, y]
        self.image = pygame.transform.scale(self.image, (10, 10))
