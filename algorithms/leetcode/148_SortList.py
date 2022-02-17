# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [4,2,1,3]        
        """
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        l = self.sortList(head)
        r = self.sortList(mid)
        return self.merge(l, r)

    def get_mid(self, node):
        sl, fa = None, node
        while fa and fa.next:
            sl = (node if not sl else sl.next)
            fa = fa.next.next
        m = sl.next
        sl.next = None
        # print(m.val)
        return m

    def merge(self, first, second):
        dh = ListNode()
        t = dh
        while first and second:
            if first.val < second.val:
                t.next = first
                first = first.next
            else:
                t.next = second
                second = second.next
            t = t.next
        if first:
            t.next = first
        else:
            t.next = second
        return dh.next
