import pygame
from Configuración import *
import os

Directorio_Principal = os.path.dirname(os.path.abspath(__file__))

Ventana_Principal = pygame.display.set_mode((Ancho_Pantalla, Alto_Pantalla))

imagen_fondo_principal = pygame.image.load("./PROYECTOS/Juegodeplataformas/Data/Texturas/Fondos/FondoMenu1.jpg")
imagen_fondo_principal = pygame.transform.scale(imagen_fondo_principal, (Ancho_Pantalla, Alto_Pantalla))
imagen_fondo_nueva = pygame.image.load("./PROYECTOS/Juegodeplataformas/Data/Texturas/Fondos/FondoMenu2.png")
imagen_fondo_nueva = pygame.transform.scale(imagen_fondo_nueva, (Ancho_Pantalla, Alto_Pantalla))
Imagen_Juego_No_Escalada = pygame.image.load(os.path.join(Directorio_Principal, os.path.join('Data', 'Texturas', 'Fondos', 'FondoJuego.jpg')))
Imagen_Juego = pygame.transform.scale(Imagen_Juego_No_Escalada, (Ancho_Pantalla, Alto_Pantalla))

pygame.display.set_caption("Ventana Principal")



Texturas = {"grass" : os.path.join('Data', 'Texturas', 'Tiles', 'Grass.png'),
            }

# imagenchiquita = pygame.transform.scale(Character, (60, 100))
