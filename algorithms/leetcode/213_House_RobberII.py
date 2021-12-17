from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,3,2]
        # [1,2,3,1]
        # if nums = [], return 0, if nums=[x] return x, if len(nums) == 2 return max(nums[x, y]), if len(nums) > 2, return max(dp[i-2]+nums[i], dp[i-1]) 
        n = len(nums)
        if n == 1: return nums[0]
        #i: rob from 0, or 1, thus the last house will either cannot rob or can rob
        def dp(i, j):
            if j < i: return 0
            return max(nums[j] + dp(i, j-2), dp(i, j-1))
        return max(dp(0, n-2), dp(1, n-1))
            
