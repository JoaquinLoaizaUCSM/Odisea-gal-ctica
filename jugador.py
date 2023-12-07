import pygame
from config import WIDTH, HEIGHT, RUTAS_IMAGENES_ENEMIGO  # Importa los detalles de la configuración
import random


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # carga la imagen del jugador
        self.numero_balas = 1
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

        self.vidas = 10
        self.puntuacion = 0

    # Actualiza la posición del jugador en función de la entrada del teclado
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velocidad
        # New code for vertical movement:
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.velocidad

    def disparar(self):

        proyectil = Proyectil(self.rect.centerx, self.rect.top)
        if len(self.proyectiles) < self.numero_balas:
            self.proyectiles.add(proyectil)
            # sonido de disparo
            pygame.mixer.Sound.play(self.disparo)
        # crea un nuevo proyectil y lo añade al grupo de sprites
        proyectil.update()

    def colision(self, enemigos):
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):
                self.vidas -= 1
                enemigo.kill()

    def colision_proyectil(self, proyectiles, enemigos):
        for proyectil in proyectiles:
            for enemigo in enemigos:
                if proyectil.rect.colliderect(enemigo.rect):
                    self.puntuacion += 1
                    enemigo.kill()
                    proyectil.kill()


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # carga la imagen del proyectil
        self.image = pygame.image.load('imagenes/laser.png')
        # crea un rectángulo a partir de la imagen
        self.rect = self.image.get_rect()
        # Ajusta la posición del proyectil
        self.rect.x = x - (self.rect.width // 2)  # Ajusta la posición horizontal
        self.rect.y = y - self.rect.height + 30  # Ajusta la posición vertical
        self.velocidad = 10

    # Actualiza la posición del proyectil
    def update(self):
        self.rect.y -= self.velocidad
        if self.rect.bottom < 0:
            self.kill()


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocidad_x = random.randint(-3, 3)
        self.velocidad_y = random.randint(1, 2)
        imagen_seleccionada = random.choice(RUTAS_IMAGENES_ENEMIGO)  # Selecciona una imagen al azar de la lista
        self.image = pygame.image.load(imagen_seleccionada)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # self.velocidad = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.velocidad_x

        # If the enemy is completely off the right side of the screen
        if self.rect.left > WIDTH:
            self.rect.right = 0
            self.reset_position()
        # If the enemy is completely off the left side of the screen
        elif self.rect.right < 0:
            self.rect.left = WIDTH
            self.reset_position()

        self.rect.y += self.velocidad_y

        # If the enemy has moved completely below the screen
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.reset_position()
        # If the enemy has moved completely above the screen
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def spawn_enemies(self):
        # Spawn enemies
        for i in range(5):
            enemy = Enemigo()
            self.all_enemies.add(enemy)
