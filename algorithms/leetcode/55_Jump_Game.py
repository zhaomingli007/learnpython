from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Returns whether we can reach n - 1 from i."""
        #  [2,3,1,1,4]
        n = len(nums)
        def dp(i): #
            if i >= n -1:return True
            if i + nums[i] >= n-1: return True
            for x in range(1, nums[i]+1):
                if dp(i+x): return True
            return False
        return dp(0)