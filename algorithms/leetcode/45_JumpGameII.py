from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dp(i):
            """Return min step from i to n-1"""
            if i>=n-1: return 0
            if i + nums[i]>=n-1: return 1
            minStep = n
            for x in range(1, nums[i]+1):
                minStep =  min(minStep, dp(i+x)+1)
            return minStep
        return dp(0)
            
