class EmptyQueueError(Exception):
    pass
class queue:
    def __init__(self):
        self.items = []
        self.front = 0
    def is_empty(self):
        return self.items == self.front

    def size(self):
        return len(self.items) - self.front
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front+=1
        return x
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items[self.front]
    def display(self):
        print(self.items)
