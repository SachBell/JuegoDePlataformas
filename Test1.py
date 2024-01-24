import pygame
import sys

pygame.init()
reloj = pygame.time.Clock()

# Configurar la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Imagen en Movimiento")

# Cargar las imágenes
imagen = pygame.image.load('./PROYECTOS/Juegodeplataformas/src/img/Imagen.png')
imagen2 = pygame.image.load('./PROYECTOS/Juegodeplataformas/src/img/Imagen2.png')

# Obtener los rectángulos asociados a las imágenes
imagen_rect = imagen.get_rect()
imagen2_rect = imagen2.get_rect()

# Configurar la velocidad de movimiento
velocidad = 2

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover la imagen en función de las teclas presionadas
    if keys[pygame.K_LEFT]:
        imagen_rect.x -= velocidad
    if keys[pygame.K_RIGHT]:
        imagen_rect.x += velocidad
    if keys[pygame.K_UP]:
        imagen_rect.y -= velocidad
    if keys[pygame.K_DOWN]:
        imagen_rect.y += velocidad

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar la primera imagen
    screen.blit(imagen, imagen_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar 1 segundo
    pygame.time.delay(200)

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar la segunda imagen
    screen.blit(imagen2, imagen2_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar 1 segundo
    pygame.time.delay(200)

    # Puedes añadir más lógica o eventos aquí si es necesario

    reloj.tick(60)  # Limitar la velocidad del bucle principal a 60 FPS
