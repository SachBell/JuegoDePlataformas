import pygame
from Configuración import *

imagen_fondo_principal = pygame.image.load("./Data/Texturas/Fondos/FondoMenu1.jpg")
imagen_fondo_principal = pygame.transform.scale(imagen_fondo_principal, (Ancho_Pantalla, Alto_Pantalla))
imagen_fondo_nueva = pygame.image.load("./Data/Texturas/Fondos/FondoMenu2.png")
imagen_fondo_nueva = pygame.transform.scale(imagen_fondo_nueva, (Ancho_Pantalla, Alto_Pantalla))

Ventana_Principal = pygame.display.set_mode((Ancho_Pantalla, Alto_Pantalla))
pygame.display.set_caption("Ventana Principal")

Texturas = {"Grass" : ".Data/Texturas/Tiles/Grass.png"}

# imagenchiquita = pygame.transform.scale(Character, (60, 100))
