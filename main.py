import random
import pygame as pg
from Cube import Cube
from Snake import Snake


class Game:

    def __init__(self, screen_size=500, block_size=10, FPS=30, g = True, easy = True):
        self.ss = screen_size
        self.bs = block_size
        self.RES = screen_size // block_size
        self.FPS = FPS
        self.g = g
        self.easy = easy
        self.surface = pg.display.set_mode((screen_size, screen_size))
        self.clock = pg.time.Clock()
        self.flag = False
        self.win = False
        self.apple = Cube(random.randint(1, self.ss-1) // self.bs * self.bs, random.randint(1, self.ss-1) // self.bs * self.bs, self.bs, (255, 0, 0))



    def backGround(self):
        self.surface.fill((0, 50, 0))

    def drawGrid(self):

        for i in range(self.RES):
            pg.draw.line(self.surface, (0, 0, 0), (i * self.bs, 0), (i * self.bs, self.ss))
            pg.draw.line(self.surface, (0, 0, 0), (0, i * self.bs), (self.ss, i * self.bs))

    def getInput(self, snake):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.flag = True
                pg.quit()

            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()

                if keys[pg.K_LEFT]:
                    snake.dirx = -1
                    snake.diry = 0

                elif keys[pg.K_RIGHT]:
                    snake.dirx = 1
                    snake.diry = 0
                elif keys[pg.K_DOWN]:
                    snake.diry = 1
                    snake.dirx = 0
                elif keys[pg.K_UP]:
                    snake.diry = -1
                    snake.dirx = 0

    def checkBorder(self, snake):
        if snake.head.rect.x >= self.ss:
            snake.head.translocateRect(-self.bs, snake.head.rect.y)
        elif snake.head.rect.x < 0:
            snake.head.translocateRect(self.ss, snake.head.rect.y)

        elif snake.head.rect.y >= self.ss:
            snake.head.translocateRect(snake.head.rect.x, -self.bs)
        elif snake.head.rect.y < 0:
            snake.head.translocateRect(snake.head.rect.x, self.ss)

    def checkBorderCrash(self, snake):
        if snake.head.rect.x >= self.ss or snake.head.rect.x < 0 or snake.head.rect.y >= self.ss or snake.head.rect.y < 0:
            self.flag = True


    def genNewApple(self):
        self.apple = Cube(random.randint(1, self.ss-1) // self.bs * self.bs, random.randint(1, self.ss-1) // self.bs * self.bs, self.bs, (255, 0, 0))

    def eatApple(self, snake):
        if snake.head.rect.colliderect(self.apple.rect):
            snake.grow(self.bs)
            self.genNewApple()

    def selfCollide(self, snake):
        for cube in snake.body[2:]:
            if snake.head.rect.colliderect(cube.rect):
                self.flag = True

    def checkWin(self, snake):
        if snake.length == (self.RES * self.RES):
            self.win = True


    def main_loop(self):
        s = Snake(self.surface, Cube((self.ss//2)// self.bs * self.bs, (self.ss//2)// self.bs * self.bs, self.bs))

        while not self.flag:
            self.backGround()
            if self.g:
                self.drawGrid()

            if self.easy:
                self.checkBorder(s)
            else:
                self.checkBorderCrash(s)


            s.headMove()
            s.trackHeadMovement()
            s.bodyMove()
            s.drawSnake(self.surface)

            self.getInput(s)
            self.selfCollide(s)
            self.eatApple(s)
            self.checkWin(s)

            self.apple.drawRect(self.surface)


            pg.display.flip()
            self.clock.tick(self.FPS)






        pg.quit()


snake = Game(600, 20, 10, False)
snake.main_loop()
