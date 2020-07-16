class EmptyQueueError(Exception):
    pass
class queue:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.append(item)
    def dqueue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[0]
    def display(self):
        print(self.items)
    
    