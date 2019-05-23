from LinkedList import *
from Node import *

def sum_list(lis1, lis2):
    check = 0
    while(lis1.size() != lis2.size()):
            if lis1.size() < lis2.size():
                lis1.insert(0)
            else:
                lis2.insert(0)
    num1 = lis1.head
    num2 = lis2.head
    new_num = LinkedList()
    add_two(num1, num2, new_num)
    return new_num

def add_two(num1, num2, num):
    if num1 != None:
        check = add_two(num1.get_next(), num2.get_next(), num)
        if check + num1.get_data() + num2.get_data() > 10:
            num.insert(check + num1.get_data() + num2.get_data() - 10)
        else:
            num.insert(check + num1.get_data() + num2.get_data())
        return ((num1.get_data() + num2.get_data() + check) // 10)
    else:
        return 0


a = LinkedList()
a.insert(6)
a.insert(3)
a.insert(2)
a.insert(6)
a.printNode()

b = LinkedList()
b.insert(3)
b.insert(5)
b.insert(3)
b.printNode()

new = sum_list(a, b)
new.printNode()
