# Importando las bibliotecas necesarias
import pygame
import sys
from base_datos import BaseDatos
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.velocidad = 5

    # Actualiza la posición del jugador en función de la entrada del teclado
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velocidad


# Esta es la clase principal del juego.
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

    # Muestra el menú principal
    def menu_principal(self):
        while True:
            self.pantalla.fill((0, 0, 0))

            self.mostrar_texto("MENU PRINCIPAL", 50, (WIDTH // 2, 100))
            self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
            self.mostrar_texto("2. Records", 30, (WIDTH // 2, 250))
            self.mostrar_texto("3. Ayuda", 30, (WIDTH // 2, 350))
            self.mostrar_texto("4. Salir", 30, (WIDTH // 2, 400))

            pygame.display.flip()

            # Maneja los eventos del menú
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
                        self.menu_ayuda()
                    elif evento.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()

    # Muestra el menú del juego
    def menu_jugar(self):
        while True:
            self.pantalla.fill((0, 0, 0))

            self.mostrar_texto("MODO JUEGO", 50, (WIDTH // 2, 100))
            self.mostrar_texto("1. Jugar", 30, (WIDTH // 2, 200))
            self.mostrar_texto("2. Salir", 30, (WIDTH // 2, 250))

            pygame.display.flip()

            # Maneja los eventos del menú del juego
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.juego_principal()
                    elif evento.key == pygame.K_2:
                        return

    # Función para el menú de registros
    def menu_records(self):
        pass

    # Función para el menú de ayuda
    def menu_ayuda(self):
        pass

    # Función principal del juego
    def juego_principal(self):
        while True:
            self.eventos()
            self.update()
            self.render()

            # Limitar los cuadros por segundo
            self.reloj.tick(60)

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

    # Ayudante para mostrar texto
    def mostrar_texto(self, texto, tamano, posicion):
        fuente = pygame.font.Font(None, tamano)
        texto_surface = fuente.render(texto, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=posicion)
        self.pantalla.blit(texto_surface, texto_rect)


if __name__ == "__main__":
    juego = Juego()
    juego.menu_principal()
