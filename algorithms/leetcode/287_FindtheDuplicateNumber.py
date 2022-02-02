from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Input: nums = [1,3,4,2,2]
        Output: 2     
        from index 1, compare 3->1; 
                              4->3,4->1,
                              2->4,2->3,2->1
                              2->2,2->4,2->1
        """
        # sorted_nums = sorted(nums)
        # for i in range(1,len(sorted_nums)):
        #     if sorted_nums[i] == sorted_nums[i-1]:
        #         return sorted_nums[i]
        # return -1
        s = set()
        for c in nums:
            if c in s:
                return c
            else:
                s.add(c)
        return -1
