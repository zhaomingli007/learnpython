# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.found = False
        self.target = None
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        if not root:
            return None
        def rec(current):
            if not current or  self.target:
                return
            if p.val < current.val:
                current.right = None #remove the right branch since the next successor must be in left tree
            if p.val > current.val:
                current.left = None

            rec(current.left)
            #access root
            print(current.val)
            if not self.target and self.found:
                self.target = current
            if current.val == p.val:
                self.found = True
            rec(current.right)
        rec(root)
        return self.target