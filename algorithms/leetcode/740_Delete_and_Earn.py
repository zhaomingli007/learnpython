
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # [2,2,3,3,3,4]
        # if nums = [], return 0
        # if nums = [2], return 2
        # if nums = [2, 2], delete nums[0], go through nums and mark as deleted for same value -1 and +1
        # if nums = [2, 2, 3], 
        # dp[i] = max(nums[i] + dp(i-1), dp(i-1))

        
