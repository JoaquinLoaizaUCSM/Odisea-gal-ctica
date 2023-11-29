import pygame
import sys
import sqlite3
from config import WIDTH, HEIGHT

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.velocidad = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velocidad

class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("datos_jugador.db")
        self.cursor = self.conexion.cursor()
        self.inicializar_tabla()

    def inicializar_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jugador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                puntuacion INTEGER
            )
        ''')
        self.conexion.commit()

    def guardar_puntuacion(self, nombre, puntuacion):
        self.cursor.execute("INSERT INTO jugador (nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))
        self.conexion.commit()

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
        self.menu_principal()

    def menu_principal(self):
        while True:
            self.pantalla.fill((0, 0, 0)) 

            self.mostrar_texto("MENU PRINCIPAL", 50, (WIDTH // 2, 100))
            self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
            self.mostrar_texto("2. Records", 30, (WIDTH // 2, 250))
            self.mostrar_texto("3. Help", 30, (WIDTH // 2, 350))
            self.mostrar_texto("4. Salir", 30, (WIDTH // 2, 400))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.menu_jugar()
                    elif evento.key == pygame.K_2:
                        self.menu_records()
                    elif evento.key == pygame.K_3:
                        self.menu_help()
                    elif evento.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()

    def menu_jugar(self):
        while True:
            self.pantalla.fill((0, 0, 0))

            self.mostrar_texto("MODO JUEGO", 50, (WIDTH // 2, 100))
            self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
            self.mostrar_texto("2. Salir", 30, (WIDTH // 2, 250))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.juego_principal()
                    elif evento.key == pygame.K_2:
                        return

    def menu_records(self):
        pass

    def menu_help(self):
        pass

    def juego_principal(self):
        while True:
            self.eventos()
            self.update()
            self.render()

            self.reloj.tick(60)

    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.todos_los_sprites.update()

    def render(self):
        self.pantalla.fill((0, 0, 0))
        self.todos_los_sprites.draw(self.pantalla)
        pygame.display.flip()

    def mostrar_texto(self, texto, tamano, posicion):
        fuente = pygame.font.Font(None, tamano)
        texto_surface = fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=posicion)
        self.pantalla.blit(texto_surface, texto_rect)

if __name__ == "__main__":
    juego = Juego()
    juego.menu_principal()
