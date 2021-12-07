
        
class _DoubleLinkedBase:
    class _Node:
        __slots__='_element', '_prev', '_next'    
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._next = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_beteen(self, e, pre, next):
        newe = self._Node(e, pre, next)
        pre._next = newe
        next._prev = newe
        self._size+=1
        return newe
    
    def _delete_node(self, node):
        prv =  node._prev
        nxt = node._next
        prv._next = nxt
        nxt._prev = prv
        self._size -=1
        element = node._element
        node._prev = node._next = node._element = None # Free node
        return element
    
        
        
class LinkedQueue(_DoubleLinkedBase):
    
    def first(self):
        if self.is_empty():
            raise ValueError("Deque(Double ended queue) is empty")
        return self._header._next.element
    
    def last(self):
        if self.is_empty():
            raise ValueError("Deque(Double ended queue) is empty")
        return self._tailer._prev.element
    
    def insert_first(self, e):
        self._insert_beteen(e, self._header, self._header._next)
        
    def insert_last(self, e):
        self._insert_beteen(e, self._tailer._prev, self._tailer)
        
    def delete_first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")    
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._tailer._prev)
            

class PositionalList(_DoubleLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._tailer:
            return None #Boundary
        else:
            return self.Position(self, node)
    
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._tailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    def _insert_beteen(self, e, pre, next):
        node = super()._insert_beteen(e, pre, next)
        return self._make_position(node)

    def _add_first(self, e):
        return self._insert_beteen(e, self._header, self._header._next)
    

    def _add_last(self, e):
        return self._insert_beteen(e, self._tailer._prev, self._tailer)

    def _add_before(self, p, e):
        ori = self._validate(p)
        return self._insert_beteen(e, ori._prev, ori)
    
    def _add_after(self, p, e):
        ori = self._validate(p)
        return self._insert_beteen(e, ori, ori._next)
    
    def _delete(self, p):
        ori = self._validate(p)
        return self._delete_node(ori)

    def _replace(self, p, e):
        ori = self._validate(p)
        ov = ori._element
        ori._element = e
        return ov
