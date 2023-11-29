import pygame
import sys
from base_datos import BaseDatos
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración
from jugador import Jugador
from menu import MenuPrincipal, MenuJuego, MenuRecords, MenuAyuda


class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego de Naves")

        self.jugador = Jugador()
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.jugador)

        self.reloj = pygame.time.Clock()

        self.base_datos = BaseDatos()
        self.menu_principal = MenuPrincipal(self.pantalla)
        self.menu_juego = MenuJuego(self.pantalla)
        self.menu_records = MenuRecords(self.pantalla)
        self.menu_ayuda = MenuAyuda(self.pantalla)

    def actualizar_pantalla(self, menu):
        while True:
            self.pantalla.fill((0, 0, 0))
            menu.mostrar()
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.mostrar_menu_jugar()
                    elif evento.key == pygame.K_2:
                        self.mostrar_menu_records()
                    elif evento.key == pygame.K_3:
                        self.mostrar_menu_ayuda()
                    elif evento.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()

    def mostrar_menu_principal(self):
        self.actualizar_pantalla(self.menu_principal)

    def mostrar_menu_jugar(self):
        self.actualizar_pantalla(self.menu_juego)

    def mostrar_menu_records(self):
        self.actualizar_pantalla(self.menu_records)

    def mostrar_menu_ayuda(self):
        self.actualizar_pantalla(self.menu_ayuda)