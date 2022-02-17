# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
       3
       5,1
       6,2,0,8
       7,4
       {(3,x),(5,3),(1,3),(6,5),(2,5),(0,1),(8,1),(7,2),(4,2)}
        
       p=7, q = 8
       loop until root:
       (2)(1)
       (5)(3x)
       p=6, q = 4:
       set(5,2)
       (3,5)
        
        
        """
        if not root:
            return None
        p_map = {root.val:None}
        qu = [root]
        while len(qu) > 0:
            cur = qu.pop(0)
            if cur.left:
                qu.append(cur.left)
                p_map[cur.left.val] = cur
            if cur.right:
                qu.append(cur.right)
                p_map[cur.right.val] = cur
        for k in p_map:
            print(k, p_map[k].val if p_map[k] else None)
        
        path = set()
        while p or q:
            if p and p.val in path:
                return p
            if q and q.val in path:
                return q
            if p:
                path.add(p.val)
                p = p_map[p.val]
            if q:
                path.add(q.val)
                q = p_map[q.val]
            if p == q:
                return p
            
        return root
            
