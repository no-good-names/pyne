import pygame as pg
import sys
from settings import *
from player import *


class Game:

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((RES))
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.player = Player(self)

    def update(self):
        self.clock.tick(FPS)
        pg.display.flip()
        pg.display.update()
        self.player.update()

    def draw(self):
        self.window.fill('black')
        self.player.draw()

    def event_check(self):
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.event_check()


if __name__ == '__main__':
    game = Game()
    game.run()
