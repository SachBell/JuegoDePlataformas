# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None: 
        self.Pincho5 = Objeto(410, 650, 50, 50, "trampa", "pincho", True)

    def Lvl_1(self):
        self.Pike1 = Objeto(800, 660, 40, 40, "trampa", "pincho", True)
        self.Arbusto1 = Objeto(300, 660, 100, 100, "", "arbusto", True)
        self.Arbusto1 = Objeto(450, 660, 45, 45, "", "arbusto", True)
        self.Arbusto1 = Objeto(550, 660, 45, 45, "", "arbusto", True)
        self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", True)
        self.Tree1 = Objeto(500, 500, 240, 240, "", "arbol2", True)
        self.Pike2 = Objeto(700, 660, 40, 40, "trampa", "pincho", True)
        self.Arbusto1 = Objeto(600, 660, 45, 45, "", "arbusto", True)
        self.Plataform1 = Objeto(500, 600, 40, 40, "muro", "grass", True)
        self.Tree2 = Objeto(1000, 500, 240, 240, "", "arbol1", True)
        self.Arbusto1 = Objeto(800, 660, 45, 45, "", "arbusto", True)
        self.Plataform2 = Objeto(950, 550, 50, 40, "muro", "piedra", True)
        self.Plataform3 = Objeto(850, 400, 50, 40, "muro", "piedra", True)
        self.Plataform4 = Objeto(750, 350, 50, 40, "muro", "piedra", True)
        self.End = Objeto(500, 100, 150, 150, "Porton_Final", "Final", True)
        self.Plataform5 = Objeto(480, 225, 200, 150, "muro", "piedra", True)
        self.Coin = Objeto(50, 100, 50, 50, "moneda", "moneda", True)
        self.Plataform7 = Objeto(45, 165, 60, 50, "muro", "piedra", True)
        self.Plataform6 = Objeto(250, 250, 60, 50, "muro", "piedra", True)
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


        
        

        
    
    def Lvl_3(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        self.Arbusto1 = Objeto(50, 660, 180, 40, "", "arbusto", True)
        

        self.Bloque1 = Objeto(200, 650, 50, 50, "muro", "piedra", True)
        self.Bloque2 = Objeto(250, 600, 50, 50, "muro", "piedra", True)
        self.Bloque3 = Objeto(300, 550, 50, 50, "muro", "piedra", True)
        self.Bloque5 = Objeto(520, 550, 50, 50, "muro", "piedra", True)
        self.Bloque6 = Objeto(570, 600, 50, 50, "muro", "piedra", True)
        self.Bloque7 = Objeto(620, 650, 50, 50, "muro", "piedra", True)
        self.Bloque7 = Objeto(670, 450, 50, 50, "muro", "piedra", True)
        

        self.Pincho1 = Objeto(250, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho2 = Objeto(300, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho3 = Objeto(520, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho4 = Objeto(570, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho5 = Objeto(410, 650, 50, 50, "trampa", "pincho", True)


        
        

        
