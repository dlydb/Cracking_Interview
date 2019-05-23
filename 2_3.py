from LinkedList import *

def del_mid_node(lis, val):
    cur = lis.head
    if cur.get_data() == val:
        head = cur.get_next()
    while (cur.get_next() != None):
        if cur.get_next().get_data() == val:
            cur.set_next(cur.get_next().get_next())
        cur = cur.get_next()

a = LinkedList()
a.insert(10)
a.insert(9)
a.insert(8)
a.insert(7)
a.insert(6)
a.insert(5)
a.insert(4)

del_mid_node(a, 6)
a.printNode()
