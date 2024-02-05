import pygame
from Configuración import *
import os

Directorio_Principal = os.path.dirname(os.path.abspath(__file__))

Ventana_Principal = pygame.display.set_mode((Ancho_Pantalla, Alto_Pantalla))

imagen_fondo_principal = pygame.image.load("./Data/Texturas/Fondos/FondoMenu1.jpg")
imagen_fondo_principal = pygame.transform.scale(imagen_fondo_principal, (Ancho_Pantalla, Alto_Pantalla))
imagen_fondo_nueva = pygame.image.load("./Data/Texturas/Fondos/FondoMenu2.png")
imagen_fondo_nueva = pygame.transform.scale(imagen_fondo_nueva, (Ancho_Pantalla, Alto_Pantalla))
Imagen_Juego_No_Escalada = pygame.image.load(os.path.join(Directorio_Principal, os.path.join('Data', 'Texturas', 'Fondos', 'FondoJuego.jpg')))
Imagen_Juego = pygame.transform.scale(Imagen_Juego_No_Escalada, (Ancho_Pantalla, Alto_Pantalla))

pygame.display.set_caption("Ventana Principal")

Texturas = {"grass" : os.path.join('Data', 'Texturas', 'Tiles', 'Grass.png'),
            "piedra": os.path.join('Data', 'Texturas', 'Tiles', 'piedra.png'),
            "cactus": os.path.join('Data', 'Sprites', 'Objetos', 'cactus.png'),
            "arbol1": os.path.join('Data', 'Sprites', 'Objetos', 'arbol1.png'),
            "arbol2": os.path.join('Data', 'Sprites', 'Objetos', 'arbol2.png'),
            "estrella": os.path.join('Data', 'Sprites', 'Objetos', 'estrella.png'),
            "trofeo": os.path.join('Data', 'Sprites', 'Objetos', 'trofeo.png'),
            "moneda": os.path.join('Data', 'Sprites', 'Objetos', 'moneda.png'),
            "bomba": os.path.join('Data', 'Sprites', 'Objetos', 'bomba.png'),
            "vida": os.path.join('Data', 'Sprites', 'Objetos', 'vida.png'),
            "fuego": os.path.join('Data', 'Sprites', 'Objetos', 'fuego.png'),
            "arbusto": os.path.join('Data', 'Sprites', 'Objetos', 'arbusto.png'),
            "diamante": os.path.join('Data', 'Sprites', 'Objetos', 'diamante.png'),
            "barril": os.path.join('Data', 'Sprites', 'Objetos', 'barril.png'),
            "calabera": os.path.join('Data', 'Sprites', 'Objetos', 'calavera.png'),
            "palmeras": os.path.join('Data', 'Sprites', 'Objetos', 'palmeras.png'),
            "Final": os.path.join('Data', 'Sprites', 'Objetos', 'Porton_Final.png')
            }

# imagenchiquita = pygame.transform.scale(Character, (60, 100))
