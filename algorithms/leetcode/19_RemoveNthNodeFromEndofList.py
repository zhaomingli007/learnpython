# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2,3,4,5], n = 2
                i   j    
        """
        fast, slow = head, head
        i = 0 
        while not fast.next:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        slow.next = slow.next.next
        return head
