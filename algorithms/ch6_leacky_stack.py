from typing import ChainMap


class LeakStack:
    _capacity = 0
    _array = []
    _curren_head = 0
    def __init__(self, capacity):
        self._capacity = capacity
        self._array = [None] * capacity
    
    def push(self, element):
        self._array[self._curren_head] = element
        self._curren_head = (self._curren_head + 1) % self._capacity
        #Full
        
    def pop(self):
        if self._curren_head == 0:
            self._curren_head = self._capacity-1
        else:
            self._curren_head -= 1
        print('index {0}'.format(self._curren_head))
        poped = self._array[self._curren_head]
        self._array[self._curren_head] = None
        return poped
    
    def print(self):
        print(self._array)
        
        
if __name__ == '__main__':
    leak_stack = LeakStack(10)
    leak_stack.push(1)
    leak_stack.push(2)
    p = leak_stack.pop()
    print(p)
    p = leak_stack.pop()
    print(p)
    p = leak_stack.pop()
    print(p)
    leak_stack.push(2)
    leak_stack.push(3)
    leak_stack.push(3)
    leak_stack.push(4)
    leak_stack.push(5)
    leak_stack.print()
    leak_stack.push(6)
    leak_stack.push(7)
    leak_stack.push(8)
    leak_stack.print()
    leak_stack.push(9)
    leak_stack.push(10)
    leak_stack.push(11)
    leak_stack.push(12)
    leak_stack.push(13)
    leak_stack.print()
    leak_stack.pop()
    leak_stack.print()
    leak_stack.push(13)
    leak_stack.print()
