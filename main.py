import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurar la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego Pygame")

# Definir jugador
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10

# Inicializar el reloj
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Dibujar en la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [player_x, player_y, player_width, player_height])

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer límite de cuadros por segundo (FPS)
    clock.tick(60)