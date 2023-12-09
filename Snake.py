from Cube import Cube
from Node import Node
from Linkst import Linkst


class Snake(object):

    def __init__(self, surface, head):
        self.surface = surface

        self.head = head
        self.body = [self.head]
        self.length = 1

        self.moveQ = Linkst(Node(0,0,None))

        self.dirx = 0
        self.diry = -1

    def trackHeadMovement(self):
        if self.moveQ.len >= 3:
            self.moveQ.pop()
        self.moveQ.append(Node(self.head.rect.x, self.head.rect.y, None))

    def headMove(self):
        self.head.moveRect(self.dirx, self.diry)

    def bodyMove(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].translocateRect(self.body[i-1].rect.x, self.body[i-1].rect.y)

    def recentMove(self):
        ptr = self.moveQ.head
        while ptr:
            ptr = ptr.next
        return ptr.val

    def grow(self, size):
        (x, y) = self.moveQ.getEle(2).val
        self.body.append(Cube(x, y, size, (self.length, 200-(self.length*2),50)))
        self.length+=1

    def drawSnake(self, surface):
        for cube in self.body:
            cube.drawRect(surface)

    def printBody(self):
        i = 1
        for cube in self.body:
            if i == 1:
                print("Head is located at ("+str(cube.rect.x)+", " + str(cube.rect.y)+")")
            else:
                print(str(i) + "th is located at (" + str(cube.rect.x) + ", " + str(cube.rect.y) + ")")
            i+=1



