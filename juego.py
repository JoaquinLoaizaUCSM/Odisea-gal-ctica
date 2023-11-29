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
        self.menu_opciones = {
            pygame.K_1: self.mostrar_menu_jugar,
            pygame.K_2: self.mostrar_menu_records,
            pygame.K_3: self.mostrar_menu_ayuda,
            pygame.K_4: self.terminar_juego,
        }
        self.fondo = pygame.image.load('imagenes/fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (WIDTH, HEIGHT))
        self.jugador = Jugador()
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.jugador)

        self.reloj = pygame.time.Clock()

        self.base_datos = BaseDatos()
        self.menu_principal = MenuPrincipal(self.pantalla)
        self.menu_juego = MenuJuego(self.pantalla)
        self.menu_records = MenuRecords(self.pantalla)
        self.menu_ayuda = MenuAyuda(self.pantalla)

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.terminar_juego()
            # La tecla W es para iniciar el juego(Temporal)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_w:
                self.juego_principal()
            elif evento.type == pygame.KEYDOWN:
                accion = self.menu_opciones.get(evento.key)
                if accion:
                    accion()

    def actualizar_pantalla(self, menu):
        while True:
            self.pantalla.fill((0, 0, 0))
            self.pantalla.blit(self.fondo, (0, 0))
            menu.mostrar()
            pygame.display.flip()
            self.manejar_eventos()

    def terminar_juego(self):
        pygame.quit()
        sys.exit()

    # Manejador de eventos
    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Actualizador de estados
    def update(self):
        self.todos_los_sprites.update()

    # Renderizador
    def render(self):
        self.pantalla.fill((0, 0, 0))
        self.todos_los_sprites.draw(self.pantalla)
        pygame.display.flip()

    def juego_principal(self):
        while True:
            self.eventos()
            self.update()
            self.render()

            # Limitar los cuadros por segundo
            self.reloj.tick(60)

    def mostrar_menu_principal(self):
        self.actualizar_pantalla(self.menu_principal)

    def mostrar_menu_jugar(self):
        self.actualizar_pantalla(self.menu_juego)

    def mostrar_menu_records(self):
        self.actualizar_pantalla(self.menu_records)

    def mostrar_menu_ayuda(self):
        self.actualizar_pantalla(self.menu_ayuda)
