import pygame
from Importaciones import *
from Objetos import Objeto

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
        self.Jumping = False
        self.jump_count = 10
        self.gravity = 3
        self.OnGround = False
        self.IdleWait = 0
        self.framecount = 0

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.IdleWait = 3
            self.ChangeSprites("left")
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < screen_width - self.rect.width:
            self.IdleWait = 3
            self.ChangeSprites("right")
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed/2
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed/2

        # Lógica de salto
        if keys[pygame.K_SPACE] and not self.Jumping:
            self.jump_count = 10
        if self.Jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.Jumping = False
                self.jump_count = 10

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
                        self.rect.y = self.LastY
                        self.OnGround = True
                    else:
                        self.rect.x = self.LastX
                        self.rect.y = self.LastY
                        self.OnGround = False
            else:
                self.OnGround = False
        
    def CheckGravity(self):
        if self.OnGround: print("tocando piso")
        else: print("En el aire"); self.rect.y += self.gravity
    
    def ActualizarUltimasCoordenadas(self):
        self.LastX = self.rect.x
        self.LastY = self.rect.y

    def AccionPersonaje(self):
        self.CheckIdle()
        self.CheckCollide()
        self.CheckGravity()
        self.ActualizarUltimasCoordenadas()

        Resize_Character = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        screen.blit(Resize_Character, self.rect)

    def GetX(self): return self.rect.x
    def GetY(self): return self.rect.y
    def GetInitialX(self): return self.InitialX
    def GetInitialY(self): return self.InitialY
