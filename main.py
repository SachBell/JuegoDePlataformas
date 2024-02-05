import pygame
import sys
from Configuración import *
from Importaciones import *
from PersonajeDefinicion import Personaje
from Objetos import *
from Estados import *
from Menu import *
from Niveles import *

pygame.init()
pygame.display.set_mode()
pygame.display.set_caption("Stickman Jumping")
EstadoActual = States()
nivel = Niveles()
nivel.Lvl_1()

Personaje_Principal = Personaje(1, 500)
Game = True

# Llamar a la pantalla de carga antes de entrar al bucle principal
# Loop principal
while Game:
    
    screen.blit(Imagen_Juego, (0,0))
    Tiempo.ComenzarTiempo()
    EstadoActual.CheckInput(Personaje_Principal)
    Objeto.DibujarObjetos(screen)
    Personaje_Principal.AccionPersonaje()
    pygame.display.flip()
    reloj.tick(60)

    if Personaje_Principal.rect.y > Alto_Pantalla: EstadoActual.Muerte(Personaje_Principal)        
    
    Si = Tiempo.MostrarTiempo()
    if Si == 30: EstadoActual.Muerte(Personaje_Principal)


 #Crear botón "Salir" centrado en la parte inferior de la ventana secundaria
        #boton_salir_nueva = pygame.Rect((Ancho_Pantalla - 300) // 2, Alto_Pantalla - 150, 300, 100)
        #pygame.draw.rect(ventana_nueva, blanco, boton_salir_nueva)
        #pygame.draw.rect(ventana_nueva, (0, 0, 0), boton_salir_nueva, 5)  # Borde del botón "Salir"

        #fuente_boton_salir = pygame.font.Font(None, 20)
        #texto_boton_salir = fuente_boton_salir.render("Salir", True, (0, 0, 0))
        #ventana_nueva.blit(texto_boton_salir, (boton_salir_nueva.x + (boton_salir_nueva.Ancho_Pantalla - texto_boton_salir.get_Ancho_Pantalla()) // 2,
                                               #boton_salir_nueva.y + (boton_salir_nueva.Alto_Pantalla - texto_boton_salir.get_Alto_Pantalla()) // 2))
