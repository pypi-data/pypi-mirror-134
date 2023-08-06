"""
FIFO
enqueue
dequeue
is_empty

"""
from typing import Generic, TypeVar

T = TypeVar("T")

class QueueOverFlow(BaseException):
    pass

class QueueUnderFlow(BaseException):
    pass


class Queue(Generic[T]):
    """Represents a Queue data structure
    """
    def __init__(self, limit: int = 10):
        self.entries: list[T] = []
        self.limit = limit
    
    def enqueue(self, item):
        if len(self.entries) > self.limit:
            raise QueueOverFlow
        self.entries.append(item)
    
    def dequeue(self):
        if not self.entries:
            raise QueueUnderFlow
        return self.entries.pop()
    
    def is_empty(self):
        return not bool(self.entries)
    
    def size(self):
        return len(self.entries)
