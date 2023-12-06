import pygame
import sys

from pygame import mixer

from base_datos import BaseDeDatosJuego
from config import WIDTH, HEIGHT
from jugador import Jugador
from menu import MenuPrincipal, MenuRecordsBD, MenuEspera, MenuAyuda
from jugabilidad import Jugabilidad


class Control:
    def __init__(self):
        self.todos_los_sprites = None
        self.jugador = None
        self.fondo = None
        self.menu_opciones = None
        self.pantalla = None
        self.mixer = None
        self.Jugabilidad = None
        pygame.init()

        self.iniciar_pantalla()
        self.cargar_recursos()
        self.iniciar_sprites()
        self.iniciar_bases_datos_menus()
        self.iniciar_reloj_sonido()

    def iniciar_pantalla(self):
        """
        Esta función inicializa la pantalla y el menú de opciones del juego.
        """
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego de Naves")
        self.menu_opciones = {
            pygame.K_2: self.mostrar_menu_records,
            pygame.K_3: self.mostrar_menu_ayuda,
            pygame.K_4: self.terminar_juego,
        }

    def cargar_recursos(self):
        """
        Esta función carga los recursos visuales necesarios para el juego.
        """
        self.fondo = pygame.image.load('imagenes/fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (WIDTH, HEIGHT))

    def iniciar_sprites(self):
        """
        Esta función inicializa los sprites del juego.
        """
        self.jugador = Jugador()
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.jugador)

    def iniciar_bases_datos_menus(self):
        """
        Esta función inicializa las bases de datos y los menús del juego.
        """
        self.base_datos = BaseDeDatosJuego()
        self.menu_principal = MenuPrincipal(self.pantalla)
        self.menu_records = MenuRecordsBD(self.pantalla)
        self.menu_ayuda = MenuAyuda(self.pantalla)
        self.menu_espera = MenuEspera(self.pantalla)

    def iniciar_reloj_sonido(self):
        """
        Esta función inicializa el reloj y el sonido del juego.
        """
        self.reloj = pygame.time.Clock()
        mixer.music.load('musica/MusicaFondo.mp3', 'musica/MusicaJugabilidad.mp3')
        mixer.music.set_volume(0.3)
        self.cargar_sonido_inicio()

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.terminar_juego()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    self.iniciar_juego()
                else:
                    accion = self.menu_opciones.get(evento.key)
                    if accion:
                        accion()

    def actualizar_pantalla(self, menu):
        while True:
            self.pantalla.blit(self.fondo, (0, 0))
            menu.mostrar()
            pygame.display.flip()
            self.manejar_eventos()

    def terminar_juego(self):
        pygame.quit()
        sys.exit()

    def mostrar_menu_principal(self):
        self.actualizar_pantalla(self.menu_principal)

    def mostrar_menu_records(self):
        self.actualizar_pantalla(self.menu_records)

    def mostrar_menu_ayuda(self):
        self.actualizar_pantalla(self.menu_ayuda)

    def cargar_sonido_inicio(self):
        pygame.mixer.music.load('musica/MusicaFondo.mp3')
        pygame.mixer.music.play(-1)

    def iniciar_juego(self):
        self.Jugabilidad = Jugabilidad()
        self.pantalla.blit(self.fondo, (0, 0))
        pygame.mixer.music.stop()   # Detiene la música de fondo
        self.mostrar_menu_y_esperar(MenuEspera, 4000)
        self.cargar_sonido_juego()
        self.Jugabilidad.juego_principal()

    def cargar_sonido_juego(self):
        pygame.mixer.music.load('musica/MusicaJugabilidad.mp3')
        pygame.mixer.music.play(-1)

    def mostrar_menu_y_esperar(self, Menu, tiempo_espera):
        menu = Menu(self.pantalla)
        menu.mostrar()
        pygame.display.flip()
        pygame.time.wait(tiempo_espera)