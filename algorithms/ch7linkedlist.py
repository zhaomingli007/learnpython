
class LinkedStack:
    """" LIFO Stack implementation"""
    class _Node:
        __slots__ = '_element', '_next'
    
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        """ Create an empty stack"""
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        if self.is_empty():
            raise ValueError('stack is empty ')
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer 

class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._tail = None
        self._size = 0

        def __len__(self):
            return self._size
        def is_empty(self):
            return self._size == 0
        
        def first(self):
            if self.is_empty():
                raise ValueError("empty queue")
            head = self._tail._next
            return head._element
        
        def dequeue(self):
            if self.is_empty():
                raise ValueError("empty queue")
            head = self._tail._next
            if self._size == 1:
                self._tail = None
            else:
                self._tail._next = head._next
            self._size -=1
            return head._element
        
        def enqueue(self,e):
            newnode = self._Node(e, None)
            if self.is_empty():
                newnode._next = newnode
            else:
                newnode._next = self._tail._next
                self._tail._next = newnode
            self._tail = newnode
            self._size += 1
            
        
            
