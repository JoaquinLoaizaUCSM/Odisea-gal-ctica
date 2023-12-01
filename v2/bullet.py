import pygame
from config import VELOCIDAD_BALA

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("imagenes\\laser.png")
        self.x = x
        self.y = y
        self.speed = VELOCIDAD_BALA

    def move(self):
        # Direccion
        self.y += -self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
