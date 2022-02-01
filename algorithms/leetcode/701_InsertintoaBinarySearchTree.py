# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Input: root = [4,2,7,1,3], val = 5
        Output: [4,2,7,1,3,5] 
        
        Input: root = [40,20,60,10,30,50,70], val = 25
        Output: [40,20,60,10,30,50,70,null,null,25]               
        """
        if not root:
            return TreeNode(val)

        mid , parent = root, root
        while mid:
            parent = mid 
            if mid.val < val:
                mid = mid.right
            elif mid.val > val:
                mid = mid.left
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root
            
            
if __name__ == '__main__':
    s = Solution()
    l1 = TreeNode(1)
    l3 = TreeNode(3)
    l2 = TreeNode(2,l1,l3)
    l7 = TreeNode(7)
    l4 = TreeNode(4,l2,l7)

    ans = s.insertIntoBST(l4, 5)
    print(ans)
    
    