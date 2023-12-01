import pygame
import random
from config import VELOCIDAD_ENEMIGOS

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("imagenes\\naveEnemigo.png")
        self.x = x
        self.y = y
        self.speed = VELOCIDAD_ENEMIGOS

    def move(self):
        self.x += self.speed
        if self.x <= 0 or self.x >= 736:
            self.speed *= -1
            self.y += 50

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

