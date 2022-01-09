from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)] # Length of increasing subsequence start from i to j
        for i in range(n):
            dp[i][i] = 1
        max_len = 1
        for j in range(n):
            for i in range(j-1, -1, -1):
                if i<j:
                    prev_max = max(dp[i+1][j], dp[i][j-1])
                    dp[i][j] = 1+prev_max if nums[j] > nums[i] else prev_max
                    max_len = max(dp[i][j],max_len)
        return max_len                    
        