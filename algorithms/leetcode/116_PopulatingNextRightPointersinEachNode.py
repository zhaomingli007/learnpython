
# Definition for a Node.
from json.tool import main
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        """
           1,
         2,  3,
        4,5,6,7
        """
        if not root:
            return None
        l, r, n = root.left, root.right, root.next
        if l:
            l.next = r
            if n:
                r.next = n.left
            self.connect(l)
            self.connect(r) 
        return root
            
          

if __name__ == '__main__':
    s = Solution()
    
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, n4, n5)
    n6 = Node(6)
    n7 = Node(7)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)
    
    
    s.connect(n1)
    
