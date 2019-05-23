from LinkedList import *

def loop_det(lis):
    slow = lis.head
    fast = lis.head

    while (fast != None and fast.get_next() != None):
        slow = slow.get_next()
        fast = fast.get_next().get_next()

        if (slow == fast):
            break
    if (fast == None or fast.get_next() == None):
        return False
    slow = lis.head
    while (slow != fast):
        slow = slow.get_next()
        fast = fast.get_next()
    return fast
