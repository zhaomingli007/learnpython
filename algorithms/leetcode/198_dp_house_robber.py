from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i:int)->int:
            if i < 0:
                return 0
            return max(nums[i] + dp(i-2), dp(i-1))
        return dp(len(nums) - 1)
            
