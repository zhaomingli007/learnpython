from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,3]
        
        1.[1][2][3]
        2.[1,2],[2,3][1,3]
        3.[1,2,3]
        """
        ans = []
        n = len(nums)

        def bt(cur=[], idx=0):
            nonlocal ans
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(idx, n):
                cur.append(nums[i])
                bt(cur, i+1)
                cur.pop()
        for k in range(n+1):
            bt()
        return ans
