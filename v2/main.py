import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from config import ANCHO_PANTALLA, ALTO_PANTALLA, CANTIDAD_ENEMIGOS
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption('Space Invaders')
        self.icon = pygame.image.load('iconos/icono.png')
        pygame.display.set_icon(self.icon)
        self.background = pygame.image.load('imagenes/10.1 Fondo.jpg')

        self.clock = pygame.time.Clock()
        self.player = Player(368, 500, 5)
        self.enemies = [Enemy(random.randint(0, ANCHO_PANTALLA), random.randint(50, 150)) for _ in range(CANTIDAD_ENEMIGOS)]
        self.bullets = []
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def game_loop(self):
        run = True
        while run:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.dx = -self.player.speed
                    if event.key == pygame.K_RIGHT:
                        self.player.dx = self.player.speed
                    if event.key == pygame.K_UP:
                        self.player.dy = -self.player.speed
                    if event.key == pygame.K_DOWN:
                        self.player.dy = self.player.speed
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.dx = 0
                    if event.key in [pygame.K_UP, pygame.K_DOWN]:
                        self.player.dy = 0
            self.player.move()
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.move()
                enemy.draw(self.screen)
            for bullet in self.bullets:
                bullet.move()
                bullet.draw(self.screen)
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()