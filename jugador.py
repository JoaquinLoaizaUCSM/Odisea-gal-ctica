import pygame
from config import WIDTH, HEIGHT  # Importa los detalles de la configuración


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # carga la imagen del jugador
        self.disparo = pygame.mixer.Sound('musica/disparo.mp3')
        self.proyectiles = []
        self.image = pygame.image.load('imagenes/A1.png')
        ckey = self.image.get_at((0, 0))
        self.image.set_colorkey(ckey)
        pygame.display.set_icon(self.image)

        # crea un rectángulo a partir de la imagen
        self.rect = self.image.get_rect()

        # Ajusta la posición del jugador
        self.rect.x = (WIDTH // 2) - (self.rect.width // 2)  # Ajusta la posición horizontal
        self.rect.y = (HEIGHT - self.rect.height)  # Ajusta la posición vertical
        self.velocidad = 5

        self.vidas = 3
        self.puntuacion = 0
        self.nivel = 1

    # Actualiza la posición del jugador en función de la entrada del teclado
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velocidad

    def disparar(self):

        # sonido de disparo
        pygame.mixer.Sound.play(self.disparo)
        pygame.mixer.music.stop()
        # crea un nuevo proyectil y lo añade al grupo de sprites
        proyectil = Proyectil(self.rect.centerx, self.rect.top)
        if len(self.proyectiles) < 3:
            self.proyectiles.add(proyectil)

    def colision(self, enemigos):
        return pygame.sprite.spritecollide(self, enemigos, True)

    def colision_proyectil(self, proyectiles, enemigos):
        return pygame.sprite.groupcollide(proyectiles, enemigos, True, True)



class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # carga la imagen del proyectil
        self.image = pygame.image.load('imagenes/laser.png')
        # crea un rectángulo a partir de la imagen
        self.rect = self.image.get_rect()
        # Ajusta la posición del proyectil
        self.rect.x = x - (self.rect.width // 2)  # Ajusta la posición horizontal
        self.rect.y = y - self.rect.height  # Ajusta la posición vertical
        self.velocidad = 10

    # Actualiza la posición del proyectil
    def update(self):
        self.rect.y -= self.velocidad
        if self.rect.bottom < 0:
            self.kill()



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
