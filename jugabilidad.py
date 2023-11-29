# Actualizador de estados
import pygame
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración
from jugador import Jugador
import sys


class Jugabilidad:

    def __init__(self, pantalla, reloj, todos_los_sprites):
        self.pantalla = pantalla
        self.fondo = pygame.image.load('imagenes/fondo.png')
        self.reloj = reloj
        self.todos_los_sprites = todos_los_sprites
        self.jugador = Jugador()
        self.todos_los_sprites.add(self.jugador)

    def update(self):
        self.todos_los_sprites.update()

    # Manejador de eventos
    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Renderizador
    def render(self):
        self.pantalla.fill((0, 0, 0))
        self.todos_los_sprites.draw(self.pantalla)
        self.pantalla.blit(self.fondo, (0, 0))
        pygame.display.flip()

    def juego_principal(self):
        while True:
            self.eventos()
            self.update()
            self.render()

            # Limitar los cuadros por segundo
            self.reloj.tick(60)
