from typing import List


class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
      """ two cases. case 1. similary to normal array, get the max sub array, case 2. the max subarray would be like: -subfix-> [at least one ele] -prefix->  
      """
      n = len(nums)
      @cache
      def dp(i, s):
          """ max sub-array until i"""
          if i == 0: return nums[i]*s
          return max(nums[i]*s, dp(i-1, s)+nums[i]*s)
      max_p = max(dp(i, 1) for i in range(n))
      max_n = max(dp(i, -1) for i in range(n))
      return max_p if max_p <0 else max(max_p, sum(nums) + max_n)
          
