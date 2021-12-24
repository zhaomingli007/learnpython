from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def dp(i):
            """return subarray end with i"""
            if i ==0: return nums[i]
            return max(nums[i], dp(i-1)+nums[i])
        return max(dp(i) for i in range(len(nums)))