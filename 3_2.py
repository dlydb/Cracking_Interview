from NodeWithMin import *

class Stack(object):
    def __init__(self, head = None):
        self.head = head

    def pop(self):
        if self.head != None:
            cur = self.head
            self.head = cur.get_next()

    def push(self, data):
        cur = NodeWithMin(data)
        cur.set_next(self.head)
        self.head = cur

    def min(self):
        return (self.head.get_min())


    def peek(self):
        if self.head != None:
            return self.head

    def isEmpty(self):
        return top == None

    def printNode(self):
        cur = self.head
        while cur:
            print(cur.get_data())
            cur = cur.get_next()

a = Stack()
a.push(8)
a.push(5)
a.push(9)
a.push(3)
print(a.min())
print(a.printNode())
a.pop()
print(a.min())
