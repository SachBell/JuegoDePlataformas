import pygame
import sys

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JUEGO 1")

white = (255, 255, 255)


muñeco_color = (0, 128, 255)
muñeco_speed = 20
jumping = False
jump_count = 10

imagen = pygame.image.load('./PROYECTOS/Juegodeplataformas/src/img/Imagen.png')
imagen_rect = imagen.get_rect()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT]:
        imagen_rect[0] -= muñeco_speed
    if keys[pygame.K_RIGHT]:
        imagen_rect[0] += muñeco_speed

    
    if not jumping:
        if keys[pygame.K_UP]:
            imagen_rect[1] -= muñeco_speed
        if keys[pygame.K_DOWN]:
            imagen_rect[1] += muñeco_speed
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            imagen_rect[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10


    screen.fill(white)

    screen.blit(imagen, imagen_rect)

    pygame.display.flip()

    clock.tick(30)