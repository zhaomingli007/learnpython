from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def dp(i):
            """return max length of sub array with positive product and """
            if i < 0 or nums[0] == 0: return 0, 0
            max_len_pos, max_len_neg = dp(i-1)
            if nums[i] > 0:
                return max_len_pos +1, max_len_neg+1 if max_len_neg else 0
            else: 
                return max_len_neg+1 if max_len_neg else 0, max_len_pos+1
                    
