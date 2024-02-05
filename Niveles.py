# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None: 
        self.Pincho5 = Objeto(410, 650, 50, 50, "trampa", "pincho", True)

    def Lvl_1(self):
        self.Pike = Objeto(800, 660, 40, 40, "trampa", "pincho", True)
        self.Pike = Objeto(600, 660, 40, 40, "trampa", "pincho", True)
        self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", True)
        self.Plataform = Objeto(500, 600, 40, 40, "muro", "grass", True)
        self.Suelo = Objeto(1000, 500, 240, 240, "", "arbol1", True)
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
    
    def Lvl_3(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        self.Arbusto1 = Objeto(50, 660, 180, 40, "", "arbusto", True)
        

        self.Bloque1 = Objeto(200, 650, 50, 50, "muro", "piedra", True)
        self.Bloque2 = Objeto(250, 600, 50, 50, "muro", "piedra", True)
        self.Bloque3 = Objeto(300, 550, 50, 50, "muro", "piedra", True)

        
        self.Bloque5 = Objeto(520, 550, 50, 50, "muro", "piedra", True)
        self.Bloque6 = Objeto(570, 600, 50, 50, "muro", "piedra", True)
        self.Bloque7 = Objeto(620, 650, 50, 50, "muro", "piedra", True)
        self.Bloque7 = Objeto(700, 450, 50, 50, "muro", "piedra", True)
        

        # self.Pincho1 = Objeto(250, 650, 50, 50, "trampa", "pincho", True)
        # self.Pincho2 = Objeto(300, 650, 50, 50, "trampa", "pincho", True)
        # self.Pincho3 = Objeto(520, 650, 50, 50, "trampa", "pincho", True)
        # self.Pincho4 = Objeto(570, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho5 = Objeto(410, 650, 50, 50, "trampa", "pincho", True)

    def EliminarInstancia(self):
        Objeto.EliminarInstancia(self.Pincho5)      


        
        

        
