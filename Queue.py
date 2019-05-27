from Node import *

class Queue(object):
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def add(self, data):
        new = Node(data)
        if (self.tail != None):
            self.tail.set_next(new)
            self.tail = new
        else:
            self.head = new
            self.tail = new
        new.set_next(None)

    def remove(self):
        if self.head != None:
            nex = self.head.get_next()
            data = self.head.get_data()
            self.head = nex
            return data

    def peek(self):
        if self.head != None:
            return self.head.get_data()

    def isEmpty(self):
        return (self.head == None)
