import pygame

class Personaje:
    def __init__(self, x, y, speed=20):
        self.image = pygame.image.load('./PROYECTOS/Juegodeplataformas/src/img/Imagen.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.jumping = False
        self.jump_count = 10
        self.gravity = 50
        self.on_ground = False

    def move(self, keys, screen_width, screen_height, caja):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < screen_width - self.rect.width:
            self.rect.x += self.speed

        # Aplicar gravedad
        if not self.jumping and not self.on_ground:
            self.rect.y += self.gravity

        # Verificar colisión con la caja
        if self.rect.colliderect(caja.get_hitbox()):
            self.on_ground = True
            self.jumping = False
            self.jump_count = 10
            # Ajustar la posición del personaje al tocar la caja
            if keys[pygame.K_SPACE]:
                self.rect.y = caja.get_hitbox().y - self.rect.height
        else:
            self.on_ground = False

        # Lógica de salto
        if keys[pygame.K_SPACE] and not self.jumping and self.on_ground:
            self.jumping = True

        if self.jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jumping = False
                self.jump_count = 10

        # Restablecer la posición del personaje al salir de la vista
        if self.rect.y > screen_height:
            self.rect.y = 100
            self.rect.x = 20
            self.on_ground = False
            self.jumping = False
            self.jump_count = 10