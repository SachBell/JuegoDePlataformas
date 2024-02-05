# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None:
        pass

    def Lvl_1(self):
        self.Pike = Objeto(800, 660, 40, 40, "trampa", "pincho", "objeto", True)
        self.Pike = Objeto(600, 660, 40, 40, "trampa", "pincho", "objeto", True)
        self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", "textura", True)
        self.Plataform = Objeto(500, 600, 40, 40, "muro", "grass", "textura", True)
        self.Suelo = Objeto(1000, 500, 240, 240, "", "arbol1", "objeto", True)
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", "textura",False)
