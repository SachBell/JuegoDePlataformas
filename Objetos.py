
import pygame

class Objeto():

    ObjetosCreados = []

    def __init__(self, x, y, width, height, tipo):
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)  # Cambia el color a verde
        Objeto.ObjetosCreados.append(self)
    
    def GetTipo(self):
        return self.tipo

    @classmethod
    def DibujarObjetos(cls, screen):
        for i in Objeto.ObjetosCreados:
            pygame.draw.rect(screen, i.color, i.rect)

    @classmethod
    def TodosLosObjetos(cls):
        return Objeto.ObjetosCreados
    

    