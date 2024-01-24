import pygame
import sys
from src.mainGame import Personaje
from src.objets.box import Caja

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JUEGO 1")

white = (255, 255, 255)

personaje = Personaje(200, 200)
caja = Caja(150, 200, 200, 500)   # Define las coordenadas y dimensiones de la caja

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

    while True:
        # Verificar si el personaje ha caído fuera de la pantalla
        if personaje.rect.y > height:
            font = pygame.font.Font(None, 74)
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            restart_text = font.render("Press R to restart", True, (255, 0, 0))
            screen.blit(game_over_text, (width // 2 - 150, height // 2 - 50))
            screen.blit(restart_text, (width // 2 - 250, height // 2 + 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        personaje.rect.x = 0  # Ajusta las coordenadas iniciales según tu diseño
                        personaje.rect.y = 0
                        personaje.jumping = False
                        personaje.jump_count = 10
