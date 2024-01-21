#La importación pygame ahora será conocida como "pg"
import pygame as pg
import sys
from Configuración import *


# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game():

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(Resolucion)
        self.clock = pg.time.Clock()

    def draw(self):
        self.screen.fill('black')

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.2f}")

    def check_events(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.draw()
            self.update()
            self.check_events()

main = Game()
main.run()