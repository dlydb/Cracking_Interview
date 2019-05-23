from LinkedList import *


def k_th_last(lis, k):
    p1 = lis.head
    p2 = lis.head

    for i in range(k):
        if p2.get_next() != None:
            p2 = p2.get_next()

    while (p2.get_next() != None):
        p1 = p1.get_next()
        p2 = p2.get_next()

    return p1.get_data()

a = LinkedList()
a.insert(10)
a.insert(9)
a.insert(8)
a.insert(7)
a.insert(6)
a.insert(5)
a.insert(4)

a.printNode()
print(k_th_last(a, 3))
