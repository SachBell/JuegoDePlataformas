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
Suelo = Objeto(0, 700, 1500, 200, "muro", "grass")
box = Objeto(600, 200, 50, 50, "muro", "grass")
Personaje_Principal = Personaje(0, 700-384)
Game = True

# Llamar a la pantalla de carga antes de entrar al bucle principal


# Loop principal
while Game:
    
    screen.blit(Imagen_Juego, (0,0))
    Tiempo.ComenzarTiempo()
    EstadoActual.CheckInput(Personaje_Principal)
    keys = pygame.key.get_pressed()
    Personaje_Principal.move(keys, Ancho_Pantalla, Alto_Pantalla)
    Personaje_Principal.AccionPersonaje()
    screen.fill(blanco)
    Objeto.DibujarObjetos(screen)
    screen.blit(Personaje_Principal.image, Personaje_Principal.rect)
    pygame.display.flip()
    reloj.tick(60)

    if Personaje_Principal.rect.y > Alto_Pantalla: EstadoActual.Muerte(Personaje_Principal)        
    
    Si = Tiempo.MostrarTiempo()
    if Si == 20: EstadoActual.Muerte(Personaje_Principal)


 #Crear botón "Salir" centrado en la parte inferior de la ventana secundaria
        #boton_salir_nueva = pygame.Rect((Ancho_Pantalla - 300) // 2, Alto_Pantalla - 150, 300, 100)
        #pygame.draw.rect(ventana_nueva, blanco, boton_salir_nueva)
        #pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_salir_nueva, 5)  # Borde del botón "Salir"

        #fuente_boton_salir = pygame.font.Font(None, 20)
        #texto_boton_salir = fuente_boton_salir.render("Salir", True, (0, 0, 0))
        #ventana_nueva.blit(texto_boton_salir, (boton_salir_nueva.x + (boton_salir_nueva.Ancho_Pantalla - texto_boton_salir.get_Ancho_Pantalla()) // 2,
                                               #boton_salir_nueva.y + (boton_salir_nueva.Alto_Pantalla - texto_boton_salir.get_Alto_Pantalla()) // 2))
