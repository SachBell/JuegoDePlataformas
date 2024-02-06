# Niveles
from Objetos import *

class Niveles():

    def __init__(self) -> None: 
        pass

    def Lvl_1(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        self.Arbusto1 = Objeto(600, 660, 45, 45, "", "arbusto", True)
        self.Arbusto2 = Objeto(300, 660, 100, 100, "", "arbusto", True)
        self.Arbusto3 = Objeto(450, 660, 45, 45, "", "arbusto", True)
        self.Arbusto4 = Objeto(550, 660, 45, 45, "", "arbusto", True)
        self.Arbusto5 = Objeto(800, 660, 45, 45, "", "arbusto", True)

        self.Pike1 = Objeto(800, 660, 40, 40, "trampa", "pincho", True)
        self.Pike2 = Objeto(700, 660, 40, 40, "trampa", "pincho", True)

        self.PlatTramp = Objeto(380, 660, 40, 40, "trampa", "grass", True)
        self.Tree1 = Objeto(500, 500, 240, 240, "", "arbol2", True)
        self.Tree2 = Objeto(1000, 500, 240, 240, "", "arbol1", True)

        self.Plataform1 = Objeto(500, 600, 40, 40, "muro", "grass", True)
        self.Tree2 = Objeto(1000, 500, 240, 240, "", "arbol1", True)
        self.Arbusto1 = Objeto(800, 660, 45, 45, "", "arbusto", True)
        self.Plataform2 = Objeto(950, 550, 50, 40, "muro", "piedra", True)
        self.Plataform3 = Objeto(850, 400, 50, 40, "muro", "piedra", True)
        self.Plataform4 = Objeto(750, 350, 50, 40, "muro", "piedra", True)
        self.Plataform5 = Objeto(480, 225, 200, 150, "muro", "piedra", True)
        self.Plataform6 = Objeto(45, 165, 60, 50, "muro", "piedra", True)
        self.Plataform7 = Objeto(250, 250, 60, 50, "muro", "piedra", True)
       
        self.End = Objeto(500, 100, 150, 150, "meta", "Final", True)
        self.Coin = Objeto(50, 100, 50, 50, "muro", "moneda", True)

        
        self.Final = Objeto(1000, 500, 300, 200, "meta", "Final", True)

    def Lvl_2(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        
        self.Tree1 = Objeto(100, 500, 240, 240, "", "arbol2", True)
        self.Tree3 = Objeto(500, 500, 240, 240, "", "arbol2", True)
        self.Tree5 = Objeto(900, 500, 240, 240, "", "arbol1", True)
        self.Arbusto1 = Objeto(20, 660, 45, 45, "", "arbusto", True)
        self.Arbusto2 = Objeto(50, 660, 45, 45, "", "arbusto", True)
        self.Arbusto3 = Objeto(250, 660, 180, 45, "", "arbusto", True)
        self.Arbusto4 = Objeto(350, 660, 45, 45, "", "arbusto", True)
        self.Arbusto5 = Objeto(500, 660, 180, 45, "", "arbusto", True)
        self.Arbusto6 = Objeto(800, 660, 45, 45, "", "arbusto", True)
        self.Arbusto7 = Objeto(900, 660, 180, 45, "", "arbusto", True)

        self.Bloque1 = Objeto(200, 600, 50, 100, "muro", "piedra", True)
        self.Bloque2 = Objeto(290, 450, 100, 50, "muro", "piedra", True)
        self.Bloque3 = Objeto(500, 380, 20, 20, "muro", "piedra", True)
        self.Bloque4 = Objeto(700, 380, 10, 10, "muro", "piedra", True)
        self.Bloque5 = Objeto(900, 450, 100, 50, "muro", "piedra", True)
        self.Bloque6 = Objeto(900, 300, 50, 200, "muro", "piedra", True)

        self.Pincho = Objeto(350, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(400, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(450, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho = Objeto(500, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(550, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(600, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(650, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(700, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho = Objeto(750, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(800, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(850, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(900, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(950, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(1000, 650, 50, 50, "", "pincho", True)
        self.Pincho = Objeto(1050, 650, 50, 50, "", "pincho", True)

        self.End = Objeto(1140, 560, 150, 150, "Porton_Final", "Final", True)

        
    def Lvl_4(self):
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
        self.Final = Objeto(1000, 515, 150, 200, "meta", "Final", True)
    
    def Lvl_3(self):
        self.Suelo = Objeto(0, 700, 1500, 240, "muro", "grass", False)
        self.Arbusto1 = Objeto(50, 660, 180, 40, "", "arbusto", True)

        self.Bloque1 = Objeto(200, 650, 50, 50, "muro", "piedra", True)
        self.Bloque2 = Objeto(250, 600, 50, 50, "muro", "piedra", True)
        self.Bloque3 = Objeto(300, 550, 50, 50, "muro", "piedra", True)

        self.Bloque7 = Objeto(200, 50, 800, 300, "muro", "piedra", True)
        self.Bloque8 = Objeto(500, 580, 20, 20, "muro", "piedra", True)
        self.Bloque9 = Objeto(600, 580, 20, 20, "muro", "piedra", True)

        self.Pincho1 = Objeto(250, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho2 = Objeto(300, 650, 50, 50, "trampa", "pincho", True)
        self.Pincho3 = Objeto(760, 685, 15, 15, "trampa", "pincho", True)

        self.DT1 = Objeto(500, 600, 150, 150, "trampa", "DTrap", True)
        self.DT2 = Objeto(820, 380, 150, 150, "trampa", "DTrap", True)
        self.DT3 = Objeto(300, 280, 150, 150, "trampa", "DTrap", True)

        self.Final = Objeto(1000, 515, 150, 200, "meta", "Final", True)

        
               

        
        

        
