from LinkedList import *
def pal(lis):
    size = lis.size()
    new_list = LinkedList()
    cur = lis.head
    for i in range(size//2 - 1):
        cur = cur.get_next()
    tem = cur
    cur = cur.get_next()
    tem.set_next(None)
    if size % 2 == 1:
        cur = cur.get_next()
    new_list.head = cur
    cur = cur.get_next()
    while (cur != None):
        new_list.insert(cur.get_data())
        cur = cur.get_next()

    par1 = lis.head
    par2 = new_list.head
    while (par1 != None):
        if (par1.get_data() != par2.get_data()):
            return False
        par1 = par1.get_next()
        par2 = par2.get_next()
    return True


a = LinkedList()
a.insert(6)
a.insert(3)
a.insert(2)
a.insert(6)
a.insert(7)
a.insert(6)
a.insert(2)
a.insert(3)
a.insert(6)
print(pal(a))
