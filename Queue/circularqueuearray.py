class EmptyQueueError(Exception):
    pass
class circularQueue:
    def __init__(self,defult_size=10):
        self.items=[None]*defult_size
        self.front=0
        self.count=0
    def is_empty(self):
        return self.count==0
    def size(self):
        return self.count
    def enqueue(self,item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        i = (self.front+self.count) % len(self.items)
        self.items[i]=item
        self.count+=1
    def dqueue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front+=1
        return x
    def peek(self):
        return self.items[self.front]
    def display(self):
        print(self.items)
    def resize(self,new_size):
        old_list = self.items
        self.items = [None]*new_size
        i=self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i) % len(old_list)
        self.front = 0
