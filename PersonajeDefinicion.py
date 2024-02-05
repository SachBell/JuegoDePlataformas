import pygame
from Importaciones import *
from Objetos import Objeto
from Configuración import *
from Estados import *


Estados = States()

class Personaje:
    def __init__(self, x, y):
        self.Sprites_Idle = [pygame.image.load('./Data/Sprites/Stickman/Stickman_Idle.png')]

        self.Sprites_Caminando_Izquierda = [pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Left_1.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Left_2.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Left_3.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Left_4.png')]
        
        self.Sprites_Caminando_Derecha = [pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Right_1.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Right_2.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Right_3.png'),
                                          pygame.image.load('./Data/Sprites/Stickman/Stickman_Walk_Right_4.png')]
        
        self.Current_Sprites = self.Sprites_Idle
        self.Sprite_Index = 0
        self.image = self.Current_Sprites[self.Sprite_Index]
        self.rect = pygame.Rect(0, 0, 60, 140)
        self.InitialX = x
        self.InitialY = y
        self.LastX = self.InitialX
        self.LastY = self.InitialY
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.JumpSpeed = 16
        self.Jumping = False
        self.CheckAgain = True
        self.IfCollide = False
        self.IfCollide2 = False
        self.HaveGround = False
        self.Jump_Speed = 10
        self.gravity = 10
        self.AddedGravity = 0
        self.OnGround = False
        self.IdleWait = 0
        self.framecount = 0
        self.i = 0
        self.count = 0
        self.Time = 2
        self.Decrease = 2
        self.StopJumping = False

    def CheckInput(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.IdleWait = 3
            self.ChangeSprites("left")
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < Ancho_Pantalla - self.rect.width:
            self.IdleWait = 3
            self.ChangeSprites("right")
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed/2
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed/2


        
        # Lógica de salto
        if keys[pygame.K_SPACE] and self.OnGround and not self.Jumping:
            self.Jump_Speed = 30
            self.Time = 0
            self.Decrease = 1
            self.Jumping = True
            self.count = 20
        elif self.Jumping and not self.StopJumping:
              
                    if self.count > 0 and self.Decrease > 0 and self.Jump_Speed > 0:
                        for i in range(0, (self.Jump_Speed - self.Decrease)):
                            self.rect.y -= 1
                            self.CheckCollide()
                        self.count -= 1
                        self.Time+=1
                        if self.Time >= 3:
                            self.Decrease += 4; self.Time = 0

                        print(f"jumping {self.count} {self.Decrease} {(self.Jump_Speed - self.Decrease)}")
                    else:
                        self.StopJumping = True 
                        
        
        # print(f"{self.Jump_Speed} {self.Time} {self.Decrease} {self.rect.x} {self.rect.y} {self.Jumping} {self.OnGround} {self.StopJumping}")

         

    def CheckIdle(self):
        if self.IdleWait == 0:
            self.Current_Sprites = self.Sprites_Idle
            self.image = self.Current_Sprites[0]
        else: 
            self.IdleWait -=1
        
    def ChangeSprites(self, side):
        if side == "left": self.Current_Sprites = self.Sprites_Caminando_Izquierda
        if side == "right": self.Current_Sprites = self.Sprites_Caminando_Derecha
        self.AnimateSprites(8)

    def AnimateSprites(self, rate):
        frames = Tiempo.RetornarFrames()
        if (frames-self.framecount) >= rate:
            self.Sprite_Index = (self.Sprite_Index + 1)
            if self.Sprite_Index == len(self.Current_Sprites): self.Sprite_Index = 0
            self.image = self.Current_Sprites[self.Sprite_Index]
            self.framecount = frames

    def CheckCollide(self):
        Objetos = Objeto.TodosLosObjetos()
        for Objeto_Actual in Objetos:          
            if self.rect.colliderect(Objeto_Actual.rect):
                if Objeto_Actual.GetTipo() == "muro":

                    if (self.rect.bottom - 10) < Objeto_Actual.rect.top : 
                        self.Ground = Objeto_Actual
                        self.HaveGround = True
                    elif (self.rect.top + 10) > Objeto_Actual.rect.bottom:
                        self.rect.y = self.LastY
                    else:
                        self.rect.x = self.LastX
                        
                elif Objeto_Actual.GetTipo() == "trampa":

                        Estados.Muerte(self)                 
            else:
                # print("No colision")
                pass
    
    def CheckCollideGround(self, Ground):
        if self.rect.colliderect(Ground.rect):
            self.rect.y = (Ground.rect.top - self.rect.height)+1
            self.IfOnGround()
            self.HasCollided(True)
            # print("encima")
        else:
            self.HasCollided(False)


    def HasCollided(self, check):
        if self.i == 0:
            self.IfCollide = check; self.i = 1
        elif self.i == 1:
            self.IfCollide2 = check; self.i = 0
        
        if (self.IfCollide == False and self.IfCollide2 == False):
            self.CheckAgain = True
            self.OnGround = False
            
        #     print("condicion cumplida")
        # print(self.IfCollide)
        # print(self.IfCollide2)

    def IfOnGround(self):
        self.OnGround = True
        # print("Tocando el piso")
    
    def IfNotOnGround(self):
        self.OnGround = False
        # print("No tocando el piso")

    def CheckGravity(self):
        if self.CheckAgain:    
            if self.OnGround: 
                print("Tocando piso 2")
                self.AddedGravity = 0
                self.gravity = 10
                self.CheckAgain = False
                if self.count > 0: pass
                else:
                    self.Jumping = False
                    self.StopJumping = False
            else: 
                # print("En el aire")
                self.AplicarGravedad(self.gravity)
    
    def AplicarGravedad(self, Gravedad):
        print(self.AddedGravity)
        for i in range(0, Gravedad):
            self.rect.y += 1
            self.CheckCollide()
        if self.AddedGravity >= 20:
            self.gravity += 1
               
        self.AddedGravity += 1
            
        
        
    def ActualizarUltimasCoordenadas(self):
        self.LastX = self.rect.x
        self.LastY = self.rect.y

    def AccionPersonaje(self):
        self.CheckIdle()
        self.CheckInput()
        self.CheckCollide()
        self.CheckGravity()
        if self.HaveGround: self.CheckCollideGround(self.Ground)
        self.ActualizarUltimasCoordenadas()
        # print(f"{self.CheckAgain}\r")
        Resize_Character = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        screen.blit(Resize_Character, self.rect)

    def GetX(self): return self.rect.x
    def GetY(self): return self.rect.y
    def GetInitialX(self): return self.InitialX
    def GetInitialY(self): return self.InitialY
