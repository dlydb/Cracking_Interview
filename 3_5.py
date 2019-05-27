from Stack import *

def sort_stack(stack1):
    stack2 = Stack()
    while (stack1.isEmpty() == False):
        tmp = stack1.pop()
        count = 0
        while (stack2.isEmpty() == False):
            if (stack2.peek() > tmp):
                stack1.push(stack2.pop())
                count += 1
            else:
                stack2.push(tmp)
                break
        if stack2.isEmpty() == True:
            stack2.push(tmp)
        while (count > 0):
            stack2.push(stack1.pop())
            count -= 1
    return stack2

a = Stack()
a.push(8)
a.push(5)
a.push(4)
a.push(10)
a.push(7)

b = sort_stack(a)
b.printNode()
