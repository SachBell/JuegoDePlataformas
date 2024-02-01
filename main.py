import pygame
import sys
from Configuración import *
from src.importMethod import *
from PersonajeDefinicion import Personaje
from src.objets.box import Caja
from Menu import *

pygame.init()

screen = pygame.display.set_mode((Resolucion))
pygame.display.set_caption("Stickman Jumping")

personaje = Personaje(200, 200)
caja = Caja(150, 200, 200, 500)   # Define las coordenadas y dimensiones de la caja

# Llamar a la pantalla de carga antes de entrar al bucle principal
pantalla_carga()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_r:
                personaje.rect.x = 0  # Ajusta las coordenadas iniciales según tu diseño
                personaje.rect.y = 0
                personaje.jumping = False
                personaje.jump_count = 10

    keys = pygame.key.get_pressed()
    personaje.move(keys, Ancho_Pantalla, Alto_Pantalla, caja)
    screen.fill(white)
    caja.dibujar(screen)
    screen.blit(personaje.image, personaje.rect)
    pygame.display.flip()
    reloj.tick(30)


    if personaje.rect.y > Alto_Pantalla:
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        restart_text = font.render("Press R to restart", True, (255, 0, 0))
        screen.blit(game_over_text, (Ancho_Pantalla // 2 - 150, Alto_Pantalla // 2 - 50))
        screen.blit(restart_text, (Ancho_Pantalla // 2 - 250, Alto_Pantalla // 2 + 50))

        pygame.display.flip()

                


 #Crear botón "Salir" centrado en la parte inferior de la ventana secundaria
        #boton_salir_nueva = pygame.Rect((Ancho_Pantalla - 300) // 2, Alto_Pantalla - 150, 300, 100)
        #pygame.draw.rect(ventana_nueva, blanco, boton_salir_nueva)
        #pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_salir_nueva, 5)  # Borde del botón "Salir"

        #fuente_boton_salir = pygame.font.Font(None, 20)
        #texto_boton_salir = fuente_boton_salir.render("Salir", True, (0, 0, 0))
        #ventana_nueva.blit(texto_boton_salir, (boton_salir_nueva.x + (boton_salir_nueva.Ancho_Pantalla - texto_boton_salir.get_Ancho_Pantalla()) // 2,
                                               #boton_salir_nueva.y + (boton_salir_nueva.Alto_Pantalla - texto_boton_salir.get_Alto_Pantalla()) // 2))
