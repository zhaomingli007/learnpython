from typing import List, Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i<=1:
                return 0 
            return min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])
        return dp(len(cost))
            
if __name__ == '__main__':
    s = Solution()
    r = s.minCostClimbingStairs([10, 15, 20])
    print(r)
    
