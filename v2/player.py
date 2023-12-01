import pygame
from config import JUGADOR_INICIAL_X, JUGADOR_INICIAL_Y, VELOCIDAD_JUGADOR, ANCHO_PANTALLA, ALTO_PANTALLA


class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.image = pygame.image.load('imagenes/A1.png')  # adaptalo a tu necesidad

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Asegurando que el jugador no salga de la pantalla (si es necesario)
        if self.x < 0:
            self.x = 0
        if self.x > ANCHO_PANTALLA - 50:  # 50 es el ancho del jugador, adaptalo a tu necesidad
            self.x = ANCHO_PANTALLA - 50
        if self.y < 0:
            self.y = 0
        if self.y > ALTO_PANTALLA - 50:  # 50 es el alto del jugador, adaptalo a tu necesidad
            self.y = ALTO_PANTALLA - 50

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))