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
                    i
                        j , j>n
                        
        [1], n = 1
         i
         j, j = n
         [1,2], n = 2
          i
            j =n 
         if j == n: i = i.next
         [1], n = 0
          i
          j n = 0 return head
         
        """
        if n == 0:
            return head
        fast, slow = head, head
        i = 0
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        if i == n:
            head = head.next
        else:
            slow.next = slow.next.next
        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,slow = head, head
        cnt = 0
        while fast:
            if cnt > n:
                slow = slow.next
            fast = fast.next
            cnt+=1
        if cnt > n:
            slow.next = slow.next.next
        else:
            head = head.next
        return head