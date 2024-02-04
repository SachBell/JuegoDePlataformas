import pygame
import sys
from src.mainGame import Personaje
from src.objets.box import Caja

pygame.init()

width, height = 800, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JUEGO 1")

white = (255, 255, 255)

personaje = Personaje(100, 10)  # Ajusta las coordenadas iniciales según tu diseño
caja = Caja(100, 500, 500, 200)   # Define las coordenadas y dimensiones de la caja

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    personaje.move(keys, width, height, caja)

    screen.fill(white)

    caja.dibujar(screen)
    screen.blit(personaje.image, personaje.rect)

    pygame.display.flip()

    clock.tick(30)