# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]        
        """
        if not root:
            return []
        ans = {}
        q = [(1,root)]
        while len(q) > 0:
            level , t = q.pop(0)
            if level in ans:
                arr = ans[level]
            else:
                arr = []
            if t.left:
                q.append((level+1, t.left))
                arr.append(t.left.val)
            if t.right:
                q.append((level+1, t.right))
                arr.append(t.right.val)
            if len(arr) > 0:
                ans[level] = arr
        ans = {0:[root.val], **ans}
        return list(ans.values())
    
if __name__ == '__main__':
    s = Solution()
    l1 = TreeNode(9)
    
    l2 = TreeNode(15)
    r2 = TreeNode(7)
    r1 = TreeNode(20, l2, r2)
    
    
    r = TreeNode(3, l1, r1)
    
    print(s.levelOrder(r))
    
                
                
        