# Imports necesarios
import pygame
import sys
from pygame import mixer

import timeit
from config import WIDTH, HEIGHT
from jugador import Jugador
from menu import HUD, MenuEspera, MenuRecordsBD, MenuIngresoNombre
from base_datos import BaseDeDatosJuego


class Jugabilidad:
    def __init__(self):
        self.init_juego()  # Inicializar componentes del juego

    def init_juego(self):
        """Inicializa los componentes necesarios del juego"""
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hud = HUD(self.pantalla)
        self.jugador = Jugador()
        self.fondo = pygame.image.load('imagenes/fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (WIDTH, HEIGHT))
        self.reloj = pygame.time.Clock()
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.jugador)
        self.menu_espera = MenuEspera(self.pantalla)

    def procesar_eventos_teclado(self, evento):
        """Procesa los eventos del teclado"""
        if evento.key == pygame.K_a:
            self.jugador.disparar()
        if evento.key == pygame.K_ESCAPE:
            self.guardar_puntuacion()
            self.terminar_juego()

    def guardar_puntuacion(self):
        try:
            """Muestra el menú, permite el ingreso de nombre y guarda la puntuación"""
            MenuRecordsBD(self.pantalla).mostrar()
            pygame.display.flip()
            pygame.time.wait(6000)

            MenuIngresoNombre(self.pantalla).mostrar()
            pygame.display.flip()
            nombre = input("Ingrese su nombre: ")
            BaseDeDatosJuego().guardar_puntuacion(nombre, self.jugador.puntuacion, timeit.default_timer())
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

    def terminar_juego(self):
        """Cierra la ventana del juego y termina el programa"""
        pygame.quit()
        sys.exit()

    def update(self):
        """Actualiza los sprites del juego"""
        self.todos_los_sprites.update()

    def eventos(self):
        """Manejador de eventos"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.terminar_juego()
            if evento.type == pygame.KEYDOWN:
                self.procesar_eventos_teclado(evento)

            if evento.type == pygame.KEYDOWN:
                # disparo con la barra espaciadora
                if evento.key == pygame.K_SPACE:
                    self.jugador.disparar()

    def render(self):
        """Renderizador"""
        self.pantalla.blit(self.fondo, (0, 0))
        self.todos_los_sprites.draw(self.pantalla)
        self.hud.mostrar(self.jugador.puntuacion, self.jugador.vidas)
        pygame.display.flip()

    def juego_principal(self):
        """Bucle principal del juego"""
        while True:
            self.update()
            self.render()
            self.reloj.tick(60)
            self.eventos()
