from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if not root:
                return 0
            return 1 + getDepth(root.left)
        # Compare left sub tree and right sub tree
        # Time complexity: log(n)*log(n)
        # Perfect binary tree node size: 2^(k+1) - 1, k is tree depth.
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            # If the depth of the left tree equals the depth of right tree, then right tree is a perfect tree.
            # left tree size +1, 2^(leftDepth+1) - 1
            return 2 ** leftDepth + self.countNodes(root.right)
        else:
            # If they are not equals, then right tree is a perfect tree
            return 2**rightDepth + self.countNodes(root.left)


