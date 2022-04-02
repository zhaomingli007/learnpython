# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import DefaultDict, List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        [(3, 0)]
        
        
        """
        if not root:
            return []
        
        stk = [(root, 0)]
        
        ans = DefaultDict(list)
        
        
        while stk:
            nd, l = stk.pop(0)
            if l in ans:
                if l % 2 == 0:
                    ans[l].append(nd.val)
                else:
                    ans[l].insert(0,nd.val)
            else:
                ans[l] = [nd.val]
            lft, rit = nd.left, nd.right
            if lft:
                stk.append((lft, l+1))
            if rit:
                stk.append((rit, l+1))
        # print(ans)
        return list(ans.values())