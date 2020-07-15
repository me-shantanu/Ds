class EmptyStackError(Exception):
    pass
class Node:
    def __init__(self,value):
        self.info = value
        self.link = None
class stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top == None
    def size(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty")
        count = 0
        p = self.top
        while p is not None:
            count+=1
            p=p.link
        return count
    def push(self,item):
        temp = Node(item)
        temp.link = self.top
        self.top = temp
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        poped = self.top.info
        self.top = self.top.link
        return poped
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.top.info
    def display(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        print("stack is : ")
        p = self.top
        while p is not None:
            print(p.info," ",end='\n')
            p=p.link
