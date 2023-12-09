import pygame as pg

class Cube(object):

    def __init__(self, x, y, size, color=(0, 200, 50)):
        self.x, self.y = x, y
        self.color = color
        self.size = size
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)

    def moveRect(self, xdir, ydir):
        self.rect.x += xdir * self.size
        self.rect.y += ydir * self.size

    def translocateRect(self, newx, newy):
        self.rect.x = newx
        self.rect.y = newy

    def drawRect(self, surface):
        pg.draw.rect(surface, self.color, self.rect, 0, 5)
