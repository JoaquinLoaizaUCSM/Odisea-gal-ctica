import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from config import ANCHO_PANTALLA, ALTO_PANTALLA, CANTIDAD_ENEMIGOS, FUENTE_TAMANO, TEXTO_X, TEXTO_Y, FUENTE_FINAL_TAMANO
import random

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Titulo e Icono
pygame.display.set_caption("Invasion Extraterrestrial")
icono = pygame.image.load("iconos\\icono.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("imagenes\\10.1 Fondo.jpg")

# Musica
mixer.music.load("16.3 MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador
jugador = Player()

# Enemigos
enemigos = [Enemy(random.randint(0, 736), random.randint(50, 200)) for _ in range(CANTIDAD_ENEMIGOS)]

# Balas
balas = []

# Puntuaje
puntuaje = 0
fuente = pygame.font.Font('freesansbold.ttf', FUENTE_TAMANO)
texto_x, texto_y = TEXTO_X, TEXTO_Y

# Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', FUENTE_FINAL_TAMANO)


# Función para mostrar puntuaje
def mostrar_puntuaje(x, y):
    texto = fuente.render(f"Puntuaje: {puntuaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función para mostrar el fin del juego
def fin_juego():
    mi_fuente_final = fuente_final.render("END", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


# Loop del juego
se_ejecuta = True
clock = pygame.time.Clock()

while se_ejecuta:

    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                jugador.move(-1)
            if evento.key == pygame.K_d:
                jugador.move(1)
            if evento.key == pygame.K_SPACE:
                if not balas:
                    bala = Bullet(jugador.x + 16, jugador.y)
                    balas.append(bala)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador.move(0)

    jugador.draw(pantalla)

    for enemigo in enemigos:
        enemigo.move()
        enemigo.draw(pantalla)

        for bala in balas:
            if bala.y < 0:
                balas.remove(bala)
            elif enemigo.x < bala.x < enemigo.x + 64 and enemigo.y < bala.y < enemigo.y + 64:
                mixer.Sound('16.2 Golpe.mp3').play()
                balas.remove(bala)
                puntuaje += 1
                enemigo.x = random.randint(0, 736)
                enemigo.y = random.randint(50, 200)

    for bala in balas:
        bala.move()
        bala.draw(pantalla)

    mostrar_puntuaje(texto_x, texto_y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
