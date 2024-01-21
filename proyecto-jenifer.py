import pygame
import sys

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JUEGO 1")

white = (255, 255, 255)


muñeco_color = (0, 128, 255)
muñeco_pos = [width // 2, height // 2]  
muñeco_speed = 5
jumping = False
jump_count = 10


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT]:
        muñeco_pos[0] -= muñeco_speed
    if keys[pygame.K_RIGHT]:
        muñeco_pos[0] += muñeco_speed

    
    if not jumping:
        if keys[pygame.K_UP]:
            muñeco_pos[1] -= muñeco_speed
        if keys[pygame.K_DOWN]:
            muñeco_pos[1] += muñeco_speed
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            muñeco_pos[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10


    screen.fill(white)

    
    pygame.draw.circle(screen, muñeco_color, muñeco_pos, 20)  # Cabeza
    pygame.draw.line(screen, muñeco_color, muñeco_pos, (muñeco_pos[0], muñeco_pos[1] + 50), 5)  # Cuerpo
    pygame.draw.line(screen, muñeco_color, (muñeco_pos[0], muñeco_pos[1] + 50), (muñeco_pos[0] - 20, muñeco_pos[1] + 100), 5)  # Pierna izquierda
    pygame.draw.line(screen, muñeco_color, (muñeco_pos[0], muñeco_pos[1] + 50), (muñeco_pos[0] + 20, muñeco_pos[1] + 100), 5)  # Pierna derecha
    pygame.draw.line(screen, muñeco_color, (muñeco_pos[0], muñeco_pos[1] + 20), (muñeco_pos[0] - 20, muñeco_pos[1] + 35), 5)  # Brazo izquierdo
    pygame.draw.line(screen, muñeco_color, (muñeco_pos[0], muñeco_pos[1] + 20), (muñeco_pos[0] + 20, muñeco_pos[1] + 35), 5)  # Brazo derecho

    
    pygame.display.flip()

    clock.tick(30)