# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_bt(nd, mn=-math.inf, mx=math.inf):
            if not nd:
                return True
            if nd.val <= mn or nd.val >=mx:
                return False
            return is_bt(nd.right, nd.val, mx) and is_bt(nd.left, mn, nd.val)
        
        return is_bt(root)