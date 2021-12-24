from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            """
            Return number of sub array arith slices from 0 to i"""
            if i<2: return 0
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                return 1+ dp(i-1)
            return 0
        return sum(dp(i) for i in range(len(nums)))        
