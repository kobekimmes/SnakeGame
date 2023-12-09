from Node import Node

class Linkst:

    def __init__(self, node=None):
        self.head = node if node else Node(None, None, None)
        self.len = 0

    def append(self, node):
        ptr = self.head

        while ptr.next:
            ptr = ptr.next

        ptr.next = node
        self.len+=1


    def pop(self):
        if self.len > 1:
            self.head = self.head.next
            self.len -= 1

    def drop(self):
        ptr = self.head
        while ptr and ptr.next and ptr.next.next:
            ptr = ptr.next
        temp = ptr.next
        ptr.next = None
        self.len -= 1
        return temp

    def getEle(self, index):
        ptr = self.head

        while index > 1:
            ptr = ptr.next
            index-=1
        return ptr


    def printQ(self):
        print("start")
        ptr = self.head.next
        while ptr:
            print(ptr.val[0], ptr.val[1])
            ptr = ptr.next
        print("end")
