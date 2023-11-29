import pygame
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración
import sys


class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def mostrar_texto(self, texto, tamano, posicion):
        fuente = pygame.font.Font(None, tamano)
        texto_surface = fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=posicion)
        self.pantalla.blit(texto_surface, texto_rect)


class MenuPrincipal(Menu):
    def mostrar(self):
        self.mostrar_texto("MENU PRINCIPAL", 50, (WIDTH // 2, 100))
        self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
        self.mostrar_texto("2. Records", 30, (WIDTH // 2, 250))
        self.mostrar_texto("3. Ayuda", 30, (WIDTH // 2, 350))
        self.mostrar_texto("4. Salir", 30, (WIDTH // 2, 400))


class MenuJuego(Menu):
    def mostrar(self):
        self.mostrar_texto("MODO JUEGO", 50, (WIDTH // 2, 100))
        self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
        self.mostrar_texto("2. Salir", 30, (WIDTH // 2, 250))


class MenuRecords(Menu):
    def mostrar(self):
        self.mostrar_texto("RECORDS", 50, (WIDTH // 2, 100))
        self.mostrar_texto("1. Mostrar Records", 30, (WIDTH // 2, 200))
        self.mostrar_texto("2. Salir", 30, (WIDTH // 2, 250))


class MenuAyuda(Menu):
    def mostrar(self):
        self.mostrar_texto("AYUDA", 50, (WIDTH // 2, 100))
        self.mostrar_texto("1. Mostrar Ayuda", 30, (WIDTH // 2, 200))
        self.mostrar_texto("2. Salir", 30, (WIDTH // 2, 250))


class MenuEspera(Menu):
    def mostrar(self):
        # Texto de espera para el juego
        self.mostrar_texto("Cargando...", 30, (WIDTH - 100, HEIGHT - 50))


class Hud(Menu):
    def mostrar(self):
        self.mostrar_texto("Puntuacion: ", 30, (WIDTH // 2, 50))
        self.mostrar_texto("Vidas: ", 30, (WIDTH // 2, 100))
        self.mostrar_texto("Nivel: ", 30, (WIDTH // 2, 150))
