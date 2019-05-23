from Node import *

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        cur = self.head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.get_next()
        return count

    def search(self, data):
        cur = self.head
        found = False
        while cur and found is False:
            if cur.get_data() == data:
                found = True
            else:
                cur = cur.get_next()
        if cur is None:
            raise ValueError("Data not in list")
        return cur

    def delete(self, data):
        cur = self.head
        found = False
        pre = None
        while cur and found is False:
            if cur.get_data == data:
                found = True
            else:
                pre = cur
                cur = cur.get_next()
        if cur is None:
            raise ValueError("Data not in list")
        if pre is None:
            self.head = cur.get_next()
        else:
            pre.set_next(cur.get_next())

    def printNode(self):
        cur = self.head
        while cur:
            print(cur.get_data())
            cur = cur.get_next()
