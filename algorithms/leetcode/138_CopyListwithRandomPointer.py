
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        q = []
        new_h = Node(x = head.val)

        q.append(head)
        visited = {head: new_h}
        
        
        
        while len(q) > 0:
            nd = q.pop()
            nxt = nd.next
            rd = nd.random
            #New node
            n_nd = visited[nd]
            #Next
            if nxt:
                if nxt not in visited:
                    n_nd.next = Node(x=nxt.val)                
                    q.append(nxt)
                    visited[nxt] = n_nd.next
                else:
                    n_nd.next = visited[nxt]

            #Randome    
            if rd:
                if rd not in visited:
                    n_nd.random = Node(x=rd.val)
                    q.append(rd)
                    visited[rd] = n_nd.random
                else:
                    n_nd.random = visited[rd]

        return new_h
        