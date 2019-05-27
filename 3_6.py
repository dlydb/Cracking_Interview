from Queue import *

class Shelter(Object):
    def __init__(self):
        self.que = Queue()

    def enqueue(self, type):
        self.que.add(type)

    def dequeueAny(self):
        return self.que.remove()

    def dequeueDog(self):
        tmp = Queue()
        while self.que.peek() != "dog" and self.que.isEmpty() == False:
            tmp.add(self.que.remove())
        if self.que.isEmpty() == True:
            self.que = tmp
            return None
        else:
            cur = self.que.remove()
            while tmp.isEmpty() == False:
                self.que.add(tmp.que.remove())
            return cur

    def dequeueDog(self):
        tmp = Queue()
        while self.que.peek() != "cat" and self.que.isEmpty() == False:
            tmp.add(self.que.remove())
        if self.que.isEmpty() == True:
            self.que = tmp
            return None
        else:
            cur = self.que.remove()
            while tmp.isEmpty() == False:
                self.que.add(tmp.que.remove())
            return cur
