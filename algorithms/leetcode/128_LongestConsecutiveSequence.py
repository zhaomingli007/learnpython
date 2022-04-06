from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0
        for i in range(len(nums)):
            # only build the seq start the smallest num.
            if nums[i] - 1 not in s:
                cur_n = nums[i]
                cur_l = 1
                while cur_n + 1 in s:
                    cur_n += 1
                    cur_l += 1

                longest = max(longest, cur_l)

        return longest
