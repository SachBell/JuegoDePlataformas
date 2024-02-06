# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None: 
        pass

    def Lvl_1(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        # self.Arbusto1 = Objeto(600, 660, 45, 45, "", "arbusto", True)
        # self.Arbusto2 = Objeto(300, 660, 100, 100, "", "arbusto", True)
        # self.Arbusto3 = Objeto(450, 660, 45, 45, "", "arbusto", True)
        # self.Arbusto4 = Objeto(550, 660, 45, 45, "", "arbusto", True)
        # self.Arbusto5 = Objeto(800, 660, 45, 45, "", "arbusto", True)

        # self.Pike1 = Objeto(800, 660, 40, 40, "trampa", "pincho", True)
        # self.Pike2 = Objeto(700, 660, 40, 40, "trampa", "pincho", True)

        # self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", True)
        # self.Tree1 = Objeto(500, 500, 240, 240, "", "arbol2", True)
        # self.Tree2 = Objeto(1000, 500, 240, 240, "", "arbol1", True)

        self.Plataform1 = Objeto(500, 600, 40, 40, "muro", "grass", True)
        self.Plataform2 = Objeto(950, 550, 50, 40, "muro", "piedra", True)
        self.Plataform3 = Objeto(850, 400, 50, 40, "muro", "piedra", True)
        self.Plataform4 = Objeto(750, 350, 50, 40, "muro", "piedra", True)
        self.Plataform5 = Objeto(480, 225, 200, 150, "muro", "piedra", True)
        self.Plataform6 = Objeto(45, 165, 60, 50, "muro", "piedra", True)
        self.Plataform7 = Objeto(250, 250, 60, 50, "muro", "piedra", True)
       
        self.End = Objeto(500, 100, 150, 150, "meta", "Final", True)
        self.Coin = Objeto(50, 100, 50, 50, "muro", "moneda", True)

    def Lvl_2(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        self.Bloque1=Objeto(300,500,50,150, "muro","piedra",True)
        self.Bloque3=Objeto(0,550,50,50, "muro","piedra",True)
        self.Bloque4=Objeto(160,500,50,50, "muro","piedra",True)
        self.Bloque5=Objeto(0,400,50,50, "muro","piedra",True)
        self.Bloque6=Objeto(180,350,20,20, "muro","piedra",True)
        self.Bloque7=Objeto(210,200,50,150, "muro","piedra",True)
        self.Bloque8=Objeto(600,650,50,50, "trampa","piedra",True)

        self.Pincho1=Objeto(110,650,50,50, "trampa","pincho",True)
        self.Pincho2=Objeto(160,650,50,50, "trampa","pincho",True)
        self.Pincho3=Objeto(210,650,50,50, "trampa","pincho",True)
        self.Pincho4=Objeto(160,450,50,50, "trampa","pincho",True)
        self.Pincho5=Objeto(300,450,50,50, "trampa","pincho",True)
        self.Pincho6=Objeto(500,650,50,50, "trampa","pincho",True)
        self.Pincho8=Objeto(390,650,50,50, "trampa","pincho",True)
        self.Pincho9=Objeto(650,650,50,50, "trampa","pincho",True)
        self.Pincho10=Objeto(550,650,50,50, "muro","pincho",True)
        
        self.Barril1=Objeto(700,650,50,50, "muro","barril",True)
        
        self.Final = Objeto(1000, 500, 300, 200, "meta", "Final", True)
    
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


        
        

        
