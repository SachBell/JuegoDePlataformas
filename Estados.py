import pygame
import sys
from Configuración import *

class States:
    def __init__(self) -> None:
        self.Dead = False
        
    def CheckInput(self, personaje):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    Initialx = personaje.GetInitialX()
                    Initialy = personaje.GetInitialY()
                    self.Reiniciar(Initialx,Initialy, personaje)
                    personaje.jumping = False
                    personaje.jump_count = 10
                    self.Dead = False
    
    def Muerte(self, personaje):
        self.Dead = True
        while self.Dead:
            font = pygame.font.Font(None, 74)
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            restart_text = font.render("Press R to restart", True, (255, 0, 0))
            screen.blit(game_over_text, (Ancho_Pantalla // 2 - 150, Alto_Pantalla // 2 - 50))
            screen.blit(restart_text, (Ancho_Pantalla // 2 - 250, Alto_Pantalla // 2 + 50))
            pygame.display.flip()
            self.CheckInput(personaje)
            reloj.tick(30)
    
    def Reiniciar(self, x, y, personaje):
        personaje.rect.x = x
        personaje.rect.y = y
        Tiempo.ModificarSegundos(0)
        personaje.gravity = 10
        
    
    
