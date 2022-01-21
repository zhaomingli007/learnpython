
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
        2,3,
        4,5,6,7
        """
        #for each level
        q = []
        q.append(root)
        def enqueue(node):
            if node.left:
                q.append(node.left)
                q.append(node.right)
                enqueue(node.left)
                enqueue(node.right)
        enqueue(root)
        #1,  2,4,8,
        #2^0,2^1
        n = len(q)
        for i in range(n):
            if 2**i < n-1:
                q[i].right = Node("#")
            if not q[i].right and i<n-1:
                q[i].right = q[i+1]
        for nd in q:
            if nd.right:
                print(nd.right.val)
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
    