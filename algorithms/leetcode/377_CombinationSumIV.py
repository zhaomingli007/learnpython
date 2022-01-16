from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
        Input: nums = [1,2,3], target = 4
        Output: 7
        Explanation:
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.        
        """
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for n in nums:
                if i-n>=0:
                    dp[i]+=dp[i-n]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
    print(s.combinationSum4([9], 3))
