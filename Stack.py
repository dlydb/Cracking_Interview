from Node import *

class Stack(object):
    def __init__(self, head = None):
        self.head = head

    def pop(self):
        if self.head != None:
            cur = self.head
            self.head = cur.get_next()
            return cur.get_data()
        else:
            return None

    def push(self, data):
        cur = Node(data)
        cur.set_next(self.head)
        self.head = cur

    def peek(self):
        if self.head != None:
            return self.head.get_data()

    def isEmpty(self):
        return self.head == None

    def printNode(self):
        cur = self.head
        while cur:
            print(cur.get_data())
            cur = cur.get_next()
