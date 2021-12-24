
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # [2,2,3,3,3,4]
        # if nums = [], return 0
        # if nums = [2], return 2
        # if nums = [2, 2], delete nums[0], go through nums and mark as deleted for same value -1 and +1
        # if nums = [2, 2, 3], 
        # dp[i] = max(nums[i] + dp(i-1), dp(i-1))
        house = [0]*(10 ** 4 + 1)
        for x in nums:
            house[x] += x
        def dp(i):
            if i < 0:return 0
            return max(house[i]+dp(i-2), dp(i-1))
        return dp(len(nums)-1)
        
        