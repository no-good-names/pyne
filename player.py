import pygame as pg
from settings import *


class Player:

    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.rect = pg.rect.Rect([self.x, self.y, 30, 30])
        # 0 = w, 1 = a, 2 = d, 3 = s
        self.inputs = [False, False, False, False]

    def draw(self):
        pg.draw.rect(self.game.window, ('green'), self.rect)

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.move_ip(0, -5)
            self.inputs[0] = True
        else:
            self.inputs[0] = False
        if keys[pg.K_a]:
            self.rect.move_ip(-5, 0)
            self.inputs[1] = True
        else:
            self.inputs[1] = False
        if keys[pg.K_d]:
            self.rect.move_ip(5, 0)
            self.inputs[2] = True
        else:
            self.inputs[2] = False
        if keys[pg.K_s]:
            self.rect.move_ip(0, 5)
            self.inputs[3] = True
        else:
            self.inputs[3] = False

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
