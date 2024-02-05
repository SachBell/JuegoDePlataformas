# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None:
        pass

    def Lvl_1(self):
        self.Pike = Objeto(800, 660, 40, 40, "trampa", "pincho", True)
        self.Pike = Objeto(600, 660, 40, 40, "trampa", "pincho", True)
        self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", True)
        self.Plataform = Objeto(500, 600, 40, 40, "muro", "grass", True)
        self.Suelo = Objeto(1000, 500, 240, 240, "", "arbol1", True)
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
