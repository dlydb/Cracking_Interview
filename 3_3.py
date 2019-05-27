from Stack import *

class MyQueue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def pop(self):
        while (self.stack1.isEmpty() == False):
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()

    def push(self, data):
        while (self.stack2.isEmpty() == False):
            self.stack1.push(self.stack2.pop())
        self.stack1.push(data)

    def peek(self):
        while (self.stack1.isEmpty() == False):
            self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def isEmpty(self):
        return self.stack1.isEmpty() or self.stack2.isEmpty()

    def printNode(self):
        if self.stack1.isEmpty():
            self.stack2.printNode()
        else:
            self.stack1.printNode()


a = MyQueue()
a.push(10)
a.push(8)
a.push(5)
a.push(7)
a.pop()
a.printNode()
b = Stack()
b.push(10)
b.push(8)
b.push(5)
b.push(7)
b.pop()
b.printNode()
