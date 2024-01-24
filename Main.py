#La importación pygame ahora será conocida como "pg"
import pygame as pygame
import sys
from Configuración import *
from Importaciones import *

# Definir colores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
imagen = pygame.image.load('Imagen.png')
imagen2 = pygame.image.load('Imagen2.png')

class Game():

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(Resolucion)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill('black')
        imagen_rect = imagenchiquita.get_rect()
        self.screen.blit(imagenchiquita, imagen_rect)

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f"{self.clock.get_fps() :.2f}")

    def check_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.draw()
            self.update()
            self.check_events()

main = Game()
main.run()