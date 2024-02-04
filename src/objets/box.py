import pygame

class Caja:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def get_hitbox(self):
        # Devuelve un rectángulo ligeramente más grande que la caja para actuar como hitbox
        margin = 10
        return pygame.Rect(self.rect.x - margin, self.rect.y - margin, self.width + 2 * margin, self.height + 2 * margin)

