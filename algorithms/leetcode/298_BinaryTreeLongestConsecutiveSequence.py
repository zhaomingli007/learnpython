
from typing import Optional
class Solution:
    # your task is to complete this function
    # function should print the top view of the binary tree
    # Note: You aren't required to print a new line after every test case
    def __init__(self):
        self.mx = -1
        
    def longestConsecutive(self, root: Optional[Node]) -> int:
        """
        """
        if not root:
            return 0
        
        def rec(node,pval, k):
            if k>1:
                self.mx =  max(self.mx , k)
            if not node:
                return
            if node:
                if node.data == pval +1:
                    k+=1
                    rec(node.left, node.data, k)
                    rec(node.right, node.data, k)
                    k-=1
                else:
                    rec(node.left, node.data, 1)
                    rec(node.right, node.data, 1)

        rec(root,-1, 1)
        return self.mx

if __name__ == '__main__':
    s = Solution()
    n11 = Node(11)
    n10 = Node(val=10)
    n10.right = n11
    
    n7 = Node(7)
    n9 = Node(9)
    n9.left = n7
    n9.right = n10
    
    n6 = Node(val = 6)
    n6.right = n9
    print(s.longestConsecutive(n6))
    
    # n1 = Node(1)
    # n2 = Node(2, n1)
    # n3 = Node(3, n2)
    # n2_2 = Node(val=2, right=n3)
    # s2 = Solution()
    # print(s2.longestConsecutive(n2_2))
    