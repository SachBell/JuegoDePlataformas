#Configuración
import pygame

#Definición de colores
celeste = (0, 100, 255)
blanco = (255, 255, 255)
pygame.font.init()
#Objeto tipo Clock
reloj = pygame.time.Clock()

#Control del tiempo
class TimeControl:
    def __init__(self) -> None:
        self.Limit = 0
        self.font = pygame.font.Font(None, 25)
        self.segundos = 0 #Segundos iniciales
        self.frames = 0 #Frames iniciales
        self.Tics_Iniciales = pygame.time.get_ticks() #Tics antes de la inicialización

    def ComenzarTiempo(self):
        self.Tics_Actuales = pygame.time.get_ticks()
        count = self.Tics_Actuales-self.Tics_Iniciales
        self.frames +=1
        if count >= 1000:
            self.segundos+=1
            self.Tics_Iniciales = self.Tics_Actuales
            return self.segundos

    def MostrarTiempo(self):
        self.Tics_Actuales = pygame.time.get_ticks()
        count = self.Tics_Actuales-self.Tics_Iniciales
        Segundos_Text = self.font.render(f"{self.segundos} seg", True, celeste)
        if count >= 1000:
            self.segundos+=1
            screen.blit(Segundos_Text, (50, 50))
            self.Tics_Iniciales = self.Tics_Actuales
            return self.segundos
    
    def FrameLimiter(self, frameslimit):
        self.Limit+=1
        if self.Limit == frameslimit: self.Limit = 0; return True
        else: return False

    def GetLimit(self):
        return self.Limit
    def RetornarSegundos(self):
        return self.segundos
    def RetornarFrames(self):
        return self.frames
    
    def ModificarSegundos(self, seg):
        self.segundos = seg
        

#Objeto para control del tiempo
Tiempo = TimeControl()  
Timer1 = TimeControl()
Timer2 = TimeControl()
Timer3 = TimeControl()
Timer4 = TimeControl()
Timer5 = TimeControl()

#Definición de la pantalla
Resolucion = Ancho_Pantalla, Alto_Pantalla = (1280, 720)
screen = pygame.display.set_mode((Resolucion), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SRCALPHA)