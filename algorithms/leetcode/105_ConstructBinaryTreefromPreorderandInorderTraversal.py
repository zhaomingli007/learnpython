# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def sub_tree(l, r):
            if l > r:
                return None
            # if l == r:
            #     return TreeNode(val=inorder[l])

            v = preorder.pop(0)
            root = TreeNode(val=v)
            v_idx = inorder.index(v)
            root.left = sub_tree(l, v_idx-1)
            root.right = sub_tree(v_idx+1, r)
            return root
                
            
        return sub_tree(0, len(inorder)-1)