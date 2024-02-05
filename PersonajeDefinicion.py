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
        self.JumpSpeed = 10
        self.Jumping = False
        self.CheckAgain = True
        self.IfCollide = False
        self.IfCollide2 = False
        self.Jump_Speed = 28
        self.gravity = 3
        self.OnGround = False
        self.IdleWait = 0
        self.framecount = 0
        self.i = 0

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
            self.Time = 5
            self.Decrease = 7
            self.Jumping = True
        if self.Jumping:
            if self.Jump_Speed > 0:
                for i in range(0,self.JumpSpeed):
                    self.rect.y -= 1
                if Tiempo.FrameLimiter(self.Time):
                    self.Jump_Speed -= self.Decrease
                    self.Time += 1
                    self.Decrease -= 1
                print(f"{self.Jump_Speed} {self.Time} {self.Decrease}") 
            else: 
                self.Jumping = False
                self.Jump_Speed = 28

    def CheckIdle(self):
        if self.IdleWait == 0:
            self.Current_Sprites = self.Sprites_Idle
            self.image = self.Current_Sprites[0]
        else: 
            self.IdleWait -=1
            self.CheckAgain = True
        
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
                        self.rect.y = (Objeto_Actual.rect.top - self.rect.height)+1
                        self.IfOnGround()
                    
                    else:
                        self.rect.x = self.LastX
                        self.rect.y = self.LastY
                        self.HasCollided(True)
                        print("colision")
                elif Objeto_Actual.GetTipo() == "trampa":
                        print("auch")
                        Estados.Muerte(self)    
                                        
            else:
                print("No colision")
                self.HasCollided(False)

    def HasCollided(self, check):
        if self.i == 0:
            self.IfCollide = check; self.i = 1
        elif self.i == 1:
            self.IfCollide2 = check; self.i = 0
        
        if (self.IfCollide == False and self.IfCollide2 == False):
            self.CheckAgain = True
            self.OnGround = False
            # print(self.IfCollide)
            # print(self.IfCollide2)
            print("condicion cumplida")

    def IfOnGround(self):
        self.OnGround = True
        # print("Tocando el piso")
    
    def IfNotOnGround(self):
        self.OnGround = False
        # print("No tocando el piso")

    def CheckGravity(self):
        if self.CheckAgain:    
            if self.OnGround: 
                # print("tocando piso\r")
                self.gravity = 3
                self.CheckAgain = False
                self.Jumping = False
            else: 
                print("En el aire")
                self.rect.y += self.gravity
            
    def ApplyGravity(self):
        self.rect.y += self.gravity
        
    def ActualizarUltimasCoordenadas(self):
        self.LastX = self.rect.x
        self.LastY = self.rect.y

    def AccionPersonaje(self):
        self.CheckIdle()
        self.CheckInput()
        self.CheckCollide()
        self.CheckGravity()
        self.ActualizarUltimasCoordenadas()
        # print(f"{self.CheckAgain}\r")
        Resize_Character = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        screen.blit(Resize_Character, self.rect)

    def GetX(self): return self.rect.x
    def GetY(self): return self.rect.y
    def GetInitialX(self): return self.InitialX
    def GetInitialY(self): return self.InitialY
