import pygame
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()      # Se inicializa la clase padre para que se pueda usar la clase Sprite
        jugador_imagen_temp = pygame.image.load('imagenes/A1.png').convert_alpha()  # Carga la imagen de jugador
        self.image = pygame.transform.scale(jugador_imagen_temp, (50, 50))  # Escala la imagen
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH // 2) - (self.rect.width // 2)  # Ajusta la posición horizontal
        self.rect.y = (HEIGHT - self.rect.height)  # Ajusta la posición vertical
        self.velocidad = 5

    # Actualiza la posición del jugador en función de la entrada del teclado
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velocidad


class enemigos:
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
