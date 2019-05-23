from LinkedList import *


def delete_dup(lis):
    cur = lis.head
    while (cur != None):
        check = cur
        while (check.get_next() != None):
            if (check.get_next().get_data() == cur.get_data()):
                check.set_next(check.get_next().get_next())
            else:
                check = check.get_next()
        cur = cur.get_next()

a = LinkedList()
a.insert(10)
a.insert(9)
a.insert(8)
a.insert(7)
a.insert(6)
a.insert(5)
a.insert(4)
a.insert(6)
a.insert(7)
a.printNode()
delete_dup(a)
a.printNode()
