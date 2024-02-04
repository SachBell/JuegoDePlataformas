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
        self.rect = pygame.Rect(0,0,165,300)
        self.rect.width = 165
        self.rect.height = 384
        self.InitialX = x
        self.InitialY = y
        self.LastX = self.InitialX
        self.LastY = self.InitialY
        self.rect.x = x
        self.rect.y = y
        self.speed = 20
        self.Jumping = False
        self.jump_count = 10
        self.gravity = 0
        self.OnGround = True
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

        # Aplicar gravedad
        if not self.Jumping and not self.OnGround:
            self.rect.y += self.gravity

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
                    self.rect.x = self.LastX
                    self.rect.y = self.LastY

                    if Tiempo.FrameLimiter(50):
                        
                        print(f"izquierda {(self.rect.right - Objeto_Actual.rect.left)}")
                        print(f"derecha {(self.rect.left - Objeto_Actual.rect.right)}")
                        print(f"arriba {(self.rect.bottom - Objeto_Actual.rect.top)}")
                        print(f"abajo {(self.rect.top - Objeto_Actual.rect.bottom)}")
                    print(self.LastX)
                    print(self.LastY)
            else:
                self.OnGround = False
        self.LastX = self.rect.x
        self.LastY = self.rect.y

    def AccionPersonaje(self):
        self.CheckIdle()
        self.CheckCollide()

    def GetX(self): return self.rect.x
    def GetY(self): return self.rect.y
    def GetInitialX(self): return self.InitialX
    def GetInitialY(self): return self.InitialY
