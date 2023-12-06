import pygame

from base_datos import BaseDeDatosJuego
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración


# Creando una clase de Menu Base

class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def mostrar_texto(self, texto, tamano, posicion):
        fuente = pygame.font.Font(None, tamano)
        texto_surface = fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=posicion)
        self.pantalla.blit(texto_surface, texto_rect)


# Mostrar Menú Principal
class MenuPrincipal(Menu):
    def mostrar(self):
        self._texto_menu_principal()
        self._opcion_jugar()
        self._opcion_records()
        self._opcion_ayuda()
        self._opcion_salir()

    def _texto_menu_principal(self):
        self.mostrar_texto("MENU PRINCIPAL", 50, (WIDTH // 2, 100))

    def _opcion_jugar(self):
        self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))

    def _opcion_records(self):
        self.mostrar_texto("2. Records", 30, (WIDTH // 2, 250))

    def _opcion_ayuda(self):
        self.mostrar_texto("3. Ayuda", 30, (WIDTH // 2, 350))

    def _opcion_salir(self):
        self.mostrar_texto("4. Salir", 30, (WIDTH // 2, 400))


# Mostrar records del BD
class MenuRecordsBD(Menu):
    def mostrar(self):
        self._texto_records()
        self._mostrar_puntajes()

    def _texto_records(self):
        self.mostrar_texto("RECORDS", 50, (WIDTH // 2, 100))

    def _mostrar_puntajes(self):
        model = BaseDeDatosJuego()
        puntajes = model.obtener_puntuaciones()
        puntajes = sorted(puntajes, key=lambda x: x[2], reverse=True)
        for i in range(len(puntajes)):
            self.mostrar_texto(f"{puntajes[i][1]}: {puntajes[i][2]}", 30, (WIDTH // 2, 200 + (i * 50)))


class MenuEspera(Menu):
    def mostrar(self):
        self._texto_espera()

    def _texto_espera(self):
        # pantalla de espera en la parte derecha abajo en la ezquina de la pantalla
        self.mostrar_texto("CARGANDO...", 30, (WIDTH - 100, HEIGHT - 50))


class MenuIngresoNombre(Menu):
    def mostrar(self):
        self._texto_ingreso_nombre()

    def _texto_ingreso_nombre(self):
        self.mostrar_texto("INGRESE SU NOMBRE", 50, (WIDTH // 2, 100))


class MenuAyuda(Menu):
    def mostrar(self):
        self._texto_ayuda()

    def _texto_ayuda(self):
        self.mostrar_texto("AYUDA", 50, (WIDTH // 2, 100))


class HUD(Menu):
    def mostrar(self, puntuacion, vidas):
        self.mostrar_texto(f"Puntuación: {puntuacion}", 30, (WIDTH // 2, 50))
        self.mostrar_texto(f"Vidas: {vidas}", 30, (WIDTH // 2, 80))
