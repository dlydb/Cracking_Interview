from LinkedList import *

def intersection(lis1, lis2):
    size1 = lis1.size()
    size2 = lis2.size()
    cur1 = lis1.head
    cur2 = lis2.head
    if size1 > size2:
        for i in range(size1 - size2):
            cur1 = cur1.get_next()
    elif size2 > size1:
        for i in range(size2 - size1):
            cur2 = cur2.get_next()
    while (cur1 != cur2 and cur1 != None and cur2 != None):
        cur1 = cur1.get_next()
        cur2 = cur2.get_next()
    if cur1 == None or cur2 == None:
        return False
    else:
        return True
