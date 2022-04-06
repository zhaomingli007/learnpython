from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [2,3,1,1,4]
      dp[0,0,0,0,0]
             
        """
        n = len(nums)
        if n <= 1:
            return True

        lst_can_reach = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= lst_can_reach:
                lst_can_reach = i
        return lst_can_reach == 0
