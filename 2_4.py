from LinkedList import *
from Node import *


def partition(lis, val):
    cur = lis.head
    larg = LinkedList()
    smal = LinkedList()
    while (cur != None):
        if cur.get_data() < val:
            if smal == None:
                smal.insert(cur.get_data())
            else:
                smal.insert(cur.get_data())
        elif cur.get_data() >= val:
            if larg == None:
                larg.insert(cur.get_data())
            else:
                larg.insert(cur.get_data())
        cur = cur.get_next()
    return larg, smal

a = LinkedList()
a.insert(10)
a.insert(9)
a.insert(8)
a.insert(7)
a.insert(6)
a.insert(5)
a.insert(4)

la, sm = partition(a, 6)
la.printNode()
print("!!!!!!!!")
sm.printNode()
