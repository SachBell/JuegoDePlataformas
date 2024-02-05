
import pygame
from Configuración import *
from Importaciones import *

class Objeto():

    ObjetosCreados = []

    def __init__(self, x, y, width, height, tipo, textura, Resize):
        self.Resize = Resize
        self.textura = textura
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)  # Cambia el color a verde
        Objeto.ObjetosCreados.append(self)
    
    def GetTipo(self):
        return self.tipo
    
    def GetTextura(self):
        return self.textura
    
    def GetIfResize(self):
        return self.Resize

    @classmethod
    def DibujarObjetos(cls, screen):
        for Objeto_Seleccionado in cls.ObjetosCreados:
            pygame.draw.rect(screen, Objeto_Seleccionado.color, Objeto_Seleccionado.rect)
            cls.TexturizarObjetos(Objeto_Seleccionado, Objeto_Seleccionado.GetTextura())
    
    @classmethod
    def TexturizarObjetos(cls, Objeto_Para_Texturizar, Textura):
        Ruta_Parcial = Texturas[Textura]
        Ruta_Completa = os.path.join(Directorio_Principal, Ruta_Parcial)
        Textura_Seleccionada = pygame.image.load(Ruta_Completa)
        if Objeto_Para_Texturizar.GetIfResize() == True: Textura_Seleccionada = pygame.transform.scale(Textura_Seleccionada, (Objeto_Para_Texturizar.rect.width, Objeto_Para_Texturizar.rect.height))
        
        for i in range(Objeto_Para_Texturizar.rect.left, Objeto_Para_Texturizar.rect.right, Textura_Seleccionada.get_width()):
            for j in range(Objeto_Para_Texturizar.rect.top, Objeto_Para_Texturizar.rect.bottom, Textura_Seleccionada.get_height()):
                screen.blit(Textura_Seleccionada, (i, j))

    @classmethod
    def TodosLosObjetos(cls):
        return cls.ObjetosCreados
    

    