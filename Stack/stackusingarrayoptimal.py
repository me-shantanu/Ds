class EmptyStackError(Exception):
    pass
class StackFullError(Exception):
    pass
class stack:
    def __init__(self,max_size=10):
        self.items=[None]*max_size
        self.count=0
    def size(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == len(self.items)
    def push(self,item):
        if self.is_full():
            raise StackFullError("Stack is Full")
        self.items[self.count] = item
        self.count+=1
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        x =  self.items[self.count-1]
        self.items[self.count-1] =None
        self.count-=1
        return x
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[self.count-1]
    def display(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty")
        print(self.items)