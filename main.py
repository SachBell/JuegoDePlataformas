import pygame
import sys
from Configuración import *
from Importaciones import *
from PersonajeDefinicion import Personaje
from Objetos import *
from Estados import *
from Menu import *

pygame.init()
pygame.display.set_mode()
pygame.display.set_caption("Stickman Jumping")
EstadoActual = States()
personaje = Personaje(0, 400)
caja2 = Objeto(800, 200, 200, 200, "muro")
Game = True

# Llamar a la pantalla de carga antes de entrar al bucle principal


# Loop principal
while Game:
    
    Tiempo.ComenzarTiempo()
    EstadoActual.CheckInput(personaje)
    keys = pygame.key.get_pressed()
    personaje.move(keys, Ancho_Pantalla, Alto_Pantalla)
    personaje.AccionPersonaje()
    screen.fill(blanco)
    Objeto.DibujarObjetos(screen)
    screen.blit(personaje.image, personaje.rect)
    pygame.display.flip()
    reloj.tick(60)

    if personaje.rect.y > Alto_Pantalla: EstadoActual.Muerte(personaje)        
    
    Si = Tiempo.MostrarTiempo()
    if Si == 20: EstadoActual.Muerte(personaje)

                


 #Crear botón "Salir" centrado en la parte inferior de la ventana secundaria
        #boton_salir_nueva = pygame.Rect((Ancho_Pantalla - 300) // 2, Alto_Pantalla - 150, 300, 100)
        #pygame.draw.rect(ventana_nueva, blanco, boton_salir_nueva)
        #pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_salir_nueva, 5)  # Borde del botón "Salir"

        #fuente_boton_salir = pygame.font.Font(None, 20)
        #texto_boton_salir = fuente_boton_salir.render("Salir", True, (0, 0, 0))
        #ventana_nueva.blit(texto_boton_salir, (boton_salir_nueva.x + (boton_salir_nueva.Ancho_Pantalla - texto_boton_salir.get_Ancho_Pantalla()) // 2,
                                               #boton_salir_nueva.y + (boton_salir_nueva.Alto_Pantalla - texto_boton_salir.get_Alto_Pantalla()) // 2))
