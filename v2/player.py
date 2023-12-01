import pygame
from config import JUGADOR_INICIAL_X, JUGADOR_INICIAL_Y, VELOCIDAD_JUGADOR

class Player:
    def __init__(self):
        self.image = pygame.image.load("imagenes\\nave.png")
        self.x = JUGADOR_INICIAL_X
        self.y = JUGADOR_INICIAL_Y
        self.speed = VELOCIDAD_JUGADOR

    def move(self, direction):
        self.x += direction * self.speed
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

